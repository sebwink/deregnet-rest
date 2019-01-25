from pymongo.collection import Collection

from redis import StrictRedis

from deregnet_rest.models.run_info import RunInfo
from deregnet_rest import util

import deregnet_rest.resources.xdata as X
from deregnet_rest.controllers.controller import Controller
from deregnet_rest.controllers.graphs import Graphs
from deregnet_rest.controllers.scores import Scores
from deregnet_rest.controllers.nodesets import NodeSets
from deregnet_rest.controllers.parameter_sets import ParameterSets
from deregnet_rest.controllers.subgraphs import Subgraphs

class RunQueue:

    def __init__(self, redis_server):
        self.redis = StrictRedis(port=redis_server.port,
                                 host=redis_server.host,
                                 #password=redis_server.passwd,
                                 )

    def push(self, run_id):
        self.redis.lpush('deregnet_run_queue', run_id)

    def pop(self):
        return self.redis.rpop('deregnet_run_queue')

    def delete(self, run_id):
        self.redis.lrem('deregnet_run_queue', 1, run_id)

    def __len__(self):
        return self.redis.llen('deregnet_run_queue')


class Runs(Collection, Controller):
    '''

    '''
    def __init__(self, client):
        super().__init__(client.deregnet_rest, name='runs')
        self._client = client
        self._queue = RunQueue(client.redis)


    @property
    def queue(self):
        return self._queue

    @property
    def graphs(self):
        return self._client.graphs

    @property
    def scores(self):
        return self._client.scores

    @property
    def parameter_sets(self):
        return self._client.parameter_sets

    @property
    def nodesets(self):
        return self._client.nodesets

    @Controller.api_call
    def delete_run(self, run_id):
        # TODO. Delete completed runs
        deletion = self.delete_one(filter={
            'id': run_id,
            'started': False,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid run ID', 400
        self.queue.delete(run_id)
        return 'Run successfully deleted', 201

    @Controller.api_call
    def get_run(self, run_id):
        run_info = self.find_one(filter={
            'id': run_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not run_info:
            return 'Invalid run ID', 400
        return util.deserialize_model(run_info, RunInfo)

    @Controller.api_call
    def get_runs(self, searchString, skip, limit):
        return [
            util.deserialize_model(run_info, RunInfo)
            for run_info in self.find(filter={
                'X-Consumer-ID': X.consumer_id()
            })
        ]

    @Controller.api_call
    def post_run(self, body):
        '''

        '''
        run_input = body.to_dict()
        run_input = {k: v for k,v in run_input.items() if v is not None}
        
        graph_id = run_input['graph_id']
        score_id = run_input.get('score_id')
        receptors_id = run_input.get('receptors_id')
        terminals_id = run_input.get('treminals_id')
        exclude_id = run_input.get('exclude_id')
        include_id = run_input.get('include_id')
        parameter_set_id = run_input.get('parameter_set_id')
 
        x_consumer_id = X.consumer_id()
 
        valid, message = self.validate_run(
            x_consumer_id,
            graph_id,
            score_id,
            receptors_id,
            terminals_id,
            exclude_id,
            include_id,
            parameter_set_id
        )
        if not valid:
            return 'Invalid run, invalid %s encountered, check your run input' % message, 400

        # generate run info and insert into database
        default_parameters = self.parameter_sets.get_parameter_set_default_data()
        if not parameter_set_id:
            parameter_set = default_parameters
        else:
            parameter_set = self.parameter_sets.get_parameter_set_as_dict(parameter_set_id)
        parameter_set = {**default_parameters, **parameter_set}
        parameter_set = {**parameter_set, **{k:v for k,v in run_input.get('parameter_set', {}).items() if v is not None}}

        run_input['parameter_set'] = parameter_set
        
        
        run_info = {
                     'id': self.generate_id(),
                     'post_time': self.timestamp('-'),
                     'started': False,
                     'done': False,
                     'subgraph_ids': [],
                     'run_input': run_input
                   }

        self.insert_one({
            **run_info,
            'X-Consumer-ID': x_consumer_id,
        })
        run_id = run_info['id']
        # push run onto the job queue
        self.queue.push(run_id)
        # register new run dependencies
        self.graphs.dependent_runs[graph_id] = run_id
        self.update_dependent_runs(run_id, score_id, self.scores)
        self.update_dependent_runs(run_id, terminals_id, self.nodesets)
        self.update_dependent_runs(run_id, receptors_id, self.nodesets)
        self.update_dependent_runs(run_id, exclude_id, self.nodesets)
        self.update_dependent_runs(run_id, include_id, self.nodesets)
        self.update_dependent_runs(run_id, parameter_set_id, self.parameter_sets)
        return util.deserialize_model(run_info, RunInfo)

    @classmethod
    def update_dependent_runs(cls, run_id, val, coll):
        if val:
            coll.dependent_runs[val] = run_id

    def validate_run(self,
                     x_consumer_id,
                     graph_id,
                     score_id,
                     receptors_id,
                     terminals_id,
                     exclude_id,
                     include_id,
                     parameter_set_id):
        if not self.graphs.find_one(filter={
            'id': graph_id,
            'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'graph ID %s' % graph_id
        if not self.scores.find_one(filter={
            'id': score_id,
            'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'score ID %s' % score_id
        if not self.nodeset_valid(receptors_id, x_consumer_id):
            return False, self.invalid_nodeset(receptors_id)
        if not self.nodeset_valid(terminals_id, x_consumer_id):
            return False, self.invalid_nodeset(terminals_id)
        if not self.nodeset_valid(exclude_id, x_consumer_id):
            return False, self.invalid_nodeset(exclude_id)
        if not self.nodeset_valid(include_id, x_consumer_id):
            return False, self.invalid_nodeset(include_id)
        if parameter_set_id and not \
           self.parameter_sets.find_one(filter={
               'id': parameter_set_id,
               'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'parameter set ID %s' % parameter_set_id
        return True, None

    def nodeset_valid(self, ID, x_consumer_id):
        if ID and not \
           self.nodesets.find_one(filter={
               'id': ID,
               'X-Consumer-ID': x_consumer_id,
           }):
            return False
        return True

    @classmethod
    def invalid_nodeset(cls, ID):
        return 'nodeset ID %s' % ID

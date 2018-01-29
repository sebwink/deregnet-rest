import time
import multiprocessing as mp

from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection

from redis import StrictRedis

from deregnet.core import AverageDeregnetArguments
from deregnet.core import SubgraphFinder

from deregnet_rest.models.run_info import RunInfo
from deregnet_rest import util

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
                                 password=redis_server.passwd)

    def push(self, run_id):
        self.redis.lpush('deregnet_run_queue', run_id)

    def pop(self):
        return self.redis.rpop('deregnet_run_queue')

    def delete(self, run_id):
        self.redis.lrem('deregnet_run_queue', 1, run_id)

    def __len__(self):
        return self.redis.llen('deregnet_run_queue')



class _Runner:
    def __init__(self, mongo_config, redis_server):
        self._client = MongoClient(**mongo_config)
        self._graphs = Graphs(self._client)
        self._scores = Scores(self._client)
        self._nodesets = NodeSets(self._client)
        self._parameter_sets = ParameterSets(self._client)
        self._runs = Runs(self._client,
                          redis_server)
        self._subgraphs = Subgraphs(self._client)

    @property
    def graphs(self):
        return self._graphs

    @property
    def scores(self):
        return self._scores

    @property
    def nodesets(self):
        return self._nodesets

    @property
    def paramter_sets(self):
        return self._parameter_sets

    @property
    def runs(self):
        return self._runs

    @property
    def subgraphs(self):
        return self._subgraphs

    @property
    def queue(self):
        return self._runs.queue

    def run(self):
        '''

        '''
        run_id = self.queue.pop()
        if not run_id:
            print('No runs to run ...')
            time.sleep(5)
            return
        else:
            run_id = run_id.decode('utf-8')
        print('Running run %s ...' % run_id)
        run_info = self.runs.find_one_and_update(filter={'id': run_id},
                                                 update={'$set': {'started': True}})
        run_input = run_info['run_input']
        args = {}
        args['root'] = run_input.get('root')
        args['scores'] = self.get_score(run_input)
        args['receptors'] = self.get_receptors(run_input)
        args['terminals'] = self.get_terminals(run_input)
        args['included_nodes'] = self.get_include(run_input)
        args['excluded_nodes'] = self.get_exclude(run_input)
        self.set_parameters(run_input, args)
        try:
            args = AverageDeregnetArguments(**args)
        except:
            pass
        graph, id_attr = self.get_graph(run_input)
        run = SubgraphFinder(graph, id_attr)
        try:
            subgraphs = run.run(args)
        except:
            pass
        self.register_subgraphs(subgraphs, run_id)

    def get_graph(self, run_input):
        graph_id = run_input['graph_id']
        graph_data = self.graphs.graph_data(graph_id)
        return self.graphs.igraph_from_graph_data(graph_data), graph_data['node_id_attr']

    def get_score(self, run_input):
        score_id = run_input.get('score_id')
        if not score_id:
            return {}
        return self.scores.score_as_dict(score_id)

    def get_nodeset(self, run_input, nodeset):
        nodeset_id = run_input.get(nodeset+'_id')
        if not nodeset_id:
            return None
        return self.nodesets.nodeset_as_list(nodeset_id)

    def get_receptors(self, run_input):
        return self.get_nodeset(run_input, 'receptors')

    def get_terminals(self, run_input):
        return self.get_nodeset(run_input, 'terminals')

    def get_include(self, run_input):
        return self.get_nodeset(run_input, 'include')

    def get_exclude(self, run_input):
        return self.get_nodeset(run_input, 'exclude')

    def set_parameters(self, run_input, args):
        parameter_set_id = run_input.get('paramter_set_id')
        default_parameters = self.paramter_sets.get_parameter_set_default_data()
        if not parameter_set_id:
            parameter_set = default_parameters
        else:
            parameter_set = self.parameter_sets.get_parameter_set_data(parameter_set_id)
        parameter_set = {**default_parameters.to_dict(), **parameter_set.to_dict()}
        args = {**args, **parameter_set}

    def register_subgraphs(self, subgraphs, run_id):
        subgraph_ids = self.subgraphs.register_subgraphs(subgraphs, run_id)
        self.runs.update_one(filter={'id': run_id},
                             update={'$set': {'done': True, 'subgraph_ids': subgraph_ids}})


class Runner:

    def __init__(self, mongo_config, redis_server):
        self._p = mp.Process(target=self.run,
                             args=(mongo_config, redis_server,),
                             daemon=True)
        self._p.start()

    def run(self, mongo_config, redis_server):
        runner = _Runner(mongo_config, redis_server)
        while True:
            runner.run()


class Runs(Collection, Controller):
    '''

    '''
    def __init__(self, client, redis_server):
        super().__init__(client.deregnet_rest, name='runs')
        self._client = client
        self._queue = RunQueue(redis_server)


    @property
    def queue(self):
        return self._queue

    @Controller.api_call
    def delete_run(self, run_id):
        deletion = self.delete_one(filter={'id': run_id, 'started': False})
        if not deletion:
            return 'Invalid run ID', 400
        self.queue.delete(run_id)
        return 'Run successfully deleted', 201

    @Controller.api_call
    def get_run(self, run_id):
        run_info = self.find_one(filter={'id': run_id})
        if not run_info:
            return 'Invalid run ID', 400
        return util.deserialize_model(run_info, RunInfo)

    @Controller.api_call
    def get_runs(self, searchString, skip, limit):
        return [ util.deserialize_model(run_info, RunInfo)
                 for run_info in self.find() ]

    @Controller.api_call
    def post_run(self, body):
        '''

        '''
        run_input = body.to_dict()
        run_input = {k: v for k,v in run_input.items() if v is not None}
        if not self.validate_run(run_input):
            return 'Invalid run, invalid IDs encountered', 400
        run_info = {
                     'id': self.generate_id(),
                     'post_time': self.timestamp('-'),
                     'started': False,
                     'done': False,
                     'subgraph_ids': [],
                     'run_input': run_input
                   }
        self.insert_one( run_info )
        self.queue.push( run_info['id'] )
        return util.deserialize_model(run_info, RunInfo)

    def validate_run(self, run_input):
        return True

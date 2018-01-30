from pymongo.collection import Collection

from redis import StrictRedis

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

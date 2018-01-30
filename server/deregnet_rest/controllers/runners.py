import sys
import time
import multiprocessing as mp

from deregnet.core import AverageDeregnetArguments
from deregnet.core import SubgraphFinder

from deregnet_rest.resources.mongodb import Database

from deregnet_rest.controllers.controller import Controller

class _Runner(Database):
    def __init__(self,
                 mongo_config,
                 mongod,
                 redis_server,
                 runner_id=None,
                 run_search_interval=20,
                 log_file=None):
        super().__init__(mongo_config['username'], mongo_config['password'], mongod, redis_server)
        self._id = runner_id
        self._run_search_interval = run_search_interval
        if log_file:
            sys.stdout = open(log_file, 'w', buffering=1)

    def __del__(self):
        if sys.stdout != sys.__stdout__:
            sys.stdout.close()

    @property
    def queue(self):
        return self._runs.queue

    @property
    def wait_time(self):
        return self._run_search_interval

    def run(self):
        '''

        '''
        run_id = self.queue.pop()
        if not run_id:
            timestamp = Controller.timestamp('-')
            print('%s: No runs to run ...' % timestamp)
            time.sleep(self.wait_time)
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
        default_parameters = self.parameter_sets.get_parameter_set_default_data()
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

    def __init__(self,
                 mongo_config,
                 mongod,
                 redis_server,
                 runner_id,
                 run_search_interval,
                 log_file):
        self._p = mp.Process(target=self.run,
                             args=(mongo_config,
                                   mongod,
                                   redis_server,
                                   runner_id,
                                   run_search_interval,
                                   log_file,),
                             daemon=True)
        self._p.start()

    def run(self, mongo_config, mongod, redis_server, runner_id, run_search_interval, log_file):
        runner = _Runner(mongo_config, mongod, redis_server, runner_id, run_search_interval, log_file)
        while True:
            runner.run()


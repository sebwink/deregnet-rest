import sys
import time
import multiprocessing as mp

from deregnet.core import AverageDeregnetArguments
from deregnet.core import SubgraphFinder

from deregnet_rest.resources.database import DatabaseServer

from deregnet_rest.controllers.controller import Controller

class _Runner(DatabaseServer):
    '''

    '''
    def __init__(self,
                 mongo_config,
                 mongod,
                 redis_server,
                 runner_id=0,
                 run_search_interval=2,
                 log_file=None):
        '''

        '''
        super().__init__(mongo_config['username'],
                         mongo_config['password'],
                         mongod,
                         redis_server)
        self._id = runner_id
        self._run_search_interval = run_search_interval
        self.log_file = log_file
        if log_file:
            sys.stdout = open(log_file, 'a', buffering=1)

    def startup_message(self):
        timestamp = Controller.datetime()
        print('%s %s: Starting runner%s ...' % (self.namelog, timestamp, self.id))

    def shutdown_message(self):
        timestamp = Controller.datetime()
        print('%s %s: Stopping runner%s ...' % (self.namelog, timestamp, self.id))

    def __del__(self):
        self.shutdown_message()
        if sys.stdout != sys.__stdout__:
            sys.stdout.close()

    @property
    def id(self):
        return self._id

    @property
    def queue(self):
        return self._runs.queue

    @property
    def wait_time(self):
        return self._run_search_interval

    @property
    def namelog(self):
        return '(runner%s)' % str(self.id)

    def run(self):
        '''

        '''
        run_id = self.queue.pop()
        timestamp = Controller.datetime()
        if not run_id:
            print('%s %s: No runs to run ...' % (self.namelog, timestamp))
            time.sleep(self.wait_time)
            return
        else:
            run_id = run_id.decode('utf-8')
        print('%s %s:Running run %s ...' % (self.namelog, timestamp, run_id))
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
        #args = self.set_parameters(run_input, args)
        args = {**args, **run_input['parameter_set']}
        #try:
        args = AverageDeregnetArguments(**args)
        #except:
            # TODO

        #    print('Parameter construction failed')
        #    return
        graph, id_attr = self.get_graph(run_input)
        tempdir = 'data/runs/runner'+str(self.id)
        finder = SubgraphFinder(graph,
                                id_attr,
                                tmp_file_path=tempdir,
                                log_file=self.log_file)
        try:
            subgraphs = finder.run(args)
        except:
            print('Subgraph run failed')
            # TODO
            return
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

    def run(self, *args):
        runner = _Runner(*args)
        runner.startup_message()
        while True:
            runner.run()

    @property
    def process(self):
        return self._p

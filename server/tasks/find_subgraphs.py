from celery import Celery

from deregnet.core import AverageDeregnetArguments
from deregnet.core import SubgraphFinder

from deregnet_rest.config import Config
from deregnet_rest.database.collections.graphs import graphs
from deregnet_rest.database.collections.scores import scores
from deregnet_rest.database.collections.nodesets import nodesets
from deregnet_rest.database.collections.runs import runs
from deregnet_rest.database.collections.subgraphs import subgraphs

class Runner:
    '''

    '''
    def run(self, run_id):
        '''

        '''
        run_info = runs.find_one_and_update(filter={'id': run_id},
                                            update={'$set': {'started': True}})
        run_input = run_info['run_input']
        args = {}
        args['root'] = run_input.get('root')
        args['scores'] = self.get_score(run_input)
        args['receptors'] = self.get_receptors(run_input)
        args['terminals'] = self.get_terminals(run_input)
        args['included_nodes'] = self.get_include(run_input)
        args['excluded_nodes'] = self.get_exclude(run_input)
        args = {**args, **run_input['parameter_set']}
        try:
            args = AverageDeregnetArguments(**args)
        except:
            # TODO

            print('Parameter construction failed')
            return
        graph, id_attr = self.get_graph(run_input)
        finder = SubgraphFinder(graph, id_attr)
        try:
            subgraphs = finder.run(args)
        except:
            print('Subgraph run failed')
            # TODO
            return
        x_consumer_id = run_info['X-Consumer-ID']
        self.register_subgraphs(subgraphs, run_id, x_consumer_id)

    def get_graph(self, run_input):
        graph_id = run_input['graph_id']
        graph_data = graphs.graph_data(graph_id)
        return graphs.igraph_from_graph_data(graph_data), graph_data['node_id_attr']

    def get_score(self, run_input):
        score_id = run_input.get('score_id')
        if not score_id:
            return {}
        return scores.score_as_dict(score_id)

    def get_nodeset(self, run_input, nodeset):
        nodeset_id = run_input.get(nodeset+'_id')
        if not nodeset_id:
            return None
        return nodesets.nodeset_as_list(nodeset_id)

    def get_receptors(self, run_input):
        return self.get_nodeset(run_input, 'receptors')

    def get_terminals(self, run_input):
        return self.get_nodeset(run_input, 'terminals')

    def get_include(self, run_input):
        return self.get_nodeset(run_input, 'include')

    def get_exclude(self, run_input):
        return self.get_nodeset(run_input, 'exclude')

    def register_subgraphs(self, _subgraphs, run_id, x_consumer_id):
        subgraph_ids = subgraphs.register_subgraphs(_subgraphs, run_id, x_consumer_id)
        runs.update_one(filter={'id': run_id, 'X-Consumer-ID': x_consumer_id},
                        update={'$set': {'done': True, 'subgraph_ids': subgraph_ids}})

REDIS_URI = 'redis://{}:{}/1'.format(Config.redis_host(), Config.redis_port())
CELERY = Celery('main', broker=REDIS_URI)
RUNNER = Runner()

@CELERY.task
def find_subgraphs(run_id):
    RUNNER.run(run_id)

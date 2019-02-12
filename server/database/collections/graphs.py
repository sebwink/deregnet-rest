import pymongo
import igraph as ig

from deregnet_rest.utils.redis import RedisSetDict

from deregnet_rest.database.connection import database

class Graphs(pymongo.collection.Collection):
    '''

    '''

    GRAPH_DATA_PROJ = {
                        '_id': False,
                        'graphmlz': True,
                        'node_id_attr': True
                      }

    GRAPH_INFO_PROJ = {
                        '_id': False,
                        'graphmlz': False,
                        'node_id_attr': False,
                        'runs': False
                      }

    def __init__(self, client):
        '''

        '''
        super().__init__(client.deregnet_rest, name='graphs')
        self._depruns = RedisSetDict('graph2run')

    @property
    def dependent_runs(self):
        return self._depruns

    def graph_data(self, graph_id):
        '''
        Retrieve a graph as an igraph Graph
        '''
        graph_data = self.find_one(
            filter={
                'id': graph_id,
            },
            projection=self.GRAPH_DATA_PROJ
        )
        return graph_data

    @classmethod
    def igraph_from_graph_data(cls, graph_data):
        return ig.Graph.Read_GraphMLz(graph_data['graphmlz'])


graphs = Graphs(database)

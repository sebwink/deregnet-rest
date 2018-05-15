import pymongo

from deregnet_rest.models.graph_info import GraphInfo
from deregnet_rest import util

from deregnet_rest.resources.redis import RedisSetDict
from deregnet_rest.controllers.controller import Controller

import os
import igraph as ig

class Graphs(pymongo.collection.Collection, Controller):
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

    def __init__(self, client, graph_storage='data/graphs'):
        '''

        '''
        super().__init__(client.deregnet_rest, name='graphs')
        self._graphs = graph_storage
        self._depruns = RedisSetDict('graph2run', client.redis)

    def dependent_runs(self, graph_id):
        return self._depruns

    @Controller.api_call
    def delete_graph(self, graph_id):
        '''

        '''
        if not self.dependent_runs.is_empty(graph_id):
            return 'Invalid graph ID: some runs depend on this graph', 400
        graph_path = self.find_one_and_delete(filter={'id': graph_id},
                                              projection=self.GRAPH_DATA_PROJ)
        if not graph_path:
            return 'Invalid graph ID: no graph with that ID', 400
        os.remove(graph_path['graphmlz'])
        return 'Graph successfully deleted', 201

    @Controller.api_call
    def get_graph(self, graph_id):
        '''

        '''
        graph_info = self.find_one(filter={'id': graph_id},
                                   projection=self.GRAPH_INFO_PROJ)
        if not graph_info:
            return 'Invalid graph ID: no graph with that ID', 400
        return util.deserialize_model(graph_info, GraphInfo)

    @Controller.api_call
    def get_graphs(self, searchString, skip, limit):
        '''

        '''
        graph_infos = self.find(projection=self.GRAPH_INFO_PROJ)
        return [ util.deserialize_model(graph_info, GraphInfo)
                 for graph_info in graph_infos ]

    @Controller.api_call
    def post_graph(self, initial_graph_info):
        '''

        '''
        graph_info = {
                       'id': self.generate_id(),
                       'time_of_upload': self.timestamp('-'),
                       'name': initial_graph_info.name,
                       'description': initial_graph_info.description,
                       'num_nodes': 0,
                       'num_edges': 0
                     }
        graph_data = {
                       'graphmlz': os.path.join(self._graphs,
                                                graph_info['id']+'.graphml.gz'),
                       'node_id_attr': initial_graph_info.node_id_attr
                     }
        self.insert_one( { **graph_info, **graph_data } )
        return util.deserialize_model(graph_info, GraphInfo)

    @Controller.api_call
    def post_graphml(self, graph_id, file_to_upload):
        '''

        '''
        graph = self.find_one(filter={'id': graph_id})
        if not graph:
            return 'Invalid graph ID', 400
        if os.path.isfile(graph['graphmlz']):
            return 'A graph with that ID is already uploaded', 409
        file_to_upload.save(graph['graphmlz'])
        try:
            G = ig.Graph.Read_GraphML(graph['graphmlz'])
        except:
            try:
                G = ig.Read_GraphMLz(graph['graphmlz'])
            except:
                return 'Invalid GraphML file (igraph)', 400
        self.update_one(filter={'id': graph_id},
                        update={ '$set': {'num_nodes': len(G.vs), 'num_edges': len(G.es)} })
        G.write_graphmlz(graph['graphmlz'])
        return 'GraphML successfully uploaded', 201

    # ------------------------------------------------------------------------- #

    def graph_data(self, graph_id):
        '''
        Server-side method to retrieve a graph as an igraph Graph
        '''
        graph_data = self.find_one(filter={'id': graph_id},
                                   projection=self.GRAPH_DATA_PROJ)
        return graph_data

    @classmethod
    def igraph_from_graph_data(cls, graph_data):
        return ig.Graph.Read_GraphMLz(graph_data['graphmlz'])

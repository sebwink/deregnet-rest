import os
import bson
import pymongo
import igraph as ig

from deregnet_rest.utils.redis import RedisSetDict

from deregnet_rest.database.connection import database
from deregnet_rest.database.files import files

class Graphs(pymongo.collection.Collection):
    '''

    '''
    GRAPH_DATA_PROJ = {
                        '_id': False,
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

    def get_ig(self, graph_id):
        graph_data = self.find_one({ 'id': graph_id })
        if graph_data is None:
            return None
        file_id = graph_data.get('file_id')
        if file_id is None:
            return None
        return self.ig_from_file_id(file_id)

    def ig_from_file_id(self, file_id):
        f = files.get(bson.objectid.ObjectId(file_id))
        temporary_file = '/tmp/{}.graphml.gz'
        with open(temporary_file, 'wb') as fp:
            fp.write(f.read())
        try:
            graph = ig.Graph.Read_GraphMLz(temporary_file)
        except:
            graph = None
        os.remove(temporary_file)
        return graph


graphs = Graphs(database)

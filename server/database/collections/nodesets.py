import pymongo

from deregnet_rest.utils.redis import RedisSetDict
from deregnet_rest.database.connection import database

class NodeSets(pymongo.collection.Collection):
    '''

    '''

    NODESET_INFO_PROJ = {
                          '_id': False,
                          'nodes': False
                        }

    NODESET_DATA_PROJ = {
                          '_id': False,
                          'nodes': True
                        }

    def __init__(self, client):
        '''

        '''
        super().__init__(client.deregnet_rest, name='nodesets')
        self._depruns = RedisSetDict('nodeset2run')

    @property
    def dependent_runs(self):
        return self._depruns

    def nodeset_as_list(self, nodeset_id):
        '''
        Server-side method to retrieve a nodeset as a list
        '''
        nodeset_data = self.find_one(filter={'id': nodeset_id},
                                     projection=self.NODESET_DATA_PROJ)
        if not nodeset_data:
            return None
        return nodeset_data['nodes']

nodesets = NodeSets(database)

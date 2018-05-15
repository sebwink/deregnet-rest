import pymongo

from deregnet_rest.models.node_set import NodeSet
from deregnet_rest.models.node_set_info import NodeSetInfo
from deregnet_rest import util

from deregnet_rest.resources.redis import RedisSetDict
from deregnet_rest.controllers.controller import Controller

class NodeSets(pymongo.collection.Collection, Controller):
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
        self._depruns = RedisSetDict('nodeset2run', client.redis)

    @property
    def dependent_runs(self):
        return self._depruns

    @Controller.api_call
    def delete_nodeset(self, nodeset_id):
        '''

        '''
        if not self.dependent_runs.is_empty(nodeset_id):
            return 'Invalid nodeset ID: some runs depend on this nodeset', 400
        deletion = self.delete_one(filter={'id': nodeset_id})
        if not deletion:
            return 'Invalid nodeset ID: No nodeset with that ID', 400
        return 'Node set successfully deleted', 201

    @Controller.api_call
    def get_nodeset(self, nodeset_id):
        '''

        '''
        nodeset_info = self.find_one(filter={'id': nodeset_id},
                                     projection=self.NODESET_INFO_PROJ)
        if not nodeset_info:
            return 'Invalid node set Id', 400
        return util.deserialize_model(nodeset_info, NodeSetInfo)

    @Controller.api_call
    def get_nodesets(self, searchString, skip, limit):
        '''

        '''
        nodeset_infos = self.find(projection=self.NODESET_INFO_PROJ)
        return [ util.deserialize_model(nodeset_info, NodeSetInfo)
                 for nodeset_info in nodeset_infos ]

    @Controller.api_call
    def post_nodeset(self, body):
        '''

        '''
        # compose nodeset_info and document for database
        nodeset_info = {
                         'description': body.description,
                         'id': self.generate_id(),
                         'size': len(body.nodes),
                         'time_of_upload': self.timestamp('-')
                        }
        document = {
                     **nodeset_info,
                     **{'nodes': body.nodes}
                   }
        # insert into database and return NodeSetInfo
        self.insert_one(document)
        return util.deserialize_model(nodeset_info, NodeSetInfo)


    # ------------------------------------------------------------------------- #

    def nodeset_as_list(self, nodeset_id):
        '''
        Server-side method to retrieve a nodeset as a list
        '''
        nodeset_data = self.find_one(filter={'id': score_id},
                                     projection=self.NODESET_DATA_PROJ)
        if not nodeset_data:
            return None
        return nodeset_data['nodes']

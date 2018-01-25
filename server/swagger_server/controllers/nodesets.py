import pymongo

from swagger_server.models.node_set import NodeSet
from swagger_server.models.node_set_info import NodeSetInfo
from swagger_server import util

from swagger_server.controllers.controller import Controller

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

    def __init__(self, db):
        '''

        '''
        super().__init__(db, name='nodesets')

    def delete_nodeset(self, nodeset_id):
        '''

        '''
        deletion = self.delete_one(filter={'id': nodeset_id})
        if not deletion:
            return 'Invalid score ID', 400
        return 'Node set successfully deleted', 201

    def get_nodeset(self, nodeset_id):
        '''

        '''
        nodeset_info = self.find_one(filter={'id': nodeset_id},
                                     projection=self.NODESET_INFO_PROJ)
        if not nodeset_info:
            return 'Invalid node set Id', 400
        return util.deserialize_model(nodeset_info, NodeSetInfo)

    def get_nodesets(self, searchString, skip, limit):
        '''

        '''
        nodeset_infos = self.find(projection=self.NODESET_INFO_PROJ)
        return [ util.deserialize_model(nodeset_info, NodeSetInfo)
                 for nodeset_info in nodeset_infos ]

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

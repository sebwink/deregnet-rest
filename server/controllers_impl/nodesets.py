from deregnet_rest.models.node_set_info import NodeSetInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X
from deregnet_rest.controllers_impl.base import Controller

from deregnet_rest.database.collections.nodesets import nodesets

class NodesetController(Controller):
    '''

    '''
    @classmethod
    @Controller.api_call
    def delete_nodeset(cls, nodeset_id):
        '''

        '''
        if not nodesets.dependent_runs.is_empty(nodeset_id):
            return 'Invalid nodeset ID: some runs depend on this nodeset', 400
        deletion = nodesets.delete_one(filter={
            'id': nodeset_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid nodeset ID: No nodeset with that ID', 400
        return 'Node set successfully deleted', 201

    @classmethod
    @Controller.api_call
    def get_nodeset(cls, nodeset_id):
        '''

        '''
        nodeset_info = nodesets.find_one(
            filter={
                'id': nodeset_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=nodesets.NODESET_INFO_PROJ
        )
        if not nodeset_info:
            return 'Invalid node set Id', 400
        return util.deserialize_model(nodeset_info, NodeSetInfo)

    @classmethod
    @Controller.api_call
    def get_nodesets(cls, searchString, skip, limit):
        '''

        '''
        nodeset_infos = nodesets.find(
            filter={'X-Consumer-ID': X.consumer_id()},
            projection=nodesets.NODESET_INFO_PROJ
        )
        return [ util.deserialize_model(nodeset_info, NodeSetInfo)
                 for nodeset_info in nodeset_infos ]

    @classmethod
    @Controller.api_call
    def post_nodeset(cls, body):
        '''

        '''
        # compose nodeset_info and document for database
        nodeset_info = {
            'description': body.description,
            'size': len(body.nodes),
            'time_of_upload': cls.timestamp('-')
        }
        x_consumer_id = X.consumer_id()
        document = {
            **nodeset_info,
            'nodes': body.nodes,
            'X-Consumer-ID': x_consumer_id,
        }
        # insert into database and return NodeSetInfo
        _id = nodesets.insert_one(document).inserted_id
        nodeset_id = cls.generate_uuid(_id)
        nodesets.update_one(
            filter={
                '_id': _id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': {
                    'id': nodeset_id,
                },
            }
        )
        nodeset_info['id'] = nodeset_id
        return util.deserialize_model(nodeset_info, NodeSetInfo)

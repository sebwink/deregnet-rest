import os
import gzip

from deregnet_rest.models.subgraph_info import SubgraphInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X
from deregnet_rest.controllers_impl.base import Controller
from deregnet_rest.database.collections.subgraphs import subgraphs

class SubgraphController(Controller):
    @classmethod
    @Controller.api_call
    def delete_subgraph(cls, subgraph_id):
        deletion = subgraphs.delete_one(filter={
            'id': subgraph_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid subgraph ID', 400
        return 'Subgraph successfully deleted', 201

    @classmethod
    @Controller.api_call
    def download_subgraph_as(cls, subgraph_id, filetype):
        subgraph_path = subgraphs.find_one(filter={
            'id': subgraph_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not subgraph_path:
            return 'Invalid subgraph ID', 400
        if filetype == 'graphml':
            with gzip.open(subgraph_path['graphmlz'], 'r') as graphml:
                content_disposition = 'attachment; filename='+subgraph_id+'.graphml'
                return graphml.read(), 200, {'Content-Disposition': content_disposition}

    @classmethod
    @Controller.api_call
    def get_subgraph(cls, subgraph_id):
        subgraph_info = subgraphs.find_one(
            filter={
                'id': subgraph_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=subgraphs.SUBGR_INFO_PROJ
        )
        if not subgraph_info:
            return 'Invalid subgraph ID', 400
        return util.deserialize_model(subgraph_info, SubgraphInfo)

    @classmethod
    @Controller.api_call
    def get_subgraphs(cls, searchString, skip, limit):
        subgraph_infos = subgraphs.find(
            filter={'X-Consumer-ID': X.consumer_id()},
            projection=subgraphs.SUBGR_INFO_PROJ
        )
        return [ util.deserialize_model(subgraph_info, SubgraphInfo)
                 for subgraph_info in subgraph_infos ]

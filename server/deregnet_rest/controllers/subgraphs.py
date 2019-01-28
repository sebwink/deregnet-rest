import os
import gzip
import igraph as ig

from pymongo.collection import Collection

from deregnet_rest.models.subgraph_info import SubgraphInfo
from deregnet_rest import util

import deregnet_rest.resources.xdata as X
from deregnet_rest.controllers.controller import Controller


class Subgraphs(Collection, Controller):

    SUBGR_INFO_PROJ = {
                        '_id': False,
                        'graphmlz': False
                      }

    SUBGR_PATH_PROJ = {
                        '_id': False,
                        'graphmlz': True
                      }

    def __init__(self, client, subgraph_storage='data/subgraphs'):
        super().__init__(client.deregnet_rest, name='subgraphs')
        self._subgraphs = subgraph_storage

    def register_subgraphs(self, subgraphs, run_id, x_consumer_id):
        rundir = os.path.join(self._subgraphs, run_id)
        os.makedirs(rundir)
        subgraph_ids = []
        for i in range(len(subgraphs.subgraphs)):
            subgraph_info = {
                'run_id': run_id,
                'score': subgraphs.avg_scores[i],
                'optimal': True, # TODO
                'optimality_type': 'optimal' if i == 0 else 'suboptimal:'+str(i),
                'num_nodes': len(subgraphs.subgraphs[i].vs),
                'num_edges': len(subgraphs.subgraphs[i].es),
                'root': 'ABC' # TODO
            }
            _id = self.insert_one({
                **subgraph_info,
                'X-Consumer-ID': x_consumer_id,
            }).inserted_id
            subgraph_id = self.generate_uuid(str(_id)+str(i))
            subgraph_path = os.path.join(rundir, subgraph_id+'.graphml.gz')
            self.update_one(
                filter={
                    '_id': _id,
                    'X-Consumer-ID': x_consumer_id,
                },
                update={
                    '$set': {
                        'id': subgraph_id,
                        'graphmlz': subgraph_path,
                    },
                }
            )
            subgraphs.to_graphmlz(i, subgraph_path)
            subgraph_info['id'] = subgraph_id
            subgraph_ids.append(subgraph_info['id'])
        return subgraph_ids

    @Controller.api_call
    def delete_subgraph(self, subgraph_id):
        deletion = self.delete_one(filter={
            'id': subgraph_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid subgraph ID', 400
        return 'Subgraph successfully deleted', 201

    @Controller.api_call
    def download_subgraph_as(self, subgraph_id, filetype):
        subgraph_path = self.find_one(filter={
            'id': subgraph_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not subgraph_path:
            return 'Invalid subgraph ID', 400
        if filetype == 'graphml':
            with gzip.open(subgraph_path['graphmlz'], 'r') as graphml:
                content_disposition = 'attachment; filename='+subgraph_id+'.graphml'
                return graphml.read(), 200, {'Content-Disposition': content_disposition}

    @Controller.api_call
    def get_subgraph(self, subgraph_id):
        subgraph_info = self.find_one(
            filter={
                'id': subgraph_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=self.SUBGR_INFO_PROJ
        )
        if not subgraph_info:
            return 'Invalid subgraph ID', 400
        return util.deserialize_model(subgraph_info, SubgraphInfo)

    @Controller.api_call
    def get_subgraphs(self, searchString, skip, limit):
        subgraph_infos = self.find(
            filter={'X-Consumer-ID': X.consumer_id()},
            projection=self.SUBGR_INFO_PROJ
        )
        return [ util.deserialize_model(subgraph_info, SubgraphInfo)
                 for subgraph_info in subgraph_infos ]

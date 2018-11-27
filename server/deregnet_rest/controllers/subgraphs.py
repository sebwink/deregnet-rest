import os
import gzip
import igraph as ig

from pymongo.collection import Collection

from deregnet_rest.models.subgraph_info import SubgraphInfo
from deregnet_rest import util

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

    def register_subgraphs(self, subgraphs, run_id):
        rundir = os.path.join(self._subgraphs, run_id)
        os.makedirs(rundir)
        subgraph_ids = []
        for i in range(len(subgraphs.subgraphs)):
            subgraph_info = {
                              'run_id': run_id,
                              'id': self.generate_id(),
                              'score': subgraphs.avg_scores[i],
                              'optimal': True, # TODO
                              'optimality_type': 'optimal' if i == 0 else 'suboptimal:'+str(i),
                              'num_nodes': len(subgraphs.subgraphs[i].vs),
                              'num_edges': len(subgraphs.subgraphs[i].es),
                              'root': 'ABC' # TODO
                            }
            subgraph_data = {
                              'graphmlz': os.path.join(rundir, subgraph_info['id']+'.graphml.gz')
                            }
            subgraphs.to_graphmlz(i, subgraph_data['graphmlz'])
            self.insert_one( {**subgraph_info, **subgraph_data} )
            subgraph_ids.append(subgraph_info['id'])
        return subgraph_ids

    @Controller.api_call
    def delete_subgraph(self, subgraph_id):
        deletion = self.delete_one(filter={'id': subgraph_id})
        if not deletion:
            return 'Invalid subgraph ID', 400
        return 'Subgraph successfully deleted', 201

    @Controller.api_call
    def download_subgraph_as(self, subgraph_id, filetype):
        subgraph_path = self.find_one(filter={'id': subgraph_id})
        if not subgraph_path:
            return 'Invalid subgraph ID', 400
        if filetype == 'graphml':
            with gzip.open(subgraph_path['graphmlz'], 'r') as graphml:
                content_disposition = 'attachment; filename='+subgraph_id+'.graphml'
                return graphml.read(), 200, {'Content-Disposition': content_disposition}

    @Controller.api_call
    def get_subgraph(self, subgraph_id):
        subgraph_info = self.find_one(filter={'id': subgraph_id},
                                      projection=self.SUBGR_INFO_PROJ)
        if not subgraph_info:
            return 'Invalid subgraph ID', 400
        return util.deserialize_model(subgraph_info, SubgraphInfo)

    @Controller.api_call
    def get_subgraphs(self, searchString, skip, limit):
        subgraph_infos = self.find(projection=self.SUBGR_INFO_PROJ)
        return [ util.deserialize_model(subgraph_info, SubgraphInfo)
                 for subgraph_info in subgraph_infos ]

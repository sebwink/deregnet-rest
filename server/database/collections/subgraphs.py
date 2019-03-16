import os
import pymongo

from deregnet_rest.controllers_impl.base import Controller
from deregnet_rest.database.connection import database


class Subgraphs(pymongo.collection.Collection):

    SUBGR_INFO_PROJ = {
                        '_id': False,
                        'graphmlz': False
                      }

    SUBGR_PATH_PROJ = {
                        '_id': False,
                        'graphmlz': True
                      }

    def __init__(self, client):
        super().__init__(client.deregnet_rest, name='subgraphs')

    def register_subgraphs(self, subgraphs, graph_id, node_id_attr, run_id, x_consumer_id):
        subgraph_ids = []
        for i, subgraph in enumerate(subgraphs.subgraphs):
            subgraph_info = {
                'run_id': run_id,
                'score': subgraphs.avg_scores[i],
                'optimal': True, # TODO
                'optimality_type': 'optimal' if i == 0 else 'suboptimal:'+str(i),
                'num_nodes': len(subgraph.vs),
                'num_edges': len(subgraph.es),
                'root': 'ABC' # TODO
            }
            _id = self.insert_one({
                **subgraph_info,
                'X-Consumer-ID': x_consumer_id,
                'nodes': {v[node_id_attr]: v['deregnet_score'] for v in subgraph.vs},
                'graph_id': graph_id,
                'node_id_attr': node_id_attr,
            }).inserted_id
            subgraph_id = Controller.generate_uuid(str(_id)+str(i))
            self.update_one(
                filter={
                    '_id': _id,
                    'X-Consumer-ID': x_consumer_id,
                },
                update={
                    '$set': {
                        'id': subgraph_id,
                    },
                }
            )
            subgraph_info['id'] = subgraph_id
            subgraph_ids.append(subgraph_info['id'])
        return subgraph_ids


subgraphs = Subgraphs(database)

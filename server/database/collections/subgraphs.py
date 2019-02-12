import os
import pymongo

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


subgraphs = Subgraphs(database)

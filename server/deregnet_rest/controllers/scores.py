from pymongo.collection import Collection

from deregnet_rest.models.score import Score
from deregnet_rest.models.score_info import ScoreInfo
from deregnet_rest import util

import deregnet_rest.resources.xdata as X
from deregnet_rest.resources.redis import RedisSetDict
from deregnet_rest.controllers.controller import Controller

class Scores(Collection, Controller):
    '''

    '''

    SCORE_INFO_PROJ = {
                        '_id': False,
                        'node_ids': False,
                        'score_values': False
                      }

    SCORE_DATA_PROJ = {
                        '_id': False,
                        'node_ids': True,
                        'score_values': True
                      }

    def __init__(self, client):
        '''

        '''
        super().__init__(client.deregnet_rest, name='scores')
        self._depruns = RedisSetDict('score2run', client.redis)

    @property
    def dependent_runs(self):
        return self._depruns

    @Controller.api_call
    def delete_score(self, score_id):
        '''

        '''
        if not self.dependent_runs.is_empty(score_id):
            return 'Invalid score ID: runs depend on this score', 400
        deletion = self.delete_one(filter={
            'id': score_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid score ID', 400
        return 'Score successfully deleted', 201

    @Controller.api_call
    def get_score(self, score_id):
        '''

        '''
        score_info = self.find_one(
            filter={
                'id': score_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=self.SCORE_INFO_PROJ
        )
        if not score_info:
            return 'Invalid ID', 400
        return util.deserialize_model(score_info, ScoreInfo)

    @Controller.api_call
    def get_scores(self, searchString=None,
                         skip=None,
                         limit=None):
        '''

        '''
        score_infos = self.find(
                filter={'X-Consumer-ID': X.consumer_id()},
                projection=self.SCORE_INFO_PROJ
        )
        return [ util.deserialize_model(score_info, ScoreInfo)
                 for score_info in score_infos ]

    @Controller.api_call
    def post_score(self, body):
        '''

        '''
        if len(body.node_ids) != len(body.score_values):
            return 'node_ids and score_values do not have matching size', 409
        # compose score_info and document for database
        score_info = {
                       'description': body.description,
                       'id': None,
                       'size': len(body.node_ids),
                       'time_of_upload': self.timestamp('-')
                     }
        score_data = {
                       'node_ids': body.node_ids,
                       'score_values': body.score_values
                     }
        # insert into database and return ScoreInfo
        x_consumer_id = X.consumer_id()
        _id = self.insert_one({
            **score_info,
            **score_data,
            'X-Consumer-ID': x_consumer_id,
        }).inserted_id
        score_id = self.generate_uuid(_id)
        self.update_one(
            filter={
                '_id': _id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': {
                    'id': score_id,
                },
            }
        )
        score_info['id'] = score_id
        return util.deserialize_model(score_info, ScoreInfo)

    # ------------------------------------------------------------------------- #

    def score_as_dict(self, score_id):
        '''
        Server-side method to retrieve a score as a dictionary.
        '''
        score_data = self.find_one(filter={'id': score_id},
                                   projection=self.SCORE_DATA_PROJ)
        if not score_data:
            return None
        return dict(zip(score_data['node_ids'], score_data['score_values']))

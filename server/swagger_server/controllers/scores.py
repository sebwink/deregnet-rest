import pymongo

from swagger_server.models.score import Score
from swagger_server.models.score_info import ScoreInfo
from swagger_server import util

from swagger_server.controllers.controller import Controller

class Scores(pymongo.collection.Collection, Controller):
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

    def __init__(self, db):
        '''

        '''
        super().__init__(db, name='scores')

    @Controller.api_call
    def delete_score(self, score_id):
        '''

        '''
        deletion = self.delete_one(filter={'id': score_id})
        if not deletion:
            return 'Invalid score ID', 400
        return 'Score successfully deleted', 201

    @Controller.api_call
    def get_score(self, score_id):
        '''

        '''
        score_info = self.find_one(filter={'id': score_id},
                                   projection=self.SCORE_INFO_PROJ)
        if not score_info:
            return 'Invalid ID', 400
        return util.deserialize_model(score_info, ScoreInfo)

    @Controller.api_call
    def get_scores(self, searchString=None,
                         skip=None,
                         limit=None):
        '''

        '''
        score_infos = self.find(projection=self.SCORE_INFO_PROJ)
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
                       'id': self.generate_id(),
                       'size': len(body.node_ids),
                       'time_of_upload': self.timestamp('-')
                     }
        score_data = {
                       'node_ids': body.node_ids,
                       'score_values': body.score_values
                     }
        # insert into database and return ScoreInfo
        self.insert_one({ **score_info, **score_data })
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

from deregnet_rest.models.score import Score
from deregnet_rest.models.score_info import ScoreInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X
from deregnet_rest.database.connection import database
from deregnet_rest.controllers_impl.base import Controller

from deregnet_rest.database.collections.scores import scores

class ScoreController(Controller):
    '''

    '''
    @classmethod
    @Controller.api_call
    def delete_score(cls, score_id):
        '''

        '''
        if not scores.dependent_runs.is_empty(score_id):
            return 'Invalid score ID: runs depend on this score', 400
        deletion = scores.delete_one(filter={
            'id': score_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid score ID', 400
        return 'Score successfully deleted', 201

    @classmethod
    @Controller.api_call
    def get_score(cls, score_id):
        '''

        '''
        score_info = scores.find_one(
            filter={
                'id': score_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=scores.SCORE_INFO_PROJ
        )
        if not score_info:
            return 'Invalid ID', 400
        return util.deserialize_model(score_info, ScoreInfo)

    @classmethod
    @Controller.api_call
    def get_scores(cls, skip, limit):
        '''

        '''
        score_infos = scores.find(
            filter={
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=scores.SCORE_INFO_PROJ
        ).skip(skip).limit(limit)
        return [
            util.deserialize_model(score_info, ScoreInfo)
            for score_info in score_infos
        ]

    @classmethod
    @Controller.api_call
    def post_score(cls, body):
        '''

        '''
        if len(body.node_ids) != len(body.score_values):
            return 'node_ids and score_values do not have matching size', 409
        # compose score_info and document for database
        score_info = {
                       'description': body.description,
                       'id': None,
                       'size': len(body.node_ids),
                       'time_of_upload': cls.timestamp('-')
                     }
        score_data = {
                       'node_ids': body.node_ids,
                       'score_values': body.score_values
                     }
        # insert into database and return ScoreInfo
        x_consumer_id = X.consumer_id()
        _id = scores.insert_one({
            **score_info,
            **score_data,
            'X-Consumer-ID': x_consumer_id,
        }).inserted_id
        score_id = cls.generate_uuid(_id)
        scores.update_one(
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

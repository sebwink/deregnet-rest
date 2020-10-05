import pymongo

from deregnet_rest.utils.redis import RedisSetDict

from deregnet_rest.database.connection import database

class Scores(pymongo.collection.Collection):
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
        self._depruns = RedisSetDict('score2run')

    @property
    def dependent_runs(self):
        return self._depruns

    def score_as_dict(self, score_id):
        '''
        Server-side method to retrieve a score as a dictionary.
        '''
        score_data = self.find_one(filter={'id': score_id},
                                   projection=self.SCORE_DATA_PROJ)
        if not score_data:
            return None
        return dict(zip(score_data['node_ids'], score_data['score_values']))



scores = Scores(database)

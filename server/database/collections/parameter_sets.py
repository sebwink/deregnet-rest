import pymongo

from deregnet_rest.database.connection import database
from deregnet_rest.utils.redis import RedisSetDict

class ParameterSets(pymongo.collection.Collection):
    '''

    '''

    PARAMSET_INFO_PROJ = {
                           '_id': False,
                           'id': True,
                           'description': True,
                           'set_parameters': True
                         }

    PARAMSET_DATA_PROJ = {
                           '_id': False,
                           'id': False,
                           'description': False,
                           'set_parameters': False
                         }

    def __init__(self, client, default='data/defaults/parameter_set.yaml'):
        super().__init__(client.deregnet_rest, name='parameter_sets')
        self._default_params = default
        self._depruns = RedisSetDict('parameters2runs')

    @property
    def dependent_runs(self):
        return self._depruns

    def get_parameter_set_default_data(self):
        default = self.read_yaml(self._default_params)
        return default


    def parameter_set_as_dict(self, parameter_set_id):
        '''
        Server-side method to retrieve the parameter set (data) as a dictionary
        '''
        return self.get_parameter_set_data(parameter_set_id).to_dict()


parameter_sets = ParameterSets(database)

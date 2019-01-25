from pymongo.collection import Collection

from deregnet.core import AverageDeregnetArguments

from deregnet_rest.models.parameter_set import ParameterSet
from deregnet_rest.models.parameter_set_info import ParameterSetInfo
from deregnet_rest import util

from deregnet_rest.resources.redis import RedisSetDict
from deregnet_rest.controllers.controller import Controller

class ParameterSets(Collection, Controller):
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
        self._depruns = RedisSetDict('parameters2runs', client.redis)

    @property
    def dependent_runs(self):
        return self._depruns

    @Controller.api_call
    def delete_parameter_set(self, parameter_set_id):
        if not self.dependent_runs.is_empty(parameter_set_id):
            return 'Invalid parameter set ID: runs depend on this parameter set', 400
        deletion = self.delete_one({'id': parameter_set_id})
        if not deletion:
            return 'Invalid parameter set ID: No parameter set with that ID', 400
        return 'Parameter set successfully deleted', 201

    @Controller.api_call
    def get_parameter_set(self, parameter_set_id):
        parameter_set_info = self.find_one(filter={'id': parameter_set_id},
                                           projection=self.PARAMSET_INFO_PROJ)
        if not parameter_set_info:
            return 'Invalid parameter set ID', 400
        return util.deserialize_model(parameter_set_info, ParameterSetInfo)

    @Controller.api_call
    def get_parameter_set_data(self, parameter_set_id):
        parameter_set_data = self.find_one(filter={'id': parameter_set_id},
                                           projection=self.PARAMSET_DATA_PROJ)
        if not parameter_set_data:
            return 'Invalid parameter set ID', 400
        return util.deserialize_model(parameter_set_data, ParameterSet)
    
    @Controller.api_call
    def get_parameter_set_default(self):
        default_info = {
                         'id': '__default__',
                         'description': 'Default parameter set',
                         'set_parameters': list(self.get_parameter_set_default_data().keys())
                       }
        print(default_info)
        return util.deserialize_model(default_info, ParameterSetInfo)

    def get_parameter_set_default_data(self):
        default = self.read_yaml(self._default_params)
        return default

    @Controller.api_call
    def get_parameter_sets(self, searchString, skip, limit):
        parameter_set_infos = self.find(projection=self.PARAMSET_INFO_PROJ)
        return [ util.deserialize_model(parameter_set_info, ParameterSetInfo)
                 for parameter_set_info in parameter_set_infos ]

    @Controller.api_call
    def post_parameter_set(self, body):
        '''

        '''
        parameter_set_data = { key: val for key, val in body.to_dict().items()
                                    if val and key != 'description'}
        try:
            AverageDeregnetArguments(**parameter_set_data)
        except:
            return 'Invalid input data', 409
        parameter_set_info = {
                               'id': self.generate_id(),
                             # 'description': body.description,
                               'set_parameters': list(parameter_set_data.keys())
                             }
        self.insert_one( { **parameter_set_data, **parameter_set_info } )
        return util.deserialize_model(parameter_set_info, ParameterSetInfo)

    # ------------------------------------------------------------------------- #

    def parameter_set_as_dict(self, parameter_set_id):
        '''
        Server-side method to retrieve the parameter set (data) as a dictionary
        '''
        return self.get_parameter_set_data(parameter_set_id).to_dict()

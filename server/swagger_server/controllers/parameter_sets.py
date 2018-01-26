import pymongo

from swagger_server.models.parameter_set import ParameterSet
from swagger_server.models.parameter_set_info import ParameterSetInfo
from swagger_server import util

from swagger_server.controllers.controller import Controller

class ParameterSets(pymongo.collection.Collection, Controller):
    def __init__(self, db, default='data/default/parameter_set.yaml'):
        super().__init__(db, name='parameter_sets')
        self._default = default

    @Controller.api_call
    def delete_parameter_set(self, parameter_set_id):
        pass

    @Controller.api_call
    def get_parameter_set(self, parameter_set_id):
        pass

    @Controller.api_call
    def get_parameter_set_data(self, parameter_set_id):
        pass

    @Controller.api_call
    def get_parameter_set_default(self):
        pass

    @Controller.api_call
    def get_parameter_set_default_data(self):
        default = self.read_yaml(self._default)

    @Controller.api_call
    def get_parameter_sets(self, searchString, skip, limit):
        pass

    @Controller.api_call
    def post_parameter_set(self, body):
        '''

        '''
        parameter_set_data = { key: val for key, val in body.as_dict().items()
                                    if val and key != 'description'}
        parameter_set_info = {
                               'id': self.generate_id(),
                             # 'description': body.description,
                               'set_parameters': list(parameter_set.keys())
                             }
        self.insert_one( { **parameter_set_data, **parameter_set_info } )
        return util.deserialize_model(parameter_set_info, ParameterSetInfo)

    # ------------------------------------------------------------------------- #

    def parameter_set_as_dict(self, parameter_set_id):
        '''
        Server-side method to retrieve the parameter set (data) as a dictionary
        '''
        return self.get_parameter_set_data(parameter_set_id).as_dict()

from deregnet.core import AverageDeregnetArguments

from deregnet_rest.models.parameter_set import ParameterSet
from deregnet_rest.models.parameter_set_info import ParameterSetInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X
from deregnet_rest.controllers_impl.base import Controller
from deregnet_rest.database.collections.parameter_sets import parameter_sets

class ParameterSetController(Controller):
    '''

    '''
    @classmethod
    @Controller.api_call
    def delete_parameter_set(cls, parameter_set_id):
        if not parameter_sets.dependent_runs.is_empty(parameter_set_id):
            return 'Invalid parameter set ID: runs depend on this parameter set', 400
        deletion = parameter_sets.delete_one({
            'id': parameter_set_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid parameter set ID: No parameter set with that ID', 400
        return 'Parameter set successfully deleted', 201

    @classmethod
    @Controller.api_call
    def get_parameter_set(cls, parameter_set_id):
        parameter_set_info = parameter_sets.find_one(
            filter={
                'id': parameter_set_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=parameter_sets.PARAMSET_INFO_PROJ
        )
        if not parameter_set_info:
            return 'Invalid parameter set ID', 400
        return util.deserialize_model(parameter_set_info, ParameterSetInfo)

    @classmethod
    @Controller.api_call
    def get_parameter_set_data(cls, parameter_set_id):
        parameter_set_data = parameter_sets.find_one(
            filter={
                'id': parameter_set_id,
                'X-Consumer-ID': X.consumer_id()
            },
            projection=parameter_sets.PARAMSET_DATA_PROJ
        )
        if not parameter_set_data:
            return 'Invalid parameter set ID', 400
        return util.deserialize_model(parameter_set_data, ParameterSet)

    @classmethod
    @Controller.api_call
    def get_parameter_set_default(cls):
        default_info = {
            'id': '__default__',
            'description': 'Default parameter set',
            'set_parameters': list(parameter_sets.get_parameter_set_default_data().keys())
        }
        return util.deserialize_model(default_info, ParameterSetInfo)

    @classmethod
    @Controller.api_call
    def get_parameter_sets(cls, skip, limit):
        parameter_set_infos = parameter_sets.find(
            filter={'X-Consumer-ID': X.consumer_id()},
            projection=parameter_sets.PARAMSET_INFO_PROJ
        ).skip(skip).limit(limit)
        return [ util.deserialize_model(parameter_set_info, ParameterSetInfo)
                 for parameter_set_info in parameter_set_infos ]

    @classmethod
    @Controller.api_call
    def post_parameter_set(cls, body):
        '''

        '''
        parameter_set_data = { key: val for key, val in body.to_dict().items()
                                    if val and key != 'description'}
        try:
            AverageDeregnetArguments(**parameter_set_data)
        except:
            return 'Invalid input data', 409
        parameter_set_info = {
            # 'description': body.description,
            'set_parameters': list(parameter_set_data.keys()),
        }
        x_consumer_id = X.consumer_id()
        _id = parameter_sets.insert_one({
            **parameter_set_data,
            **parameter_set_info,
            'X-Consumer-ID': x_consumer_id,
        }).inserted_id
        parameter_set_id = cls.generate_uuid(_id)
        parameter_sets.update_one(
            filter={
                '_id': _id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': {
                    'id': parameter_set_id,
                },
            }
        )
        parameter_set_info['id'] = parameter_set_id
        return util.deserialize_model(parameter_set_info, ParameterSetInfo)

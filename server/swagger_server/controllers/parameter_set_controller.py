import connexion
import six

from swagger_server.models.parameter_set import ParameterSet  # noqa: E501
from swagger_server.models.parameter_set_info import ParameterSetInfo  # noqa: E501
from swagger_server import util


def delete_parameter_set(parameter_set_id):  # noqa: E501
    """Delete a previously uploaded parameter collection

    Deletes a parameter collection # noqa: E501

    :param parameter_set_id: ID of the parameter collection to be deleted
    :type parameter_set_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_parameter_set(parameter_set_id):  # noqa: E501
    """Retrieve information on a previously uploaded score

     # noqa: E501

    :param parameter_set_id: ID of parameter collection to retrieve information about
    :type parameter_set_id: str

    :rtype: ParameterSetInfo
    """
    return 'do some magic!'


def get_parameter_set_data(parameter_set_id):  # noqa: E501
    """Retrieve a parameter collection

    Returns a parameter collection # noqa: E501

    :param parameter_set_id: ID of the parameter collection to return
    :type parameter_set_id: str

    :rtype: ParameterSet
    """
    return 'do some magic!'


def get_parameter_set_default():  # noqa: E501
    """Retrieve the defaul parameter collection

    Returns the default parameter collection # noqa: E501


    :rtype: ParameterSetInfo
    """
    return 'do some magic!'


def get_parameter_set_default_data():  # noqa: E501
    """Retrieve information on a previously uploaded score

     # noqa: E501


    :rtype: ParameterSet
    """
    return 'do some magic!'


def get_parameter_sets(searchString=None, skip=None, limit=None):  # noqa: E501
    """List available previously uploaded parameter collections

    Returns a list with information about availabel parameter collections # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[ParameterSetInfo]
    """
    return 'do some magic!'


def post_parameter_set(body):  # noqa: E501
    """Upload a parameters collection for use with DeRegNet algorithms

     # noqa: E501

    :param body: Parameters to be uploaded for later use with a DeRegNet algorithm
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ParameterSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

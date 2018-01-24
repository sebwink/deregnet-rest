import connexion
import six

from swagger_server.models.run_info import RunInfo  # noqa: E501
from swagger_server.models.run_input import RunInput  # noqa: E501
from swagger_server import util


def delete_run(run_id):  # noqa: E501
    """Cancel an active run

    For valid response try integer IDs with positive integer value.\\ \\ Negative or non-integer values will generate API errors # noqa: E501

    :param run_id: ID of the order that needs to be deleted
    :type run_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_run(run_id):  # noqa: E501
    """Retrieve the status of a previously submitted run

    Returns a single pet # noqa: E501

    :param run_id: ID of pet to return
    :type run_id: str

    :rtype: RunInfo
    """
    return 'do some magic!'


def get_runs(searchString=None, skip=None, limit=None):  # noqa: E501
    """List current and past runs

    Returns a single pet # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[RunInfo]
    """
    return 'do some magic!'


def post_run(body):  # noqa: E501
    """Run average score DeRegNet algorithm

     # noqa: E501

    :param body: All data needed to run the algorithm
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RunInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

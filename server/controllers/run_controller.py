import connexion
import six

from deregnet_rest.models.run_info import RunInfo  # noqa: E501
from deregnet_rest.models.run_input import RunInput  # noqa: E501
from deregnet_rest import util


from deregnet_rest.controllers_impl.runs import RunController

def delete_run(run_id):  # noqa: E501
    """Cancel an active run, you cannot delete finished runs

    Cancel a run # noqa: E501

    :param run_id: ID of the run to be deleted
    :type run_id: str

    :rtype: None
    """
    return RunController.delete_run(run_id)


def get_run(run_id):  # noqa: E501
    """Retrieve the status of a previously submitted run

    Returns a single pet # noqa: E501

    :param run_id: ID of pet to return
    :type run_id: str

    :rtype: RunInfo
    """
    return RunController.get_run(run_id)


def get_runs(skip=0, limit=1000):  # noqa: E501
    """List current and past runs

    Returns a single pet # noqa: E501

    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[RunInfo]
    """
    return RunController.get_runs(skip, limit)


def post_run(body):  # noqa: E501
    """Run average score DeRegNet algorithm

     # noqa: E501

    :param body: All data needed to run the algorithm
    :type body: dict | bytes

    :rtype: RunInfo
    """
    if connexion.request.is_json:
        body = RunInput.from_dict(connexion.request.get_json())  # noqa: E501
    return RunController.post_run(body)

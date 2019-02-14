import connexion
import six

from deregnet_rest.models.score import Score  # noqa: E501
from deregnet_rest.models.score_info import ScoreInfo  # noqa: E501
from deregnet_rest import util


from deregnet_rest.controllers_impl.scores import ScoreController

def delete_score(score_id):  # noqa: E501
    """Delete a previously uploaded node score

    Delete a previously uploaded node score # noqa: E501

    :param score_id: ID of the node score to be deleted
    :type score_id: str

    :rtype: None
    """
    return ScoreController.delete_score(score_id)


def get_score(score_id):  # noqa: E501
    """Retrieve information on a previously uploaded score

     # noqa: E501

    :param score_id: ID of node score to return
    :type score_id: str

    :rtype: ScoreInfo
    """
    return ScoreController.get_score(score_id)


def get_scores(skip=0, limit=1000):  # noqa: E501
    """List available previously uploaded node scores

    Returns a list with all available node scores # noqa: E501

    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[ScoreInfo]
    """
    return ScoreController.get_scores(skip, limit)


def post_score(body):  # noqa: E501
    """Upload a node score for use with DeRegNet algorithms

     # noqa: E501

    :param body: Node scores to be uploaded for later use with a DeRegNet algorithm
    :type body: dict | bytes

    :rtype: ScoreInfo
    """
    if connexion.request.is_json:
        body = Score.from_dict(connexion.request.get_json())  # noqa: E501
    return ScoreController.post_score(body)

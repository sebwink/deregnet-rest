import connexion
import six

from swagger_server.models.score import Score  # noqa: E501
from swagger_server.models.score_info import ScoreInfo  # noqa: E501
from swagger_server import util


def delete_score(score_id):  # noqa: E501
    """Delete a previously uploaded node score

    Delete a previously uploaded node score # noqa: E501

    :param score_id: ID of the node score to be deleted
    :type score_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_score(score_id):  # noqa: E501
    """Retrieve information on a previously uploaded score

     # noqa: E501

    :param score_id: ID of node score to return
    :type score_id: str

    :rtype: ScoreInfo
    """
    return 'do some magic!'


def get_scores(searchString=None, skip=None, limit=None):  # noqa: E501
    """List available previously uploaded node scores

    Returns a list with all available node scores # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[ScoreInfo]
    """
    return 'do some magic!'


def post_score(body):  # noqa: E501
    """Upload a node score for use with DeRegNet algorithms

     # noqa: E501

    :param body: Node scores to be uploaded for later use with a DeRegNet algorithm
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Score.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

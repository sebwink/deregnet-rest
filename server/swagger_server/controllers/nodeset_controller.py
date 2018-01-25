import connexion
import six

from swagger_server.models.node_set import NodeSet  # noqa: E501
from swagger_server.models.node_set_info import NodeSetInfo  # noqa: E501
from swagger_server import util


def delete_nodeset(nodeset_id):  # noqa: E501
    """Delete a previously uploaded node set

    Deletes a node set # noqa: E501

    :param nodeset_id: ID of the node set to be deleted
    :type nodeset_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_nodeset(nodeset_id):  # noqa: E501
    """Retrieve information on a previously uploaded node set

     # noqa: E501

    :param nodeset_id: ID of node set to return
    :type nodeset_id: str

    :rtype: NodeSetInfo
    """
    return 'do some magic!'


def get_nodesets(searchString=None, skip=None, limit=None):  # noqa: E501
    """List available previously uploaded node sets

    Returns a list with information of all available node sets # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[NodeSetInfo]
    """
    return 'do some magic!'


def post_nodeset(body):  # noqa: E501
    """Upload a node set for use with DeRegNet algorithms

     # noqa: E501

    :param body: Node set to be uploaded for later use with a DeRegNet algorithm
    :type body: dict | bytes

    :rtype: NodeSetInfo
    """
    if connexion.request.is_json:
        body = NodeSet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

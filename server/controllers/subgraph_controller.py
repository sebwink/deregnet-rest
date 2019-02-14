import connexion
import six

from deregnet_rest.models.subgraph_info import SubgraphInfo  # noqa: E501
from deregnet_rest import util


from deregnet_rest.controllers_impl.subgraphs import SubgraphController

def delete_subgraph(subgraph_id):  # noqa: E501
    """Delete a previously found subgraph

    Deletes a subgraph # noqa: E501

    :param subgraph_id: ID of the order that needs to be deleted
    :type subgraph_id: str

    :rtype: None
    """
    return SubgraphController.delete_subgraph(subgraph_id)


def download_subgraph_as(subgraph_id, filetype):  # noqa: E501
    """Download a subgraph

    With this GET Request you will retrieve a subgraph    # noqa: E501

    :param subgraph_id: The Name of the graph
    :type subgraph_id: str
    :param filetype: File type of file to be downloaded
    :type filetype: str

    :rtype: None
    """
    return SubgraphController.download_subgraph_as(subgraph_id, filetype)


def get_subgraph(subgraph_id):  # noqa: E501
    """Retrieve the information about a subgraph

    Returns a single pet # noqa: E501

    :param subgraph_id: ID of subgraph about which to retrieve information
    :type subgraph_id: str

    :rtype: SubgraphInfo
    """
    return SubgraphController.get_subgraph(subgraph_id)


def get_subgraphs(skip=0, limit=1000):  # noqa: E501
    """List available found subgraphs

    Returns a single pet # noqa: E501

    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[SubgraphInfo]
    """
    return SubgraphController.get_subgraphs(skip, limit)

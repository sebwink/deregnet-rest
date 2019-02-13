import connexion
import six

from deregnet_rest.models.graph_info import GraphInfo  # noqa: E501
from deregnet_rest.models.inital_graph_info import InitalGraphInfo  # noqa: E501
from deregnet_rest import util


from deregnet_rest.controllers_impl.graphs import GraphController

def delete_graph(graph_id):  # noqa: E501
    """Delete a previously uploaded network

    Delete a previously uplaoded network # noqa: E501

    :param graph_id: ID of the graph to be deleted
    :type graph_id: str

    :rtype: None
    """
    return GraphController.delete_graph(graph_id)


def get_graph(graph_id):  # noqa: E501
    """Retrieve information on a previously uploaded graph

     # noqa: E501

    :param graph_id: ID of graph to return
    :type graph_id: str

    :rtype: GraphInfo
    """
    return GraphController.get_graph(graph_id)


def get_graphs(searchString=None, skip=None, limit=None):  # noqa: E501
    """List available previously uploaded graphs

    Returns a list of all available graphs # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[GraphInfo]
    """
    return GraphController.get_graphs(searchString=None, skip=None, limit=None)


def post_graph(initalGraphInfo=None):  # noqa: E501
    """Allows to initiate GraphML upload

    This Endpoint creates a Metadata-Object for a Graph. It returns the endpoint that is to be called with the  file containing the graph as payload/body in the header-attribute \&quot;location\&quot;  # noqa: E501

    :param initalGraphInfo: The intial Information required for creating a new graph
    :type initalGraphInfo: dict | bytes

    :rtype: GraphInfo
    """
    if connexion.request.is_json:
        initalGraphInfo = InitalGraphInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return GraphController.post_graph(initial_graph_info=initalGraphInfo)


def post_graphml(graph_id, file_to_upload):  # noqa: E501
    """Uploads a GraphML file

    Adds a Graph to the system. The Graph Object with name:graphname must already be created by issuing a POST Request to /graph with repsective payload  # noqa: E501

    :param graph_id: The Name of the graph
    :type graph_id: str
    :param file_to_upload: The file containing the graph
    :type file_to_upload: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return GraphController.post_graphml(graph_id, file_to_upload)

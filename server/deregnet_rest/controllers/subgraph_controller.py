from deregnet_rest import db

def delete_subgraph(subgraph_id):  # noqa: E501
    """Delete a previously found subgraph

    Deletes a subgraph # noqa: E501

    :param subgraph_id: ID of the order that needs to be deleted
    :type subgraph_id: str

    :rtype: None
    """
    return db.subgraphs.delete_subgraph(subgraph_id)


def download_subgraph_as(subgraph_id, filetype):  # noqa: E501
    """Download a subgraph

    With this GET Request you will retrieve a subgraph    # noqa: E501

    :param subgraph_id: The Name of the graph
    :type subgraph_id: str
    :param filetype: File type of file to be downloaded
    :type filetype: str

    :rtype: None
    """
    return db.subgraphs.download_subgraph_as(subgraph_id, filetype)


def get_subgraph(subgraph_id):  # noqa: E501
    """Retrieve the information about a subgraph

    Returns a single pet # noqa: E501

    :param subgraph_id: ID of subgraph about which to retrieve information
    :type subgraph_id: str

    :rtype: SubgraphInfo
    """
    return db.subgraphs.get_subgraph(subgraph_id)


def get_subgraphs(searchString=None, skip=None, limit=None):  # noqa: E501
    """List available found subgraphs

    Returns a single pet # noqa: E501

    :param searchString: pass an optional search string for narrowing the list
    :type searchString: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[SubgraphInfo]
    """
    return db.subgraphs.get_subgraphs(searchString=None, skip=None, limit=None)

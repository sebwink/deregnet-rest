# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from deregnet_rest.models.subgraph_info import SubgraphInfo  # noqa: E501
from deregnet_rest.test import BaseTestCase


class TestSubgraphController(BaseTestCase):
    """SubgraphController integration test stubs"""

    def test_delete_subgraph(self):
        """Test case for delete_subgraph

        Delete a previously found subgraph
        """
        response = self.client.open(
            '/deregnet/subgraph/{subgraph_id}'.format(subgraph_id='subgraph_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_subgraph_as(self):
        """Test case for download_subgraph_as

        Download a subgraph
        """
        response = self.client.open(
            '/deregnet/subgraph/{subgraph_id}/{filetype}'.format(subgraph_id='subgraph_id_example', filetype='filetype_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subgraph(self):
        """Test case for get_subgraph

        Retrieve the information about a subgraph
        """
        response = self.client.open(
            '/deregnet/subgraph/{subgraph_id}'.format(subgraph_id='subgraph_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subgraphs(self):
        """Test case for get_subgraphs

        List available found subgraphs
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/deregnet/subgraphs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

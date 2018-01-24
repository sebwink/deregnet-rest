# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.graph_info import GraphInfo  # noqa: E501
from swagger_server.models.inital_graph_info import InitalGraphInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGraphController(BaseTestCase):
    """GraphController integration test stubs"""

    def test_delete_graph(self):
        """Test case for delete_graph

        Delete a previously uploaded network
        """
        response = self.client.open(
            '/sebwink/deregnet/1.0.0/graph/{graph_id}'.format(graph_id='graph_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_graph(self):
        """Test case for get_graph

        Retrieve information on a previously uploaded graph 
        """
        response = self.client.open(
            '/sebwink/deregnet/1.0.0/graph/{graph_id}'.format(graph_id='graph_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_graphs(self):
        """Test case for get_graphs

        List available previously uploaded graphs
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/sebwink/deregnet/1.0.0/graphs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_graph(self):
        """Test case for post_graph

        Allows to initiate GraphML upload
        """
        initalGraphInfo = InitalGraphInfo()
        response = self.client.open(
            '/sebwink/deregnet/1.0.0/graph',
            method='POST',
            data=json.dumps(initalGraphInfo),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_graphml(self):
        """Test case for post_graphml

        Uploads a GraphML file
        """
        data = dict(file_to_upload=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/sebwink/deregnet/1.0.0/graph/{graph_id}'.format(graph_id='graph_id_example'),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

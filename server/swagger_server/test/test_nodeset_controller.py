# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.node_set import NodeSet  # noqa: E501
from swagger_server.models.node_set_info import NodeSetInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNodesetController(BaseTestCase):
    """NodesetController integration test stubs"""

    def test_delete_nodeset(self):
        """Test case for delete_nodeset

        Delete a previously uploaded node set
        """
        response = self.client.open(
            '/deregnet/nodeset/{nodeset_id}'.format(nodeset_id='nodeset_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_nodeset(self):
        """Test case for get_nodeset

        Retrieve information on a previously uploaded node set
        """
        response = self.client.open(
            '/deregnet/nodeset/{nodeset_id}'.format(nodeset_id='nodeset_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_nodesets(self):
        """Test case for get_nodesets

        List available previously uploaded node sets
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/deregnet/nodesets',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_nodeset(self):
        """Test case for post_nodeset

        Upload a node set for use with DeRegNet algorithms
        """
        body = NodeSet()
        response = self.client.open(
            '/deregnet/nodeset',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

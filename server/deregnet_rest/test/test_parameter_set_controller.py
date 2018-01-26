# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from deregnet_rest.models.parameter_set import ParameterSet  # noqa: E501
from deregnet_rest.models.parameter_set_info import ParameterSetInfo  # noqa: E501
from deregnet_rest.test import BaseTestCase


class TestParameterSetController(BaseTestCase):
    """ParameterSetController integration test stubs"""

    def test_delete_parameter_set(self):
        """Test case for delete_parameter_set

        Delete a previously uploaded parameter collection
        """
        response = self.client.open(
            '/deregnet/parameter_set/{parameter_set_id}'.format(parameter_set_id='parameter_set_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameter_set(self):
        """Test case for get_parameter_set

        Retrieve information on a previously uploaded score
        """
        response = self.client.open(
            '/deregnet/parameter_set/{parameter_set_id}'.format(parameter_set_id='parameter_set_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameter_set_data(self):
        """Test case for get_parameter_set_data

        Retrieve a parameter collection
        """
        response = self.client.open(
            '/deregnet/parameter_set/{parameter_set_id}/data'.format(parameter_set_id='parameter_set_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameter_set_default(self):
        """Test case for get_parameter_set_default

        Retrieve the defaul parameter collection
        """
        response = self.client.open(
            '/deregnet/parameter_set/default',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameter_set_default_data(self):
        """Test case for get_parameter_set_default_data

        Retrieve information on a previously uploaded score
        """
        response = self.client.open(
            '/deregnet/parameter_set/default/data',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_parameter_sets(self):
        """Test case for get_parameter_sets

        List available previously uploaded parameter collections
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/deregnet/parameter_sets',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_parameter_set(self):
        """Test case for post_parameter_set

        Upload a parameters collection for use with DeRegNet algorithms
        """
        body = ParameterSet()
        response = self.client.open(
            '/deregnet/parameter_set',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.run_info import RunInfo  # noqa: E501
from swagger_server.models.run_input import RunInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRunController(BaseTestCase):
    """RunController integration test stubs"""

    def test_delete_run(self):
        """Test case for delete_run

        Cancel an active run, you cannot delete finished runs
        """
        response = self.client.open(
            '/deregnet/run/{run_id}'.format(run_id='run_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_run(self):
        """Test case for get_run

        Retrieve the status of a previously submitted run
        """
        response = self.client.open(
            '/deregnet/run/{run_id}'.format(run_id='run_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_runs(self):
        """Test case for get_runs

        List current and past runs
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/deregnet/runs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_run(self):
        """Test case for post_run

        Run average score DeRegNet algorithm
        """
        body = RunInput()
        response = self.client.open(
            '/deregnet/run',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

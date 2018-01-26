# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from deregnet_rest.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_graph_docs(self):
        """Test case for graph_docs

        Help page on graph endpoint
        """
        response = self.client.open(
            '/deregnet/info/graph',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_help(self):
        """Test case for help

        General help page
        """
        response = self.client.open(
            '/deregnet/info',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index(self):
        """Test case for index

        Index, redirects to /info
        """
        response = self.client.open(
            '/deregnet/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_docs(self):
        """Test case for info_docs

        Help page on info endpoint
        """
        response = self.client.open(
            '/deregnet/info/info',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_nodeset_docs(self):
        """Test case for nodeset_docs

        Help page on nodeset endpoint
        """
        response = self.client.open(
            '/deregnet/info/nodeset',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parameter_set_docs(self):
        """Test case for parameter_set_docs

        Help page on subgraph endpoint
        """
        response = self.client.open(
            '/deregnet/info/parameter_set',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_docs(self):
        """Test case for run_docs

        Help page on run endpoint
        """
        response = self.client.open(
            '/deregnet/info/run',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_score_docs(self):
        """Test case for score_docs

        Help page on score endpoint
        """
        response = self.client.open(
            '/deregnet/info/score',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subgraph_docs(self):
        """Test case for subgraph_docs

        Help page on subgraph endpoint
        """
        response = self.client.open(
            '/deregnet/info/subgraph',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

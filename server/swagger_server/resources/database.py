import os
import subprocess
import getpass

import yaml
import pymongo

from swagger_server.controllers.graphs import Graphs
from swagger_server.controllers.scores import Scores
from swagger_server.controllers.nodesets import NodeSets
from swagger_server.controllers.parameter_sets import ParameterSets
from swagger_server.controllers.runs import Runs
from swagger_server.controllers.subgraphs import Subgraphs


__SERVER_ROOT__ = 'server'


class MongoD:
    def __init__(self, path2conf):
        pass

    @classmethod
    def read_config(cls, path2conf):
        with open(path2conf, 'r') as conf:
            conf = yaml.load(conf)
        if conf is None:
            return {}
        return conf

class Database(pymongo.MongoClient):
    def __init__(self, user, passwd, path2conf=None):
        conf = {}
        if path2conf is None:
            path2conf = ('%s/mongod.conf' % __SERVER_ROOT__)
            conf = MongoD.read_config(path2conf)
        elif path2conf:
            conf = MongoD.read_config(path2conf)
        super().__init__(username=user,
                         password=passwd,
                         authSource='deregnet_rest',
                         **conf)
        self._db = self.deregnet_rest
        self._graphs = Graphs(self._db)
        self._scores = Scores(self._db)
        self._nodesets = NodeSets(self._db)
        self._parameter_sets = ParameterSets(self._db)
        self._runs = Runs(self._db)
        self._subgraphs = Subgraphs(self._db)

    @property
    def graphs(self):
        return self._graphs

    @property
    def scores(self):
        return self._scores

    @property
    def nodesets(self):
        return self._nodesets

    @property
    def parameter_sets(self):
        return self._parameter_sets

    @property
    def runs(self):
        return self._runs

    @property
    def subgraphs(self):
        return self._subgraphs


def get_database(path2conf=None):
    #user = getpass.getpass(prompt='User: ')
    user = 'deregnet_rest_server'
    #passwd = getpass.getpass(prompt='Password: ')
    passwd = 'deregnet'
    return Database(user, passwd, path2conf)

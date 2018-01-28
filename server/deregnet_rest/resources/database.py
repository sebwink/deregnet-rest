import os
import subprocess
import getpass

import yaml
import pymongo

from deregnet_rest.controllers.graphs import Graphs
from deregnet_rest.controllers.scores import Scores
from deregnet_rest.controllers.nodesets import NodeSets
from deregnet_rest.controllers.parameter_sets import ParameterSets
from deregnet_rest.controllers.runs import Runs
from deregnet_rest.controllers.runs import Runner
from deregnet_rest.controllers.subgraphs import Subgraphs


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
        config = {}
        if path2conf is None:
            path2conf = ('%s/mongod.conf' % __SERVER_ROOT__)
            config = MongoD.read_config(path2conf)
        elif path2conf:
            config = MongoD.read_config(path2conf)
        self._config = {
                         **{
                             'username': user,
                             'password': passwd,
                             'authSource': 'deregnet_rest'
                           },
                         **config
                       }
        super().__init__(**self._config)
        self._db = self.deregnet_rest
        self._graphs = Graphs(self._db)
        self._scores = Scores(self._db)
        self._nodesets = NodeSets(self._db)
        self._parameter_sets = ParameterSets(self._db)
        self._runs = Runs(self, {})
        self._runner = Runner(self._config, {})
        self._subgraphs = Subgraphs(self._db)

    def __del__(self):
        self.close()

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

class Server:
    pass


def get_database(path2conf=None):
    #user = getpass.getpass(prompt='User: ')
    user = 'deregnet_rest_server'
    #passwd = getpass.getpass(prompt='Password: ')
    passwd = 'deregnet'
    return Database(user, passwd, path2conf)

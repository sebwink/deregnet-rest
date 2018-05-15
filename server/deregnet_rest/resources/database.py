import getpass

from pymongo import MongoClient

from deregnet_rest.resources.mongodb import get_mongod
from deregnet_rest.resources.redis import get_redis

from deregnet_rest.controllers.graphs import Graphs
from deregnet_rest.controllers.scores import Scores
from deregnet_rest.controllers.nodesets import NodeSets
from deregnet_rest.controllers.parameter_sets import ParameterSets
from deregnet_rest.controllers.runs import Runs
from deregnet_rest.controllers.subgraphs import Subgraphs


class DatabaseServer(MongoClient):
    def __init__(self, user, passwd, mongod, redis):
        self._config = {
                         'username': user,
                         'password': passwd,
                         'authSource': 'deregnet_rest',
                         'host': mongod.host,
                         'port': mongod.port
                       }
        super().__init__(**self._config)
        self._mongod = mongod
        self._redis = redis

        self._graphs = Graphs(self)
        self._scores = Scores(self)
        self._nodesets = NodeSets(self)
        self._parameter_sets = ParameterSets(self)
        self._runs = Runs(self)
        self._subgraphs = Subgraphs(self)


    @property
    def mongod(self):
        return self._mongod

    @property
    def redis(self):
        return self._redis

    @property
    def config(self):
        return self._config

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

    def __del__(self):
        self.close()


def mongo_auth():
    #user = getpass.getpass(prompt='User: ')
    user = 'deregnet_rest_server'
    #passwd = getpass.getpass(prompt='Password: ')
    passwd = 'deregnet'
    return user, passwd


def get_database_server(config):
    user, passwd = mongo_auth()
    mongod = get_mongod(config)
    redis = get_redis(config)
    return DatabaseServer(user, passwd, mongod, redis)

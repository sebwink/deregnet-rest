import os
import subprocess
import yaml

from pymongo import MongoClient

from deregnet_rest.controllers.graphs import Graphs
from deregnet_rest.controllers.scores import Scores
from deregnet_rest.controllers.nodesets import NodeSets
from deregnet_rest.controllers.parameter_sets import ParameterSets
from deregnet_rest.controllers.runs import Runs
from deregnet_rest.controllers.subgraphs import Subgraphs


class MongoD:
    def __init__(self, path2config='server/config/mongod.conf',
                 mongo_bindir='/usr/bin'):
        if not os.path.isfile(path2config):
            raise RuntimeError('Could not find mongod configuration file')
        self._config = self.read_config(path2config)
        mongod_call = [os.path.join(mongo_bindir, 'mongod'), '--config', path2config]
        self._mongod = subprocess.Popen(mongod_call)

    @classmethod
    def read_config(cls, path2conf):
        with open(path2conf, 'r') as conf:
            conf = yaml.load(conf)
        if conf is None:
            return {}
        return conf

    @property
    def config(self):
        return self._config

    @property
    def host(self):
        return self._config.get('host', 'localhost')

    @property
    def port(self):
        return int(self._config.get('port', '27017'))

    def kill(self):
        self._mongod.kill()

    def __del__(self):
        self.kill()


class Database(MongoClient):
    def __init__(self, user, passwd, mongod, redis_server):
        config = {}
        self._config = {
                         'username': user,
                         'password': passwd,
                         'authSource': 'deregnet_rest',
                         'host': mongod.host,
                         'port': mongod.port
                       }
        super().__init__(**self._config)
        self._graphs = Graphs(self)
        self._scores = Scores(self)
        self._nodesets = NodeSets(self)
        self._parameter_sets = ParameterSets(self)
        self._runs = Runs(self, redis_server)
        self._subgraphs = Subgraphs(self)

        self._mongod = mongod
        self._user = user
        self._passwd = passwd

    @property
    def mongod(self):
        return self._mongod

    def __del__(self):
        self.close()

    @property
    def config(self):
        return self._config


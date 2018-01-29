import os
import subprocess
import getpass

import yaml
import pymongo

from deregnet_rest.resources.redis import RedisServer
from deregnet_rest.resources.mongodb import MongoD
from deregnet_rest.resources.mongodb import Database
from deregnet_rest.controllers.runs import Runner



class Server:
    def __init__(self, database, redis_server):
        self._db = database
        self._redis = redis_server
        self._runner = Runner(database.config,
                              self.redis)

    @property
    def db(self):
        return self._db

    @property
    def redis(self):
        return self._redis

    @property
    def graphs(self):
        return self._db._graphs

    @property
    def scores(self):
        return self._db._scores

    @property
    def nodesets(self):
        return self._db._nodesets

    @property
    def parameter_sets(self):
        return self._db._parameter_sets

    @property
    def runs(self):
        return self._db._runs

    @property
    def subgraphs(self):
        return self._db._subgraphs


def init_server(path2conf):
    path2redis_conf = 'server/config/redis.conf'
    redis_bindir = '/opt/redis/4.0.2/bin'
    redis_server = RedisServer(path2redis_conf, redis_bindir)
    return Server(get_database({}, redis_server),
                  redis_server)

def get_database(conf, redis_server):
    #user = getpass.getpass(prompt='User: ')
    user = 'deregnet_rest_server'
    #passwd = getpass.getpass(prompt='Password: ')
    passwd = 'deregnet'
    path2conf = 'server/config/mongod.conf'
    mongod_bindir = '/usr/bin'
    return Database(user,
                    passwd,
                    MongoD(path2conf, mongod_bindir),
                    redis_server)

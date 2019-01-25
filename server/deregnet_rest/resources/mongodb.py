import os
import subprocess
import yaml

class MongoD:
    '''

    '''
    def __init__(self,
                 host=None,
                 port=None,
                 path2config='server/config/mongod.conf',
                 mongod='/usr/bin/env mongod',
                 start_it=True):
        '''

        '''
        self._host = host
        self._port = port
        if not os.path.isfile(path2config):
            raise RuntimeError('Could not find mongod configuration file')
        self._config = self.read_config(path2config)
        self._mongod = None
        if start_it:
            mongod_call = mongod.split(' ') + ['--config', path2config]
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
        if self._host is None:
            return self._config.get('host', 'localhost')
        return self._host

    @property
    def port(self):
        if self._port is None:
            return int(self._config['net'].get('port', 27017))
        return int(self._port)

    def kill_if_this_started_it(self):
        if self._mongod:
            self._mongod.kill()

    def __del__(self):
        self.kill_if_this_started_it()

def get_mongod(config):
    return MongoD(host=config.mongo_host,
                  port=config.mongo_port,
                  path2config=config.mongod_config,
                  mongod=config.mongod,
                  start_it=config.start_mongod)

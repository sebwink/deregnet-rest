import os
import subprocess


class RedisServer:
    def __init__(self, path2config='server/config/redis.conf',
                       redis_server='/usr/bin/env redis-server',
                       start_it=True):
        if not os.path.isfile(path2config):
            raise RuntimeError("No Redis configuration file found")
        self._path2config = path2config
        with open(path2config, 'r') as conff:
            lines = conff.read().split('\n')
            lines = [line for line in lines
                          if line and not line.startswith('#')]
            config = [line.split(' ') for line in lines]
            config = [(p[0], ' '.join(p[1:])) for p in config]
            _config = {k: [] for k,_ in config}
            for k, v in config:
                _config[k].append(v)
            self._config = {k: v if len(v) > 1 else v[0] for k,v in _config.items()}
        self._redis_server = None
        if start_it:
            self._redis_server = self.init_redis(path2config, redis_server)

    @classmethod
    def init_redis(cls, path2config, redis_server):
        redis_call = redis_server.split(' ') + [path2config]
        return subprocess.Popen(redis_call)

    def __del__(self):
        self.kill_if_this_started_it()

    def kill_if_this_started_it(self):
        self._redis_server.kill()

    @property
    def host(self):
        return self._config.get('host', 'localhost')

    @property
    def port(self):
        return self._config['port']

    @property
    def passwd(self):
        return self._config['requirepass']

def get_redis(config):
    return RedisServer(path2config=config.redis_config,
                       redis_server=config.redis,
                       start_it=config.start_redis)

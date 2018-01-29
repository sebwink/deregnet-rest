import os
import subprocess


class RedisServer:
    def __init__(self, path2conf='server/config/redis.conf',
                       redis_bindir='/opt/redis/4.0.2/bin'):
        if not os.path.isfile(path2conf):
            raise RuntimeError("No Redis configuration file found")
        self._path2config = path2conf
        with open(path2conf, 'r') as conff:
            lines = conff.read().split('\n')
            lines = [line for line in lines
                          if line and not line.startswith('#')]
            config = [line.split(' ') for line in lines]
            config = [(p[0], ' '.join(p[1:])) for p in config]
            _config = {k: [] for k,_ in config}
            for k, v in config:
                _config[k].append(v)
            self._config = {k: v if len(v) > 1 else v[0] for k,v in _config.items()}
        self._redis_server = self.init_redis(path2conf, redis_bindir)

    @classmethod
    def init_redis(cls, path2conf, redis_bindir):
        redis_server = os.path.join(redis_bindir, 'redis-server')
        return subprocess.Popen([redis_server, path2conf])

    def __del__(self):
        self.kill()

    def kill(self):
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

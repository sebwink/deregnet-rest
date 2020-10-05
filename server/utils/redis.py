from redis import StrictRedis

from deregnet_rest.config import Config

class RedisSetDict:
    def __init__(self, name):
        self.redis = StrictRedis(
            port=Config.redis_port(),
            host=Config.redis_host(),
        )
        self._name = name

    @property
    def name(self):
        return self._name

    def add(self, key, *items):
        self[key] = set(items)

    def __getitem__(self, key):
        return self.redis.smembers(self.keyprfx+key)

    def __setitem__(self, key, items):
        items = set(items)
        self.redis.sadd(self.keyprfx+key, *items)
        self.redis.sadd(self.keyset_name, key)

    def __delitem__(self, key):
        self.redis.delete(self.keyprfx+key)

    def delete_keys(self, *keys):
        self.redis.delete(*[self.keyprfx+key for key in keys])

    def delete(self):
        self.delete_keys(*self.keys)
        self.redis.delete(self.keyset_name)

    def __len__(self):
        return len(self.keys)

    def len(self, key):
        return self.redis.scard(self.keyprfx+key)

    def contains(self, key, item):
        return self.redis.sismember(self.keyprfx+key, item)

    def is_empty(self, key):
        return self.len(key) == 0

    @property
    def keys(self):
        return self.redis.smembers(self.keyset_name)

    @property
    def keyset_name(self):
        return self._name+'_setdict_keys'

    @property
    def keyprfx(self):
        return self._name+'_'

from hashids import Hashids
import uuid
import datetime
import time
import yaml

__SALT__ = 'This should be constant during the entire lifetime of the database!'
hashids = Hashids(salt=__SALT__)

__SALT_UUID__ = uuid.uuid5(uuid.uuid1(), __SALT__)

class Controller:

    @classmethod
    def timestamp(cls, sep=''):
        return time.strftime(sep.join(['%Y', '%m', '%d', '%H', '%M', '%S']),
                             time.gmtime())

    @classmethod
    def datetime(cls):
        return datetime.datetime.now()

    @classmethod
    def generate_id(cls, seed=None):
        if seed is None:
            seed = int(cls.timestamp())
        else:
            seed = str(seed)
            seed = int.from_bytes(seed.encode('utf-8'), 'little')
        return hashids.encode(seed)

    @classmethod
    def generate_uuid(cls, name):
        return str(uuid.uuid5(__SALT_UUID__, str(name)))

    @classmethod
    def read_yaml(cls, path2yaml):
        with open(path2yaml, 'r') as yamlf:
            return yaml.load(yamlf)

    @classmethod
    def api_call(cls, method):

        def _m(self, *args, **kwargs):
            #try:
            return method(self, *args, **kwargs)
            #except:
            #    return 'Internal Server Error', 500

        return _m

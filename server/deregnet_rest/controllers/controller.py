from hashids import Hashids
import datetime
import time
import yaml

__SALT__ = 'This should be constant during the entire lifetime of the database!'

class Controller:

    @classmethod
    def timestamp(cls, sep=''):
        return time.strftime(sep.join(['%Y', '%m', '%d', '%H', '%M', '%S']),
                             time.gmtime())

    @classmethod
    def datetime(cls):
        return datetime.datetime.now()

    @classmethod
    def generate_id(cls):
        hashids = Hashids(salt=__SALT__)
        ID = hashids.encode(int(cls.timestamp()))
        time.sleep(1)  # TODO: get somehow rid of this...
        return ID

    @classmethod
    def read_yaml(cls, path2yaml):
        with open(path2yaml, 'r') as yamlf:
            return yaml.load(yamlf)

    @classmethod
    def api_call(cls, method):

        def _m(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs)
            except:
                return 'Internal Server Error', 500

        return _m

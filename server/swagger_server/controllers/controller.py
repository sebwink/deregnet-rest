from hashids import Hashids
import time

__SALT__ = 'This should be constant during the entire lifetime of the server!'

class Controller:

    @classmethod
    def timestamp(cls, sep=''):
        return time.strftime(sep.join(['%Y', '%m', '%d', '%H', '%M', '%S']),
                             time.gmtime())

    @classmethod
    def generate_id(cls):
        hashids = Hashids(salt=__SALT__)
        ID = hashids.encode(int(cls.timestamp()))
        time.sleep(1)  # TODO: get somehow rid of this...
        return ID

import pymongo

from deregnet_rest.database.connection import database

class Runs(pymongo.collection.Collection):
    '''

    '''
    def __init__(self, client):
        super().__init__(client.deregnet_rest, name='runs')

runs = Runs(database)

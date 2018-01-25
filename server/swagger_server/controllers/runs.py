import pymongo

class Runs(pymongo.collection.Collection):
    def __init__(self, db):
        super().__init__(db, name='runs')

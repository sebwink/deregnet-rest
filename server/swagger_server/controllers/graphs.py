import pymongo

class Graphs(pymongo.collection.Collection):
    def __init__(self, db):
        super().__init__(db, name='graphs')

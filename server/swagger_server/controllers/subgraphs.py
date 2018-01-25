import pymongo

class Subgraphs(pymongo.collection.Collection):
    def __init__(self, db):
        super().__init__(db, name='subgraphs')

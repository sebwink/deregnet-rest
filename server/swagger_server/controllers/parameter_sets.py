import pymongo

class ParameterSets(pymongo.collection.Collection):
    def __init__(self, db):
        super().__init__(db, name='parameter_sets')

from pymongo import MongoClient
from deregnet_rest.config import Config

database = MongoClient(
    host=Config.mongo_host(),
    port=Config.mongo_port(),
    username=Config.mongo_user(),
    password=Config.mongo_password(),
)

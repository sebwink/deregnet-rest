import gridfs

from deregnet_rest.database.connection import database

files = gridfs.GridFS(database.deregnet_rest)

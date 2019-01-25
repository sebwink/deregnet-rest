import os

from deregnet_rest.resources.server import init_server, Config

config = Config(os.environ.get('DEREGNET_REST_CONFIG'))
server = init_server(config)

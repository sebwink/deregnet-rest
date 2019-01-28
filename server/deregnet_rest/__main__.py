#!/usr/bin/env python3

import os

from deregnet_rest import app
from deregnet_rest.init import config

DEBUG = not bool(os.getenv('DEPLOY', False))

if __name__ == '__main__':
    app.run(host=config.host,
            port=config.port,
            debug=DEBUG,
            server=config.server_backend)

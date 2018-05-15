#!/usr/bin/env python3

from deregnet_rest import app
from deregnet_rest.init import config

if __name__ == '__main__':
    app.run(host=config.host,
            port=config.port,
            debug=config.debug,
            server=config.server_backend)

import os
import multiprocessing as mp

# bind
HOST = '0.0.0.0'
PORT = os.getenv('PORT', 8080)
bind = '{}:{}'.format(HOST, PORT)
# workers
workers = os.getenv('WORKERS', mp.cpu_count() * 2 + 1)
# logging
accesslog = '-'

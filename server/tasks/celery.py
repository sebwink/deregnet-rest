from celery import Celery

from deregnet_rest.config import Config
import deregnet_rest.tasks.find_subgraphs as _find_subgraphs

REDIS_URI = 'redis://{}:{}/1'.format(Config.redis_host(), Config.redis_port())
celery = Celery('main', broker=REDIS_URI)

@celery.task(name='find-subgraph')
def find_subgraphs(run_id):
    _find_subgraphs.task(run_id)

if __name__ == '__main__':
    celery.start()

#!/usr/bin/env python3

import sys

from swagger_client.api.run_api import RunApi

def post_simple_run(run_api, graph_id, score_id, description='test_run'):
    body = {
             'graph_id': graph_id,
             'score_id': score_id,
             'description': description
           }
    response = run_api.post_run(body)           # Post a run via the run API
    sys.stdout.write(response.id)

def show_usage():
    print('Usage: post_run graph_id score_id')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        show_usage()
        sys.exit()
    graph_id = sys.argv[1]
    score_id = sys.argv[2]
    run_api = RunApi()                           # Initialize run API
    post_simple_run(run_api, graph_id, score_id)

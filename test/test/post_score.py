#!/usr/bin/env python3

import sys
import json

from swagger_client.api.score_api import ScoreApi

def post_score(score_api, node_ids, score_values, description):
    body = {
             'node_ids': node_ids,
             'score_values': score_values,
             'description': description
           }
    response = score_api.post_score(body)                  # Post score with call to score API
    sys.stdout.write(response.id)

def show_usage():
    print('Usage: post_score score.json [ score_info.json ]')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        show_usage()
        sys.exit()
    # score data
    with open(sys.argv[1], 'r') as scoref:
        scores = json.load(scoref)
    node_ids, score_values = list(scores.keys()), list(scores.values())
    # description
    description = ''
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as descf:
            description = json.load(descf).get('description', '')
    score_api = ScoreApi()                                 # Initialize score API
    post_score(score_api, node_ids, score_values, description)

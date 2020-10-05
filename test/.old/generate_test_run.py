#!/usr/bin/env python3

import json

graph_id = json.load(open('graph_info.json'))['id']
score_id = json.load(open('score.json'))['id']

run = {
    "description": "test run!",    
    "graph_id": graph_id,
    "score_id": score_id,
    "parameter_set": {
        "num_suboptimal": 1,
        "max_overlap": 0,
        "algorithm": "dta"
    },
}

json.dump(run, open('test_run.json', 'w'))

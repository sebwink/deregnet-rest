#!/usr/bin/env python3

import sys
import json

from swagger_client.api.graph_api import GraphApi

def post_graph(path, graph_api, init_info):
    response = graph_api.post_graph(inital_graph_info=init_info)                  # Graph upload initialization API call
    graph_id = response.id
    graph_api.post_graphml(graph_id=graph_id,                   # Actual graph upload API call
                           file_to_upload=path)
    sys.stdout.write(graph_id)

def show_usage():
    print('Usage: post_graph path2graphml [ path2initInfo ]')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        show_usage()
        sys.exit()
    graph_path = sys.argv[1]
    init_info = {}
    if len(sys.argv) > 2:
        init_info_path = sys.argv[2]
        with open(init_info_path, 'r') as jsonf:
            init_info = json.load(jsonf)
    graph_api = GraphApi()                                      # Initialize Graph API
    post_graph(graph_path, graph_api, init_info)

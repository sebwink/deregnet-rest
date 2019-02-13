import os
import igraph as ig

from deregnet_rest.models.graph_info import GraphInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X
from deregnet_rest.database.collections.graphs import graphs
from deregnet_rest.database.files import files
from deregnet_rest.controllers_impl.base import Controller

def valid_graphmlz(data):
    tmp = '/tmp/{}.validate.graphml.gz'.format(os.getpid())
    with open(tmp, 'wb') as tmpf:
        tmpf.write(data)
    valid = True
    try:
        ig.Graph.Read_GraphMLz(tmp)
    except:
        valid = False
    os.remove(tmp)
    return valid

class GraphController(Controller):
    @classmethod
    @Controller.api_call
    def delete_graph(cls, graph_id):
        '''
        Delete a graph
        '''
        if not graphs.dependent_runs.is_empty(graph_id):
            return 'Invalid graph ID: some runs depend on this graph', 400
        graph_data = graphs.find_one_and_delete(
            filter={
                'id': graph_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=graphs.GRAPH_DATA_PROJ
        )
        if not graph_data:
            return 'Invalid graph ID: no graph with that ID', 400
        file_id = graph_data.get('file_id')
        if file_id:
            files.delete(file_id)
        return 'Graph successfully deleted', 201

    @classmethod
    @Controller.api_call
    def get_graph(cls, graph_id):
        '''

        '''
        graph_info = graphs.find_one(
            filter={
                'id': graph_id,
                'X-Consumer-ID': X.consumer_id(),
            },
            projection=graphs.GRAPH_INFO_PROJ
        )
        if not graph_info:
            return 'Invalid graph ID: no graph with that ID', 400
        return util.deserialize_model(graph_info, GraphInfo)

    @classmethod
    @Controller.api_call
    def get_graphs(cls, searchString, skip, limit):
        '''

        '''
        graph_infos = graphs.find(
            filter={'X-Consumer-ID': X.consumer_id()},
            projection=graphs.GRAPH_INFO_PROJ
        )
        return [
            util.deserialize_model(graph_info, GraphInfo)
            for graph_info in graph_infos
        ]

    @classmethod
    @Controller.api_call
    def post_graph(cls, initial_graph_info):
        '''

        '''
        graph_info = {
            'time_of_upload': cls.timestamp('-'),
            'name': initial_graph_info.name,
            'description': initial_graph_info.description,
            'num_nodes': 0,
            'num_edges': 0,
        }
        graph_data = {
            'file_id': None,
            'node_id_attr': initial_graph_info.node_id_attr,
        }
        x_consumer_id = X.consumer_id()
        _id = graphs.insert_one({
            **graph_info,
            **graph_data,
            'X-Consumer-ID': x_consumer_id,
        }).inserted_id
        graph_id = cls.generate_uuid(_id)
        graphs.update_one(
            filter={
                '_id': _id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': { 'id': graph_id },
            }
        )
        graph_info['id'] = graph_id
        return util.deserialize_model(graph_info, GraphInfo)

    @classmethod
    @Controller.api_call
    def post_graphml(cls, graph_id, file_to_upload):
        '''

        '''
        x_consumer_id = X.consumer_id()
        graph = graphs.find_one(filter={
            'id': graph_id,
            'X-Consumer-ID': x_consumer_id,
        })
        if not graph:
            return 'Invalid graph ID', 400
        if graph['file_id'] is not None:
            return 'A graph for that ID is already uploaded', 409
        content = file_to_upload.read()
        if not valid_graphmlz(content):
            return 'Invalid GraphML file (igraph)', 400
        file_id = files.put(content)
        graph = graphs.ig_from_file_id(file_id)
        graphs.update_one(
            filter={
                'id': graph_id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': {
                    'file_id': file_id,
                    'num_nodes': len(graph.vs),
                    'num_edges': len(graph.es)
                }
            })
        return 'GraphML successfully uploaded', 201

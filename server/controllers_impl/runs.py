from deregnet_rest.models.run_info import RunInfo
from deregnet_rest import util

import deregnet_rest.utils.xdata as X

from deregnet_rest.controllers_impl.base import Controller
from deregnet_rest.database.collections.graphs import graphs
from deregnet_rest.database.collections.scores import scores
from deregnet_rest.database.collections.nodesets import nodesets
from deregnet_rest.database.collections.parameter_sets import parameter_sets
from deregnet_rest.database.collections.runs import runs
from deregnet_rest.tasks.find_subgraphs import celery, find_subgraphs

class RunController(Controller):
    '''

    '''
    @classmethod
    @Controller.api_call
    def delete_run(cls, run_id):
        # TODO. Delete completed runs if they do not reference subgraphs
        deletion = runs.delete_one(filter={
            'id': run_id,
            'started': False,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not deletion:
            return 'Invalid run ID', 400
        celery.control.revoke(run_id)
        return 'Run successfully deleted', 201

    @classmethod
    @Controller.api_call
    def get_run(cls, run_id):
        run_info = runs.find_one(filter={
            'id': run_id,
            'X-Consumer-ID': X.consumer_id(),
        })
        if not run_info:
            return 'Invalid run ID', 400
        return util.deserialize_model(run_info, RunInfo)

    @classmethod
    @Controller.api_call
    def get_runs(cls, skip, limit):
        return [
            util.deserialize_model(run_info, RunInfo)
            for run_info in runs.find(filter={
                'X-Consumer-ID': X.consumer_id()
            }).skip(skip).limit(limit)
        ]

    @classmethod
    @Controller.api_call
    def post_run(cls, body):
        '''

        '''
        run_input = body.to_dict()
        run_input = {k: v for k,v in run_input.items() if v is not None}
        graph_id = run_input['graph_id']
        score_id = run_input.get('score_id')
        receptors_id = run_input.get('receptors_id')
        terminals_id = run_input.get('treminals_id')
        exclude_id = run_input.get('exclude_id')
        include_id = run_input.get('include_id')
        parameter_set_id = run_input.get('parameter_set_id')

        x_consumer_id = X.consumer_id()

        valid, message = cls.validate_run(
            x_consumer_id,
            graph_id,
            score_id,
            receptors_id,
            terminals_id,
            exclude_id,
            include_id,
            parameter_set_id
        )
        if not valid:
            return 'Invalid run, invalid %s encountered, check your run input' % message, 400

        # generate run info and insert into database
        default_parameters = parameter_sets.get_parameter_set_default_data()
        if not parameter_set_id:
            parameter_set = default_parameters
        else:
            parameter_set = parameter_sets.get_parameter_set_as_dict(parameter_set_id)
        parameter_set = {**default_parameters, **parameter_set}
        parameter_set = {**parameter_set, **{k:v for k,v in run_input.get('parameter_set', {}).items() if v is not None}}

        run_input['parameter_set'] = parameter_set

        run_info = {
                     'post_time': cls.timestamp('-'),
                     'started': False,
                     'done': False,
                     'subgraph_ids': [],
                     'run_input': run_input
                   }

        _id = runs.insert_one({
            **run_info,
            'X-Consumer-ID': x_consumer_id,
        }).inserted_id
        run_id = cls.generate_uuid(_id)
        runs.update_one(
            filter={
                '_id': _id,
                'X-Consumer-ID': x_consumer_id,
            },
            update={
                '$set': {
                    'id': run_id,
                },
            }
        )
        # register new run dependencies
        graphs.dependent_runs[graph_id] = run_id
        cls.update_dependent_runs(run_id, score_id, scores)
        cls.update_dependent_runs(run_id, terminals_id, nodesets)
        cls.update_dependent_runs(run_id, receptors_id, nodesets)
        cls.update_dependent_runs(run_id, exclude_id, nodesets)
        cls.update_dependent_runs(run_id, include_id, nodesets)
        cls.update_dependent_runs(run_id, parameter_set_id, parameter_sets)
        run_info['id'] = run_id
        # push run onto the job queue
        find_subgraphs.apply_async((run_id,), task_id=run_id, queue='runs')
        return util.deserialize_model(run_info, RunInfo)

    @classmethod
    def update_dependent_runs(cls, run_id, val, coll):
        if val:
            coll.dependent_runs[val] = run_id

    @classmethod
    def validate_run(cls,
                     x_consumer_id,
                     graph_id,
                     score_id,
                     receptors_id,
                     terminals_id,
                     exclude_id,
                     include_id,
                     parameter_set_id):
        if not graphs.find_one(filter={
            'id': graph_id,
            'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'graph ID %s' % graph_id
        if not scores.find_one(filter={
            'id': score_id,
            'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'score ID %s' % score_id
        if not cls.nodeset_valid(receptors_id, x_consumer_id):
            return False, cls.invalid_nodeset(receptors_id)
        if not cls.nodeset_valid(terminals_id, x_consumer_id):
            return False, cls.invalid_nodeset(terminals_id)
        if not cls.nodeset_valid(exclude_id, x_consumer_id):
            return False, cls.invalid_nodeset(exclude_id)
        if not cls.nodeset_valid(include_id, x_consumer_id):
            return False, cls.invalid_nodeset(include_id)
        if parameter_set_id and not \
           parameter_sets.find_one(filter={
               'id': parameter_set_id,
               'X-Consumer-ID': x_consumer_id,
        }):
            return False, 'parameter set ID %s' % parameter_set_id
        return True, None

    @classmethod
    def nodeset_valid(cls, ID, x_consumer_id):
        if ID and not \
           nodesets.find_one(filter={
               'id': ID,
               'X-Consumer-ID': x_consumer_id,
           }):
            return False
        return True

    @classmethod
    def invalid_nodeset(cls, ID):
        return 'nodeset ID %s' % ID

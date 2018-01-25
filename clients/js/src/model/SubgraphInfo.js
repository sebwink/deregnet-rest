/**
 * DeRegNet REST API
 * DeRegNet REST API 
 *
 * OpenAPI spec version: 0.0.1
 * Contact: deregnet@informatik.uni-tuebingen.de
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */


import ApiClient from '../ApiClient';





/**
* The SubgraphInfo model module.
* @module model/SubgraphInfo
* @version 0.0.1
*/
export default class SubgraphInfo {
    /**
    * Constructs a new <code>SubgraphInfo</code>.
    * @alias module:model/SubgraphInfo
    * @class
    * @param id {String} Subgraph Id
    * @param runId {String} Id of run the subgraph is a result of
    * @param numNodes {Number} Number of nodes in subgraph
    * @param numEdges {Number} Number of edges in subgraph
    * @param optimal {Boolean} Whether the subgraph is optimal, ie not prematurely stopped by a 'gap_cut' or 'time_limit'. This field is independent from the 'optimality_type' field. 
    * @param optimalityType {String} 'optimal': optimal subgraph 'suboptimal:1': first suboptimal subgraph 'suboptimal:2': second suboptimal subgraph, etc. ... 
    * @param root {String} Id of root node, either predefined or found by algorithm 
    * @param score {Number} Score of the subgraph
    */

    constructor(id, runId, numNodes, numEdges, optimal, optimalityType, root, score) {
        

        
        

        this['id'] = id;this['run_id'] = runId;this['num_nodes'] = numNodes;this['num_edges'] = numEdges;this['optimal'] = optimal;this['optimality_type'] = optimalityType;this['root'] = root;this['score'] = score;

        
    }

    /**
    * Constructs a <code>SubgraphInfo</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/SubgraphInfo} obj Optional instance to populate.
    * @return {module:model/SubgraphInfo} The populated <code>SubgraphInfo</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubgraphInfo();

            
            
            

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('run_id')) {
                obj['run_id'] = ApiClient.convertToType(data['run_id'], 'String');
            }
            if (data.hasOwnProperty('num_nodes')) {
                obj['num_nodes'] = ApiClient.convertToType(data['num_nodes'], 'Number');
            }
            if (data.hasOwnProperty('num_edges')) {
                obj['num_edges'] = ApiClient.convertToType(data['num_edges'], 'Number');
            }
            if (data.hasOwnProperty('optimal')) {
                obj['optimal'] = ApiClient.convertToType(data['optimal'], 'Boolean');
            }
            if (data.hasOwnProperty('optimality_type')) {
                obj['optimality_type'] = ApiClient.convertToType(data['optimality_type'], 'String');
            }
            if (data.hasOwnProperty('root')) {
                obj['root'] = ApiClient.convertToType(data['root'], 'String');
            }
            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], 'Number');
            }
        }
        return obj;
    }

    /**
    * Subgraph Id
    * @member {String} id
    */
    id = undefined;
    /**
    * Id of run the subgraph is a result of
    * @member {String} run_id
    */
    run_id = undefined;
    /**
    * Number of nodes in subgraph
    * @member {Number} num_nodes
    */
    num_nodes = undefined;
    /**
    * Number of edges in subgraph
    * @member {Number} num_edges
    */
    num_edges = undefined;
    /**
    * Whether the subgraph is optimal, ie not prematurely stopped by a 'gap_cut' or 'time_limit'. This field is independent from the 'optimality_type' field. 
    * @member {Boolean} optimal
    */
    optimal = undefined;
    /**
    * 'optimal': optimal subgraph 'suboptimal:1': first suboptimal subgraph 'suboptimal:2': second suboptimal subgraph, etc. ... 
    * @member {String} optimality_type
    */
    optimality_type = undefined;
    /**
    * Id of root node, either predefined or found by algorithm 
    * @member {String} root
    */
    root = undefined;
    /**
    * Score of the subgraph
    * @member {Number} score
    */
    score = undefined;








}



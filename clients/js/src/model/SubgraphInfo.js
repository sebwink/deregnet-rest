/**
 * DeRegNet REST API
 * DeRegNet REST API 
 *
 * OpenAPI spec version: 1.0.0
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
* @version 1.0.0
*/
export default class SubgraphInfo {
    /**
    * Constructs a new <code>SubgraphInfo</code>.
    * @alias module:model/SubgraphInfo
    * @class
    */

    constructor() {
        

        
        

        

        
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
            if (data.hasOwnProperty('num_nodes')) {
                obj['num_nodes'] = ApiClient.convertToType(data['num_nodes'], 'Number');
            }
            if (data.hasOwnProperty('num_edges')) {
                obj['num_edges'] = ApiClient.convertToType(data['num_edges'], 'Number');
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
    * Number of nodes in subgraph
    * @member {Number} num_nodes
    */
    num_nodes = undefined;
    /**
    * Number of edges in subgraph
    * @member {Number} num_edges
    */
    num_edges = undefined;








}


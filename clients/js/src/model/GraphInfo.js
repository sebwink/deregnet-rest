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
* The GraphInfo model module.
* @module model/GraphInfo
* @version 1.0.0
*/
export default class GraphInfo {
    /**
    * Constructs a new <code>GraphInfo</code>.
    * @alias module:model/GraphInfo
    * @class
    * @param numNodes {Number} Number of nodes in the graph
    * @param numEdges {Number} Number of edges in the graph
    * @param id {String} Id of the graph
    * @param timeOfUpload {String} Time of upload
    */

    constructor(numNodes, numEdges, id, timeOfUpload) {
        

        
        

        this['num_nodes'] = numNodes;this['num_edges'] = numEdges;this['id'] = id;this['time_of_upload'] = timeOfUpload;

        
    }

    /**
    * Constructs a <code>GraphInfo</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/GraphInfo} obj Optional instance to populate.
    * @return {module:model/GraphInfo} The populated <code>GraphInfo</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GraphInfo();

            
            
            

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('num_nodes')) {
                obj['num_nodes'] = ApiClient.convertToType(data['num_nodes'], 'Number');
            }
            if (data.hasOwnProperty('num_edges')) {
                obj['num_edges'] = ApiClient.convertToType(data['num_edges'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('time_of_upload')) {
                obj['time_of_upload'] = ApiClient.convertToType(data['time_of_upload'], 'String');
            }
        }
        return obj;
    }

    /**
    * Name of the graph
    * @member {String} name
    */
    name = undefined;
    /**
    * Description of the graph
    * @member {String} description
    */
    description = undefined;
    /**
    * Number of nodes in the graph
    * @member {Number} num_nodes
    */
    num_nodes = undefined;
    /**
    * Number of edges in the graph
    * @member {Number} num_edges
    */
    num_edges = undefined;
    /**
    * Id of the graph
    * @member {String} id
    */
    id = undefined;
    /**
    * Time of upload
    * @member {String} time_of_upload
    */
    time_of_upload = undefined;








}



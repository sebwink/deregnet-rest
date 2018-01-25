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


import ApiClient from "../ApiClient";
import GraphInfo from '../model/GraphInfo';
import InitalGraphInfo from '../model/InitalGraphInfo';

/**
* Graph service.
* @module api/GraphApi
* @version 0.0.1
*/
export default class GraphApi {

    /**
    * Constructs a new GraphApi. 
    * @alias module:api/GraphApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteGraph operation.
     * @callback module:api/GraphApi~deleteGraphCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a previously uploaded network
     * Delete a previously uplaoded network
     * @param {String} graphId ID of the graph to be deleted
     * @param {module:api/GraphApi~deleteGraphCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteGraph(graphId, callback) {
      let postBody = null;

      // verify the required parameter 'graphId' is set
      if (graphId === undefined || graphId === null) {
        throw new Error("Missing the required parameter 'graphId' when calling deleteGraph");
      }


      let pathParams = {
        'graph_id': graphId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;

      return this.apiClient.callApi(
        '/graph/{graph_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getGraph operation.
     * @callback module:api/GraphApi~getGraphCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GraphInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve information on a previously uploaded graph 
     * @param {String} graphId ID of graph to return
     * @param {module:api/GraphApi~getGraphCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GraphInfo}
     */
    getGraph(graphId, callback) {
      let postBody = null;

      // verify the required parameter 'graphId' is set
      if (graphId === undefined || graphId === null) {
        throw new Error("Missing the required parameter 'graphId' when calling getGraph");
      }


      let pathParams = {
        'graph_id': graphId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GraphInfo;

      return this.apiClient.callApi(
        '/graph/{graph_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getGraphs operation.
     * @callback module:api/GraphApi~getGraphsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GraphInfo>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available previously uploaded graphs
     * Returns a list of all available graphs
     * @param {Object} opts Optional parameters
     * @param {String} opts.searchString pass an optional search string for narrowing the list
     * @param {Number} opts.skip number of records to skip for pagination
     * @param {Number} opts.limit maximum number of records to return
     * @param {module:api/GraphApi~getGraphsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GraphInfo>}
     */
    getGraphs(opts, callback) {
      opts = opts || {};
      let postBody = null;


      let pathParams = {
      };
      let queryParams = {
        'searchString': opts['searchString'],
        'skip': opts['skip'],
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GraphInfo];

      return this.apiClient.callApi(
        '/graphs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the postGraph operation.
     * @callback module:api/GraphApi~postGraphCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GraphInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Allows to initiate GraphML upload
     * This Endpoint creates a Metadata-Object for a Graph. It returns the endpoint that is to be called with the  file containing the graph as payload/body in the header-attribute \&quot;location\&quot; 
     * @param {Object} opts Optional parameters
     * @param {module:model/InitalGraphInfo} opts.initalGraphInfo The intial Information required for creating a new graph
     * @param {module:api/GraphApi~postGraphCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GraphInfo}
     */
    postGraph(opts, callback) {
      opts = opts || {};
      let postBody = opts['initalGraphInfo'];


      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GraphInfo;

      return this.apiClient.callApi(
        '/graph', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the postGraphml operation.
     * @callback module:api/GraphApi~postGraphmlCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Uploads a GraphML file
     * Adds a Graph to the system. The Graph Object with name:graphname must already be created by issuing a POST Request to /graph with repsective payload 
     * @param {String} graphId The Name of the graph
     * @param {File} fileToUpload The file containing the graph
     * @param {module:api/GraphApi~postGraphmlCallback} callback The callback function, accepting three arguments: error, data, response
     */
    postGraphml(graphId, fileToUpload, callback) {
      let postBody = null;

      // verify the required parameter 'graphId' is set
      if (graphId === undefined || graphId === null) {
        throw new Error("Missing the required parameter 'graphId' when calling postGraphml");
      }

      // verify the required parameter 'fileToUpload' is set
      if (fileToUpload === undefined || fileToUpload === null) {
        throw new Error("Missing the required parameter 'fileToUpload' when calling postGraphml");
      }


      let pathParams = {
        'graph_id': graphId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'file_to_upload': fileToUpload
      };

      let authNames = [];
      let contentTypes = ['multipart/form-data'];
      let accepts = [];
      let returnType = null;

      return this.apiClient.callApi(
        '/graph/{graph_id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }


}

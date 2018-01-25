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
import ParameterSet from '../model/ParameterSet';
import ParameterSetInfo from '../model/ParameterSetInfo';

/**
* ParameterSet service.
* @module api/ParameterSetApi
* @version 0.0.1
*/
export default class ParameterSetApi {

    /**
    * Constructs a new ParameterSetApi. 
    * @alias module:api/ParameterSetApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteParameterSet operation.
     * @callback module:api/ParameterSetApi~deleteParameterSetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a previously uploaded parameter collection
     * Deletes a parameter collection
     * @param {String} parameterSetId ID of the parameter collection to be deleted
     * @param {module:api/ParameterSetApi~deleteParameterSetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteParameterSet(parameterSetId, callback) {
      let postBody = null;

      // verify the required parameter 'parameterSetId' is set
      if (parameterSetId === undefined || parameterSetId === null) {
        throw new Error("Missing the required parameter 'parameterSetId' when calling deleteParameterSet");
      }


      let pathParams = {
        'parameter_set_id': parameterSetId
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
        '/parameter_set/{parameter_set_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getParameterSet operation.
     * @callback module:api/ParameterSetApi~getParameterSetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ParameterSetInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve information on a previously uploaded score
     * @param {String} parameterSetId ID of parameter collection to retrieve information about
     * @param {module:api/ParameterSetApi~getParameterSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ParameterSetInfo}
     */
    getParameterSet(parameterSetId, callback) {
      let postBody = null;

      // verify the required parameter 'parameterSetId' is set
      if (parameterSetId === undefined || parameterSetId === null) {
        throw new Error("Missing the required parameter 'parameterSetId' when calling getParameterSet");
      }


      let pathParams = {
        'parameter_set_id': parameterSetId
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
      let returnType = ParameterSetInfo;

      return this.apiClient.callApi(
        '/parameter_set/{parameter_set_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getParameterSetData operation.
     * @callback module:api/ParameterSetApi~getParameterSetDataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ParameterSet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a parameter collection
     * Returns a parameter collection
     * @param {String} parameterSetId ID of the parameter collection to return
     * @param {module:api/ParameterSetApi~getParameterSetDataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ParameterSet}
     */
    getParameterSetData(parameterSetId, callback) {
      let postBody = null;

      // verify the required parameter 'parameterSetId' is set
      if (parameterSetId === undefined || parameterSetId === null) {
        throw new Error("Missing the required parameter 'parameterSetId' when calling getParameterSetData");
      }


      let pathParams = {
        'parameter_set_id': parameterSetId
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
      let returnType = ParameterSet;

      return this.apiClient.callApi(
        '/parameter_set/{parameter_set_id}/data', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getParameterSetDefault operation.
     * @callback module:api/ParameterSetApi~getParameterSetDefaultCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ParameterSetInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the defaul parameter collection
     * Returns the default parameter collection
     * @param {module:api/ParameterSetApi~getParameterSetDefaultCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ParameterSetInfo}
     */
    getParameterSetDefault(callback) {
      let postBody = null;


      let pathParams = {
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
      let returnType = ParameterSetInfo;

      return this.apiClient.callApi(
        '/parameter_set/default', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getParameterSetDefaultData operation.
     * @callback module:api/ParameterSetApi~getParameterSetDefaultDataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ParameterSet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve information on a previously uploaded score
     * @param {module:api/ParameterSetApi~getParameterSetDefaultDataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ParameterSet}
     */
    getParameterSetDefaultData(callback) {
      let postBody = null;


      let pathParams = {
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
      let returnType = ParameterSet;

      return this.apiClient.callApi(
        '/parameter_set/default/data', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getParameterSets operation.
     * @callback module:api/ParameterSetApi~getParameterSetsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ParameterSetInfo>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available previously uploaded parameter collections
     * Returns a list with information about availabel parameter collections
     * @param {Object} opts Optional parameters
     * @param {String} opts.searchString pass an optional search string for narrowing the list
     * @param {Number} opts.skip number of records to skip for pagination
     * @param {Number} opts.limit maximum number of records to return
     * @param {module:api/ParameterSetApi~getParameterSetsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ParameterSetInfo>}
     */
    getParameterSets(opts, callback) {
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
      let returnType = [ParameterSetInfo];

      return this.apiClient.callApi(
        '/parameter_sets', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the postParameterSet operation.
     * @callback module:api/ParameterSetApi~postParameterSetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ParameterSetInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload a parameters collection for use with DeRegNet algorithms
     * @param {module:model/ParameterSet} body Parameters to be uploaded for later use with a DeRegNet algorithm
     * @param {module:api/ParameterSetApi~postParameterSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ParameterSetInfo}
     */
    postParameterSet(body, callback) {
      let postBody = body;

      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling postParameterSet");
      }


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
      let returnType = ParameterSetInfo;

      return this.apiClient.callApi(
        '/parameter_set', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }


}

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


import ApiClient from "../ApiClient";

/**
* Info service.
* @module api/InfoApi
* @version 1.0.0
*/
export default class InfoApi {

    /**
    * Constructs a new InfoApi. 
    * @alias module:api/InfoApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the graphDocs operation.
     * @callback module:api/InfoApi~graphDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on graph endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~graphDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    graphDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/graph', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the help operation.
     * @callback module:api/InfoApi~helpCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * General help page
     * Returns a single pet
     * @param {module:api/InfoApi~helpCallback} callback The callback function, accepting three arguments: error, data, response
     */
    help(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the index operation.
     * @callback module:api/InfoApi~indexCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Index, redirects to /info
     * Returns a single pet
     * @param {module:api/InfoApi~indexCallback} callback The callback function, accepting three arguments: error, data, response
     */
    index(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the infoDocs operation.
     * @callback module:api/InfoApi~infoDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on info endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~infoDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    infoDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/info', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the nodesetDocs operation.
     * @callback module:api/InfoApi~nodesetDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on nodeset endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~nodesetDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    nodesetDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/nodeset', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the parameterSetDocs operation.
     * @callback module:api/InfoApi~parameterSetDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on subgraph endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~parameterSetDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    parameterSetDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/parameter_set', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the runDocs operation.
     * @callback module:api/InfoApi~runDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on run endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~runDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    runDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/run', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the scoreDocs operation.
     * @callback module:api/InfoApi~scoreDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on score endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~scoreDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    scoreDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/score', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the subgraphDocs operation.
     * @callback module:api/InfoApi~subgraphDocsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Help page on subgraph endpoint
     * Returns a single pet
     * @param {module:api/InfoApi~subgraphDocsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    subgraphDocs(callback) {
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
      let accepts = ['text/html'];
      let returnType = null;

      return this.apiClient.callApi(
        '/info/subgraph', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }


}

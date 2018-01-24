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


import ApiClient from './ApiClient';
import GraphInfo from './model/GraphInfo';
import InitalGraphInfo from './model/InitalGraphInfo';
import NodeSet from './model/NodeSet';
import NodeSetInfo from './model/NodeSetInfo';
import ParameterSet from './model/ParameterSet';
import ParameterSetInfo from './model/ParameterSetInfo';
import RunInfo from './model/RunInfo';
import RunInput from './model/RunInput';
import Score from './model/Score';
import ScoreInfo from './model/ScoreInfo';
import SubgraphInfo from './model/SubgraphInfo';
import GraphApi from './api/GraphApi';
import InfoApi from './api/InfoApi';
import NodesetApi from './api/NodesetApi';
import ParameterSetApi from './api/ParameterSetApi';
import RunApi from './api/RunApi';
import ScoreApi from './api/ScoreApi';
import SubgraphApi from './api/SubgraphApi';


/**
* DeRegNet_REST_API.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var DeRegNetRestApi = require('index'); // See note below*.
* var xxxSvc = new DeRegNetRestApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new DeRegNetRestApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new DeRegNetRestApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new DeRegNetRestApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The GraphInfo model constructor.
     * @property {module:model/GraphInfo}
     */
    GraphInfo,

    /**
     * The InitalGraphInfo model constructor.
     * @property {module:model/InitalGraphInfo}
     */
    InitalGraphInfo,

    /**
     * The NodeSet model constructor.
     * @property {module:model/NodeSet}
     */
    NodeSet,

    /**
     * The NodeSetInfo model constructor.
     * @property {module:model/NodeSetInfo}
     */
    NodeSetInfo,

    /**
     * The ParameterSet model constructor.
     * @property {module:model/ParameterSet}
     */
    ParameterSet,

    /**
     * The ParameterSetInfo model constructor.
     * @property {module:model/ParameterSetInfo}
     */
    ParameterSetInfo,

    /**
     * The RunInfo model constructor.
     * @property {module:model/RunInfo}
     */
    RunInfo,

    /**
     * The RunInput model constructor.
     * @property {module:model/RunInput}
     */
    RunInput,

    /**
     * The Score model constructor.
     * @property {module:model/Score}
     */
    Score,

    /**
     * The ScoreInfo model constructor.
     * @property {module:model/ScoreInfo}
     */
    ScoreInfo,

    /**
     * The SubgraphInfo model constructor.
     * @property {module:model/SubgraphInfo}
     */
    SubgraphInfo,

    /**
    * The GraphApi service constructor.
    * @property {module:api/GraphApi}
    */
    GraphApi,

    /**
    * The InfoApi service constructor.
    * @property {module:api/InfoApi}
    */
    InfoApi,

    /**
    * The NodesetApi service constructor.
    * @property {module:api/NodesetApi}
    */
    NodesetApi,

    /**
    * The ParameterSetApi service constructor.
    * @property {module:api/ParameterSetApi}
    */
    ParameterSetApi,

    /**
    * The RunApi service constructor.
    * @property {module:api/RunApi}
    */
    RunApi,

    /**
    * The ScoreApi service constructor.
    * @property {module:api/ScoreApi}
    */
    ScoreApi,

    /**
    * The SubgraphApi service constructor.
    * @property {module:api/SubgraphApi}
    */
    SubgraphApi
};

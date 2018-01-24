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
* The ParameterSet model module.
* @module model/ParameterSet
* @version 1.0.0
*/
export default class ParameterSet {
    /**
    * Constructs a new <code>ParameterSet</code>.
    * @alias module:model/ParameterSet
    * @class
    */

    constructor() {
        

        
        

        

        
    }

    /**
    * Constructs a <code>ParameterSet</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/ParameterSet} obj Optional instance to populate.
    * @return {module:model/ParameterSet} The populated <code>ParameterSet</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ParameterSet();

            
            
            

            if (data.hasOwnProperty('default_score')) {
                obj['default_score'] = ApiClient.convertToType(data['default_score'], 'Number');
            }
            if (data.hasOwnProperty('flip_orientation')) {
                obj['flip_orientation'] = ApiClient.convertToType(data['flip_orientation'], 'Boolean');
            }
            if (data.hasOwnProperty('num_suboptimal')) {
                obj['num_suboptimal'] = ApiClient.convertToType(data['num_suboptimal'], 'Number');
            }
            if (data.hasOwnProperty('max_overlap')) {
                obj['max_overlap'] = ApiClient.convertToType(data['max_overlap'], 'Number');
            }
            if (data.hasOwnProperty('gap_cut')) {
                obj['gap_cut'] = ApiClient.convertToType(data['gap_cut'], 'Number');
            }
            if (data.hasOwnProperty('min_size')) {
                obj['min_size'] = ApiClient.convertToType(data['min_size'], 'Number');
            }
            if (data.hasOwnProperty('max_size')) {
                obj['max_size'] = ApiClient.convertToType(data['max_size'], 'Number');
            }
            if (data.hasOwnProperty('abs_values')) {
                obj['abs_values'] = ApiClient.convertToType(data['abs_values'], 'Boolean');
            }
            if (data.hasOwnProperty('model_sense')) {
                obj['model_sense'] = ApiClient.convertToType(data['model_sense'], 'String');
            }
            if (data.hasOwnProperty('algorithm')) {
                obj['algorithm'] = ApiClient.convertToType(data['algorithm'], 'String');
            }
            if (data.hasOwnProperty('time_limit')) {
                obj['time_limit'] = ApiClient.convertToType(data['time_limit'], 'Number');
            }
        }
        return obj;
    }

    /**
    * Score of graph node when not defined in node score
    * @member {Number} default_score
    */
    default_score = undefined;
    /**
    * Find a deregulated subgraph upstream of a terminal (root)
    * @member {Boolean} flip_orientation
    */
    flip_orientation = undefined;
    /**
    * Number of suboptimal subgraphs to find
    * @member {Number} num_suboptimal
    */
    num_suboptimal = undefined;
    /**
    * Maximal overlap (node percentage) of two subgraphs
    * @member {Number} max_overlap
    */
    max_overlap = undefined;
    /**
    * Gap cut to stop optimization prematurely when the best solution found so far is within <Gap cut> * 100 percent of the best possible solution. Best found solutions are accessible as subgraphs. 
    * @member {Number} gap_cut
    */
    gap_cut = undefined;
    /**
    * Minimal size of a subgraph (number of nodes)
    * @member {Number} min_size
    */
    min_size = undefined;
    /**
    * Maximal size of a subgraph (number of nodes)
    * @member {Number} max_size
    */
    max_size = undefined;
    /**
    * Whether to take the absolute values of the provided scores as actual scores in the computation 
    * @member {Boolean} abs_values
    */
    abs_values = undefined;
    /**
    * 'max' means maximization, 'min' means minimization.  Suitability depends on the semantics of the node scores 
    * @member {module:model/ParameterSet.ModelSenseEnum} model_sense
    */
    model_sense = undefined;
    /**
    * Which algorithm to use: gcc: Generalized Charnes-Cooper transform (recommended) dta: Dinkelbach-type algorithm ovt: Objective-Variable transform 
    * @member {module:model/ParameterSet.AlgorithmEnum} algorithm
    */
    algorithm = undefined;
    /**
    * Time limit in second. A run is aborted if the limit is reached, in case there were feasible solutions found you can access those as subgraphs though 
    * @member {Number} time_limit
    */
    time_limit = undefined;






    /**
    * Allowed values for the <code>model_sense</code> property.
    * @enum {String}
    * @readonly
    */
    static ModelSenseEnum = {
    
        /**
         * value: "max"
         * @const
         */
        "max": "max",
    
        /**
         * value: "min"
         * @const
         */
        "min": "min"    
    };

    /**
    * Allowed values for the <code>algorithm</code> property.
    * @enum {String}
    * @readonly
    */
    static AlgorithmEnum = {
    
        /**
         * value: "dta"
         * @const
         */
        "dta": "dta",
    
        /**
         * value: "gcc"
         * @const
         */
        "gcc": "gcc",
    
        /**
         * value: "ovt"
         * @const
         */
        "ovt": "ovt"    
    };



}


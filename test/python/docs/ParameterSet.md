# ParameterSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_score** | **float** | Score of graph node when not defined in node score | [optional] 
**flip_orientation** | **bool** | Find a deregulated subgraph upstream of a terminal (root) | [optional] 
**num_suboptimal** | **int** | Number of suboptimal subgraphs to find | [optional] 
**max_overlap** | **float** | Maximal overlap (node percentage) of two subgraphs | [optional] 
**gap_cut** | **float** | Gap cut to stop optimization prematurely when the best solution found so far is within &lt;Gap cut&gt; * 100 percent of the best possible solution. Best found solutions are accessible as subgraphs.  | [optional] 
**min_size** | **int** | Minimal size of a subgraph (number of nodes) | [optional] 
**max_size** | **int** | Maximal size of a subgraph (number of nodes) | [optional] 
**abs_values** | **bool** | Whether to take the absolute values of the provided scores as actual scores in the computation  | [optional] 
**model_sense** | **str** | &#39;max&#39; means maximization, &#39;min&#39; means minimization.  Suitability depends on the semantics of the node scores  | [optional] 
**algorithm** | **str** | Which algorithm to use: gcc: Generalized Charnes-Cooper transform (recommended) dta: Dinkelbach-type algorithm ovt: Objective-Variable transform  | [optional] 
**time_limit** | **int** | Time limit in second. A run is aborted if the limit is reached, in case there were feasible solutions found you can access those as subgraphs though  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



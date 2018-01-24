# DeRegNetRestApi.ParameterSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultScore** | **Number** | Score of graph node when not defined in node score | [optional] 
**flipOrientation** | **Boolean** | Find a deregulated subgraph upstream of a terminal (root) | [optional] 
**numSuboptimal** | **Number** | Number of suboptimal subgraphs to find | [optional] 
**maxOverlap** | **Number** | Maximal overlap (node percentage) of two subgraphs | [optional] 
**gapCut** | **Number** | Gap cut to stop optimization prematurely when the best solution found so far is within &lt;Gap cut&gt; * 100 percent of the best possible solution. Best found solutions are accessible as subgraphs.  | [optional] 
**minSize** | **Number** | Minimal size of a subgraph (number of nodes) | [optional] 
**maxSize** | **Number** | Maximal size of a subgraph (number of nodes) | [optional] 
**absValues** | **Boolean** | Whether to take the absolute values of the provided scores as actual scores in the computation  | [optional] 
**modelSense** | **String** | &#39;max&#39; means maximization, &#39;min&#39; means minimization.  Suitability depends on the semantics of the node scores  | [optional] 
**algorithm** | **String** | Which algorithm to use: gcc: Generalized Charnes-Cooper transform (recommended) dta: Dinkelbach-type algorithm ovt: Objective-Variable transform  | [optional] 
**timeLimit** | **Number** | Time limit in second. A run is aborted if the limit is reached, in case there were feasible solutions found you can access those as subgraphs though  | [optional] 


<a name="ModelSenseEnum"></a>
## Enum: ModelSenseEnum


* `max` (value: `"max"`)

* `min` (value: `"min"`)




<a name="AlgorithmEnum"></a>
## Enum: AlgorithmEnum


* `dta` (value: `"dta"`)

* `gcc` (value: `"gcc"`)

* `ovt` (value: `"ovt"`)





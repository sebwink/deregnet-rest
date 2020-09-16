# ParameterSet
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultUnderscorescore** | [**BigDecimal**](number.md) | Score of graph node when not defined in node score | [optional] [default to null]
**flipUnderscoreorientation** | [**Boolean**](boolean.md) | Find a deregulated subgraph upstream of a terminal (root) | [optional] [default to null]
**numUnderscoresuboptimal** | [**Integer**](integer.md) | Number of suboptimal subgraphs to find | [optional] [default to null]
**maxUnderscoreoverlap** | [**BigDecimal**](number.md) | Maximal overlap (node percentage) of two subgraphs | [optional] [default to null]
**gapUnderscorecut** | [**BigDecimal**](number.md) | Gap cut to stop optimization prematurely when the best solution found so far is within &lt;Gap cut&gt; * 100 percent of the best possible solution. Best found solutions are accessible as subgraphs.  | [optional] [default to null]
**minUnderscoresize** | [**Integer**](integer.md) | Minimal size of a subgraph (number of nodes) | [optional] [default to null]
**maxUnderscoresize** | [**Integer**](integer.md) | Maximal size of a subgraph (number of nodes) | [optional] [default to null]
**absUnderscorevalues** | [**Boolean**](boolean.md) | Whether to take the absolute values of the provided scores as actual scores in the computation  | [optional] [default to null]
**modelUnderscoresense** | [**String**](string.md) | &#39;max&#39; means maximization, &#39;min&#39; means minimization.  Suitability depends on the semantics of the node scores  | [optional] [default to null]
**algorithm** | [**String**](string.md) | Which algorithm to use: gcc: Generalized Charnes-Cooper transform (recommended) dta: Dinkelbach-type algorithm ovt: Objective-Variable transform  | [optional] [default to null]
**timeUnderscorelimit** | [**Integer**](integer.md) | Time limit in second. A run is aborted if the limit is reached, in case there were feasible solutions found you can access those as subgraphs though  | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


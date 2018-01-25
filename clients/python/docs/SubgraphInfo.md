# SubgraphInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subgraph Id | 
**run_id** | **str** | Id of run the subgraph is a result of | 
**num_nodes** | **int** | Number of nodes in subgraph | 
**num_edges** | **int** | Number of edges in subgraph | 
**optimal** | **bool** | Whether the subgraph is optimal, ie not prematurely stopped by a &#39;gap_cut&#39; or &#39;time_limit&#39;. This field is independent from the &#39;optimality_type&#39; field.  | 
**optimality_type** | **str** | &#39;optimal&#39;: optimal subgraph &#39;suboptimal:1&#39;: first suboptimal subgraph &#39;suboptimal:2&#39;: second suboptimal subgraph, etc. ...  | 
**root** | **str** | Id of root node, either predefined or found by algorithm  | 
**score** | **float** | Score of the subgraph | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



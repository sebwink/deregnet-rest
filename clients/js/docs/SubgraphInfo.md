# DeRegNetRestApi.SubgraphInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Subgraph Id | 
**runId** | **String** | Id of run the subgraph is a result of | 
**numNodes** | **Number** | Number of nodes in subgraph | 
**numEdges** | **Number** | Number of edges in subgraph | 
**optimal** | **Boolean** | Whether the subgraph is optimal, ie not prematurely stopped by a &#39;gap_cut&#39; or &#39;time_limit&#39;. This field is independent from the &#39;optimality_type&#39; field.  | 
**optimalityType** | **String** | &#39;optimal&#39;: optimal subgraph &#39;suboptimal:1&#39;: first suboptimal subgraph &#39;suboptimal:2&#39;: second suboptimal subgraph, etc. ...  | 
**root** | **String** | Id of root node, either predefined or found by algorithm  | 
**score** | **Number** | Score of the subgraph | 



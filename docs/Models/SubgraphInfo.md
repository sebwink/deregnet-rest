# SubgraphInfo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**String**](string.md) | Subgraph Id | [default to null]
**runUnderscoreid** | [**String**](string.md) | Id of run the subgraph is a result of | [default to null]
**numUnderscorenodes** | [**Integer**](integer.md) | Number of nodes in subgraph | [default to null]
**numUnderscoreedges** | [**Integer**](integer.md) | Number of edges in subgraph | [default to null]
**optimal** | [**Boolean**](boolean.md) | Whether the subgraph is optimal, ie not prematurely stopped by a &#39;gap_cut&#39; or &#39;time_limit&#39;. This field is independent from the &#39;optimality_type&#39; field.  | [default to null]
**optimalityUnderscoretype** | [**String**](string.md) | &#39;optimal&#39;: optimal subgraph &#39;suboptimal:1&#39;: first suboptimal subgraph &#39;suboptimal:2&#39;: second suboptimal subgraph, etc. ...  | [default to null]
**root** | [**String**](string.md) | Id of root node, either predefined or found by algorithm  | [default to null]
**score** | [**BigDecimal**](number.md) | Score of the subgraph | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


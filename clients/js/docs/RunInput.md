# DeRegNetRestApi.RunInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of run | [optional] 
**parameterSetId** | **String** | Id of a parameter set to run the algorithm with | [optional] 
**parameterSet** | [**ParameterSet**](ParameterSet.md) |  | [optional] 
**graphId** | **String** | Id of graph underlying the run | 
**scoreId** | **String** | Id of node score used in the run | [optional] 
**receptorsId** | **String** | Id of a node set acting as receptors in the run | [optional] 
**terminalsId** | **String** | Id of a node set acting as terminals in the run | [optional] 
**excludeId** | **String** | Id of a node set of nodes to be excluded from the subgraphs  | [optional] 
**includeId** | **String** | Id of a node set of nodes to be included in the subgraphs  | [optional] 
**root** | **String** | Node id of a fixed root node | [optional] 



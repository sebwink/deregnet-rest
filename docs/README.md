# Documentation for DeRegNet REST API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://api.dereg.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GraphApi* | [**deleteGraph**](Apis/GraphApi.md#deletegraph) | **DELETE** /graph/{graph_id} | Delete a previously uploaded network
*GraphApi* | [**getGraph**](Apis/GraphApi.md#getgraph) | **GET** /graph/{graph_id} | Retrieve information on a previously uploaded graph 
*GraphApi* | [**getGraphs**](Apis/GraphApi.md#getgraphs) | **GET** /graphs | List available previously uploaded graphs
*GraphApi* | [**postGraph**](Apis/GraphApi.md#postgraph) | **POST** /graph | Allows to initiate GraphML upload
*GraphApi* | [**postGraphml**](Apis/GraphApi.md#postgraphml) | **POST** /graph/{graph_id} | Uploads a GraphML file
*NodesetApi* | [**deleteNodeset**](Apis/NodesetApi.md#deletenodeset) | **DELETE** /nodeset/{nodeset_id} | Delete a previously uploaded node set
*NodesetApi* | [**getNodeset**](Apis/NodesetApi.md#getnodeset) | **GET** /nodeset/{nodeset_id} | Retrieve information on a previously uploaded node set
*NodesetApi* | [**getNodesets**](Apis/NodesetApi.md#getnodesets) | **GET** /nodesets | List available previously uploaded node sets
*NodesetApi* | [**postNodeset**](Apis/NodesetApi.md#postnodeset) | **POST** /nodeset | Upload a node set for use with DeRegNet algorithms
*ParameterSetApi* | [**deleteParameterSet**](Apis/ParameterSetApi.md#deleteparameterset) | **DELETE** /parameter_set/{parameter_set_id} | Delete a previously uploaded parameter collection
*ParameterSetApi* | [**getParameterSet**](Apis/ParameterSetApi.md#getparameterset) | **GET** /parameter_set/{parameter_set_id} | Retrieve information on a previously uploaded score
*ParameterSetApi* | [**getParameterSetData**](Apis/ParameterSetApi.md#getparametersetdata) | **GET** /parameter_set/{parameter_set_id}/data | Retrieve a parameter collection
*ParameterSetApi* | [**getParameterSetDefault**](Apis/ParameterSetApi.md#getparametersetdefault) | **GET** /parameter_set/default | Retrieve the defaul parameter collection
*ParameterSetApi* | [**getParameterSetDefaultData**](Apis/ParameterSetApi.md#getparametersetdefaultdata) | **GET** /parameter_set/default/data | Retrieve information on a previously uploaded score
*ParameterSetApi* | [**getParameterSets**](Apis/ParameterSetApi.md#getparametersets) | **GET** /parameter_sets | List available previously uploaded parameter collections
*ParameterSetApi* | [**postParameterSet**](Apis/ParameterSetApi.md#postparameterset) | **POST** /parameter_set | Upload a parameters collection for use with DeRegNet algorithms
*RunApi* | [**deleteRun**](Apis/RunApi.md#deleterun) | **DELETE** /run/{run_id} | Cancel an active run, you cannot delete finished runs
*RunApi* | [**getRun**](Apis/RunApi.md#getrun) | **GET** /run/{run_id} | Retrieve the status of a previously submitted run
*RunApi* | [**getRuns**](Apis/RunApi.md#getruns) | **GET** /runs | List current and past runs
*RunApi* | [**postRun**](Apis/RunApi.md#postrun) | **POST** /run | Run average score DeRegNet algorithm
*ScoreApi* | [**deleteScore**](Apis/ScoreApi.md#deletescore) | **DELETE** /score/{score_id} | Delete a previously uploaded node score
*ScoreApi* | [**getScore**](Apis/ScoreApi.md#getscore) | **GET** /score/{score_id} | Retrieve information on a previously uploaded score
*ScoreApi* | [**getScores**](Apis/ScoreApi.md#getscores) | **GET** /scores | List available previously uploaded node scores
*ScoreApi* | [**postScore**](Apis/ScoreApi.md#postscore) | **POST** /score | Upload a node score for use with DeRegNet algorithms
*SubgraphApi* | [**deleteSubgraph**](Apis/SubgraphApi.md#deletesubgraph) | **DELETE** /subgraph/{subgraph_id} | Delete a previously found subgraph
*SubgraphApi* | [**downloadSubgraphAs**](Apis/SubgraphApi.md#downloadsubgraphas) | **GET** /subgraph/{subgraph_id}/{filetype} | Download a subgraph
*SubgraphApi* | [**getSubgraph**](Apis/SubgraphApi.md#getsubgraph) | **GET** /subgraph/{subgraph_id} | Retrieve the information about a subgraph
*SubgraphApi* | [**getSubgraphs**](Apis/SubgraphApi.md#getsubgraphs) | **GET** /subgraphs | List available found subgraphs


<a name="documentation-for-models"></a>
## Documentation for Models

 - [GraphInfo](.//Models/GraphInfo.md)
 - [InitalGraphInfo](.//Models/InitalGraphInfo.md)
 - [NodeSet](.//Models/NodeSet.md)
 - [NodeSetInfo](.//Models/NodeSetInfo.md)
 - [ParameterSet](.//Models/ParameterSet.md)
 - [ParameterSetInfo](.//Models/ParameterSetInfo.md)
 - [RunInfo](.//Models/RunInfo.md)
 - [RunInput](.//Models/RunInput.md)
 - [Score](.//Models/Score.md)
 - [ScoreInfo](.//Models/ScoreInfo.md)
 - [SubgraphInfo](.//Models/SubgraphInfo.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.

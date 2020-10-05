# GraphApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteGraph**](GraphApi.md#deleteGraph) | **DELETE** /graph/{graph_id} | Delete a previously uploaded network
[**getGraph**](GraphApi.md#getGraph) | **GET** /graph/{graph_id} | Retrieve information on a previously uploaded graph 
[**getGraphs**](GraphApi.md#getGraphs) | **GET** /graphs | List available previously uploaded graphs
[**postGraph**](GraphApi.md#postGraph) | **POST** /graph | Allows to initiate GraphML upload
[**postGraphml**](GraphApi.md#postGraphml) | **POST** /graph/{graph_id} | Uploads a GraphML file


<a name="deleteGraph"></a>
# **deleteGraph**
> deleteGraph(graphId)

Delete a previously uploaded network

    Delete a previously uplaoded network

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| ID of the graph to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getGraph"></a>
# **getGraph**
> GraphInfo getGraph(graphId)

Retrieve information on a previously uploaded graph 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| ID of graph to return | [default to null]

### Return type

[**GraphInfo**](..//Models/GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getGraphs"></a>
# **getGraphs**
> List getGraphs(skip, limit)

List available previously uploaded graphs

    Returns a list of all available graphs

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postGraph"></a>
# **postGraph**
> GraphInfo postGraph(initalGraphInfo)

Allows to initiate GraphML upload

    This Endpoint creates a Metadata-Object for a Graph. It returns the endpoint that is to be called with the  file containing the graph as payload/body in the header-attribute \&quot;location\&quot; 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initalGraphInfo** | [**InitalGraphInfo**](..//Models/InitalGraphInfo.md)| The intial Information required for creating a new graph | [optional]

### Return type

[**GraphInfo**](..//Models/GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="postGraphml"></a>
# **postGraphml**
> postGraphml(graphId, fileToUpload)

Uploads a GraphML file

    Adds a Graph to the system. The Graph Object with name:graphname must already be created by issuing a POST Request to /graph with repsective payload 

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| The Name of the graph | [default to null]
 **fileToUpload** | **File**| The file containing the graph | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


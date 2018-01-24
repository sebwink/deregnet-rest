# DeRegNetRestApi.GraphApi

All URIs are relative to *https://virtserver.swaggerhub.com/sebwink/deregnet/1.0.0*

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

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.GraphApi();

let graphId = "graphId_example"; // String | ID of the graph to be deleted


apiInstance.deleteGraph(graphId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| ID of the graph to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getGraph"></a>
# **getGraph**
> GraphInfo getGraph(graphId)

Retrieve information on a previously uploaded graph 

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.GraphApi();

let graphId = "graphId_example"; // String | ID of graph to return


apiInstance.getGraph(graphId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| ID of graph to return | 

### Return type

[**GraphInfo**](GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getGraphs"></a>
# **getGraphs**
> [GraphInfo] getGraphs(opts)

List available previously uploaded graphs

Returns a list of all available graphs

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.GraphApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getGraphs(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchString** | **String**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **Number**| number of records to skip for pagination | [optional] 
 **limit** | **Number**| maximum number of records to return | [optional] 

### Return type

[**[GraphInfo]**](GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postGraph"></a>
# **postGraph**
> postGraph(opts)

Allows to initiate GraphML upload

This Endpoint creates a Metadata-Object for a Graph. It returns the endpoint that is to be called with the  file containing the graph as payload/body in the header-attribute \&quot;location\&quot; 

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.GraphApi();

let opts = { 
  'initalGraphInfo': new DeRegNetRestApi.InitalGraphInfo() // InitalGraphInfo | The intial Information required for creating a new graph
};

apiInstance.postGraph(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initalGraphInfo** | [**InitalGraphInfo**](InitalGraphInfo.md)| The intial Information required for creating a new graph | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="postGraphml"></a>
# **postGraphml**
> postGraphml(graphId, fileToUpload)

Uploads a GraphML file

Adds a Graph to the system. The Graph Object with name:graphname must already be created by issuing a POST Request to /graph with repsective payload 

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.GraphApi();

let graphId = "graphId_example"; // String | The Name of the graph

let fileToUpload = "/path/to/file.txt"; // File | The file containing the graph


apiInstance.postGraphml(graphId, fileToUpload, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graphId** | **String**| The Name of the graph | 
 **fileToUpload** | **File**| The file containing the graph | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


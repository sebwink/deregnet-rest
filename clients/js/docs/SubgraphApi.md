# DeRegNetRestApi.SubgraphApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSubgraph**](SubgraphApi.md#deleteSubgraph) | **DELETE** /subgraph/{subgraph_id} | Delete a previously found subgraph
[**downloadSubgraphAs**](SubgraphApi.md#downloadSubgraphAs) | **GET** /subgraph/{subgraph_id}/{filetype} | Download a subgraph
[**getSubgraph**](SubgraphApi.md#getSubgraph) | **GET** /subgraph/{subgraph_id} | Retrieve the information about a subgraph
[**getSubgraphs**](SubgraphApi.md#getSubgraphs) | **GET** /subgraphs | List available found subgraphs


<a name="deleteSubgraph"></a>
# **deleteSubgraph**
> deleteSubgraph(subgraphId)

Delete a previously found subgraph

Deletes a subgraph

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.SubgraphApi();

let subgraphId = "subgraphId_example"; // String | ID of the order that needs to be deleted


apiInstance.deleteSubgraph(subgraphId, (error, data, response) => {
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
 **subgraphId** | **String**| ID of the order that needs to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="downloadSubgraphAs"></a>
# **downloadSubgraphAs**
> downloadSubgraphAs(subgraphId, filetype)

Download a subgraph

With this GET Request you will retrieve a subgraph   

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.SubgraphApi();

let subgraphId = "subgraphId_example"; // String | The Name of the graph

let filetype = "filetype_example"; // String | File type of file to be downloaded


apiInstance.downloadSubgraphAs(subgraphId, filetype, (error, data, response) => {
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
 **subgraphId** | **String**| The Name of the graph | 
 **filetype** | **String**| File type of file to be downloaded | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

<a name="getSubgraph"></a>
# **getSubgraph**
> SubgraphInfo getSubgraph(subgraphId)

Retrieve the information about a subgraph

Returns a single pet

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.SubgraphApi();

let subgraphId = "subgraphId_example"; // String | ID of subgraph about which to retrieve information


apiInstance.getSubgraph(subgraphId, (error, data, response) => {
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
 **subgraphId** | **String**| ID of subgraph about which to retrieve information | 

### Return type

[**SubgraphInfo**](SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getSubgraphs"></a>
# **getSubgraphs**
> [SubgraphInfo] getSubgraphs(opts)

List available found subgraphs

Returns a single pet

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.SubgraphApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getSubgraphs(opts, (error, data, response) => {
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

[**[SubgraphInfo]**](SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


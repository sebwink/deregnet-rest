# DeRegNetRestApi.NodesetApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteNodeset**](NodesetApi.md#deleteNodeset) | **DELETE** /nodeset/{nodeset_id} | Delete a previously uploaded node set
[**getNodeset**](NodesetApi.md#getNodeset) | **GET** /nodeset/{nodeset_id} | Retrieve information on a previously uploaded node set
[**getNodesets**](NodesetApi.md#getNodesets) | **GET** /nodesets | List available previously uploaded node sets
[**postNodeset**](NodesetApi.md#postNodeset) | **POST** /nodeset | Upload a node set for use with DeRegNet algorithms


<a name="deleteNodeset"></a>
# **deleteNodeset**
> deleteNodeset(nodesetId)

Delete a previously uploaded node set

Deletes a node set

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.NodesetApi();

let nodesetId = "nodesetId_example"; // String | ID of the node set to be deleted


apiInstance.deleteNodeset(nodesetId, (error, data, response) => {
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
 **nodesetId** | **String**| ID of the node set to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getNodeset"></a>
# **getNodeset**
> NodeSetInfo getNodeset(nodesetId)

Retrieve information on a previously uploaded node set

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.NodesetApi();

let nodesetId = "nodesetId_example"; // String | ID of node set to return


apiInstance.getNodeset(nodesetId, (error, data, response) => {
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
 **nodesetId** | **String**| ID of node set to return | 

### Return type

[**NodeSetInfo**](NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getNodesets"></a>
# **getNodesets**
> [NodeSetInfo] getNodesets(opts)

List available previously uploaded node sets

Returns a list with information of all available node sets

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.NodesetApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getNodesets(opts, (error, data, response) => {
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

[**[NodeSetInfo]**](NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postNodeset"></a>
# **postNodeset**
> NodeSetInfo postNodeset(body)

Upload a node set for use with DeRegNet algorithms

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.NodesetApi();

let body = new DeRegNetRestApi.NodeSet(); // NodeSet | Node set to be uploaded for later use with a DeRegNet algorithm


apiInstance.postNodeset(body, (error, data, response) => {
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
 **body** | [**NodeSet**](NodeSet.md)| Node set to be uploaded for later use with a DeRegNet algorithm | 

### Return type

[**NodeSetInfo**](NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


# DeRegNetRestApi.ParameterSetApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteParameterSet**](ParameterSetApi.md#deleteParameterSet) | **DELETE** /parameter_set/{parameter_set_id} | Delete a previously uploaded parameter collection
[**getParameterSet**](ParameterSetApi.md#getParameterSet) | **GET** /parameter_set/{parameter_set_id} | Retrieve information on a previously uploaded score
[**getParameterSetData**](ParameterSetApi.md#getParameterSetData) | **GET** /parameter_set/{parameter_set_id}/data | Retrieve a parameter collection
[**getParameterSetDefault**](ParameterSetApi.md#getParameterSetDefault) | **GET** /parameter_set/default | Retrieve the defaul parameter collection
[**getParameterSetDefaultData**](ParameterSetApi.md#getParameterSetDefaultData) | **GET** /parameter_set/default/data | Retrieve information on a previously uploaded score
[**getParameterSets**](ParameterSetApi.md#getParameterSets) | **GET** /parameter_sets | List available previously uploaded parameter collections
[**postParameterSet**](ParameterSetApi.md#postParameterSet) | **POST** /parameter_set | Upload a parameters collection for use with DeRegNet algorithms


<a name="deleteParameterSet"></a>
# **deleteParameterSet**
> deleteParameterSet(parameterSetId)

Delete a previously uploaded parameter collection

Deletes a parameter collection

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

let parameterSetId = "parameterSetId_example"; // String | ID of the parameter collection to be deleted


apiInstance.deleteParameterSet(parameterSetId, (error, data, response) => {
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
 **parameterSetId** | **String**| ID of the parameter collection to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getParameterSet"></a>
# **getParameterSet**
> ParameterSetInfo getParameterSet(parameterSetId)

Retrieve information on a previously uploaded score

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

let parameterSetId = "parameterSetId_example"; // String | ID of parameter collection to retrieve information about


apiInstance.getParameterSet(parameterSetId, (error, data, response) => {
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
 **parameterSetId** | **String**| ID of parameter collection to retrieve information about | 

### Return type

[**ParameterSetInfo**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getParameterSetData"></a>
# **getParameterSetData**
> ParameterSet getParameterSetData(parameterSetId)

Retrieve a parameter collection

Returns a parameter collection

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

let parameterSetId = "parameterSetId_example"; // String | ID of the parameter collection to return


apiInstance.getParameterSetData(parameterSetId, (error, data, response) => {
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
 **parameterSetId** | **String**| ID of the parameter collection to return | 

### Return type

[**ParameterSet**](ParameterSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getParameterSetDefault"></a>
# **getParameterSetDefault**
> ParameterSetInfo getParameterSetDefault()

Retrieve the defaul parameter collection

Returns the default parameter collection

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

apiInstance.getParameterSetDefault((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ParameterSetInfo**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getParameterSetDefaultData"></a>
# **getParameterSetDefaultData**
> ParameterSet getParameterSetDefaultData()

Retrieve information on a previously uploaded score

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

apiInstance.getParameterSetDefaultData((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ParameterSet**](ParameterSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getParameterSets"></a>
# **getParameterSets**
> [ParameterSetInfo] getParameterSets(opts)

List available previously uploaded parameter collections

Returns a list with information about availabel parameter collections

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getParameterSets(opts, (error, data, response) => {
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

[**[ParameterSetInfo]**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postParameterSet"></a>
# **postParameterSet**
> ParameterSetInfo postParameterSet(body)

Upload a parameters collection for use with DeRegNet algorithms

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ParameterSetApi();

let body = new DeRegNetRestApi.ParameterSet(); // ParameterSet | Parameters to be uploaded for later use with a DeRegNet algorithm


apiInstance.postParameterSet(body, (error, data, response) => {
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
 **body** | [**ParameterSet**](ParameterSet.md)| Parameters to be uploaded for later use with a DeRegNet algorithm | 

### Return type

[**ParameterSetInfo**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


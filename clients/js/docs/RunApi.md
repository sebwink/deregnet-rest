# DeRegNetRestApi.RunApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRun**](RunApi.md#deleteRun) | **DELETE** /run/{run_id} | Cancel an active run, you cannot delete finished runs
[**getRun**](RunApi.md#getRun) | **GET** /run/{run_id} | Retrieve the status of a previously submitted run
[**getRuns**](RunApi.md#getRuns) | **GET** /runs | List current and past runs
[**postRun**](RunApi.md#postRun) | **POST** /run | Run average score DeRegNet algorithm


<a name="deleteRun"></a>
# **deleteRun**
> deleteRun(runId)

Cancel an active run, you cannot delete finished runs

Cancel a run

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.RunApi();

let runId = "runId_example"; // String | ID of the run to be deleted


apiInstance.deleteRun(runId, (error, data, response) => {
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
 **runId** | **String**| ID of the run to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRun"></a>
# **getRun**
> RunInfo getRun(runId)

Retrieve the status of a previously submitted run

Returns a single pet

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.RunApi();

let runId = "runId_example"; // String | ID of pet to return


apiInstance.getRun(runId, (error, data, response) => {
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
 **runId** | **String**| ID of pet to return | 

### Return type

[**RunInfo**](RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRuns"></a>
# **getRuns**
> [RunInfo] getRuns(opts)

List current and past runs

Returns a single pet

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.RunApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getRuns(opts, (error, data, response) => {
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

[**[RunInfo]**](RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postRun"></a>
# **postRun**
> RunInfo postRun(body)

Run average score DeRegNet algorithm

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.RunApi();

let body = new DeRegNetRestApi.RunInput(); // RunInput | All data needed to run the algorithm


apiInstance.postRun(body, (error, data, response) => {
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
 **body** | [**RunInput**](RunInput.md)| All data needed to run the algorithm | 

### Return type

[**RunInfo**](RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


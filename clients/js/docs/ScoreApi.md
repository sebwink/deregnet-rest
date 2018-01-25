# DeRegNetRestApi.ScoreApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteScore**](ScoreApi.md#deleteScore) | **DELETE** /score/{score_id} | Delete a previously uploaded node score
[**getScore**](ScoreApi.md#getScore) | **GET** /score/{score_id} | Retrieve information on a previously uploaded score
[**getScores**](ScoreApi.md#getScores) | **GET** /scores | List available previously uploaded node scores
[**postScore**](ScoreApi.md#postScore) | **POST** /score | Upload a node score for use with DeRegNet algorithms


<a name="deleteScore"></a>
# **deleteScore**
> deleteScore(scoreId)

Delete a previously uploaded node score

Delete a previously uploaded node score

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ScoreApi();

let scoreId = "scoreId_example"; // String | ID of the node score to be deleted


apiInstance.deleteScore(scoreId, (error, data, response) => {
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
 **scoreId** | **String**| ID of the node score to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getScore"></a>
# **getScore**
> ScoreInfo getScore(scoreId)

Retrieve information on a previously uploaded score

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ScoreApi();

let scoreId = "scoreId_example"; // String | ID of node score to return


apiInstance.getScore(scoreId, (error, data, response) => {
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
 **scoreId** | **String**| ID of node score to return | 

### Return type

[**ScoreInfo**](ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getScores"></a>
# **getScores**
> [ScoreInfo] getScores(opts)

List available previously uploaded node scores

Returns a list with all available node scores

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ScoreApi();

let opts = { 
  'searchString': "searchString_example", // String | pass an optional search string for narrowing the list
  'skip': 56, // Number | number of records to skip for pagination
  'limit': 56 // Number | maximum number of records to return
};

apiInstance.getScores(opts, (error, data, response) => {
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

[**[ScoreInfo]**](ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="postScore"></a>
# **postScore**
> ScoreInfo postScore(body)

Upload a node score for use with DeRegNet algorithms

### Example
```javascript
import DeRegNetRestApi from 'de_reg_net_rest_api';

let apiInstance = new DeRegNetRestApi.ScoreApi();

let body = new DeRegNetRestApi.Score(); // Score | Node scores to be uploaded for later use with a DeRegNet algorithm


apiInstance.postScore(body, (error, data, response) => {
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
 **body** | [**Score**](Score.md)| Node scores to be uploaded for later use with a DeRegNet algorithm | 

### Return type

[**ScoreInfo**](ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


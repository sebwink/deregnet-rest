# swagger_client.ScoreApi

All URIs are relative to *https://virtserver.swaggerhub.com/sebwink/deregnet/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_score**](ScoreApi.md#delete_score) | **DELETE** /score/{score_id} | Delete a previously uploaded node score
[**get_score**](ScoreApi.md#get_score) | **GET** /score/{score_id} | Retrieve information on a previously uploaded score
[**get_scores**](ScoreApi.md#get_scores) | **GET** /scores | List available previously uploaded node scores
[**post_score**](ScoreApi.md#post_score) | **POST** /score | Upload a node score for use with DeRegNet algorithms


# **delete_score**
> delete_score(score_id)

Delete a previously uploaded node score

Delete a previously uploaded node score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScoreApi()
score_id = 'score_id_example' # str | ID of the node score to be deleted

try:
    # Delete a previously uploaded node score
    api_instance.delete_score(score_id)
except ApiException as e:
    print("Exception when calling ScoreApi->delete_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score_id** | **str**| ID of the node score to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score**
> ScoreInfo get_score(score_id)

Retrieve information on a previously uploaded score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScoreApi()
score_id = 'score_id_example' # str | ID of node score to return

try:
    # Retrieve information on a previously uploaded score
    api_response = api_instance.get_score(score_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **score_id** | **str**| ID of node score to return | 

### Return type

[**ScoreInfo**](ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scores**
> list[ScoreInfo] get_scores(search_string=search_string, skip=skip, limit=limit)

List available previously uploaded node scores

Returns a list with all available node scores

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScoreApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List available previously uploaded node scores
    api_response = api_instance.get_scores(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreApi->get_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[ScoreInfo]**](ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_score**
> post_score(body)

Upload a node score for use with DeRegNet algorithms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScoreApi()
body = swagger_client.Score() # Score | Node scores to be uploaded for later use with a DeRegNet algorithm

try:
    # Upload a node score for use with DeRegNet algorithms
    api_instance.post_score(body)
except ApiException as e:
    print("Exception when calling ScoreApi->post_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Score**](Score.md)| Node scores to be uploaded for later use with a DeRegNet algorithm | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


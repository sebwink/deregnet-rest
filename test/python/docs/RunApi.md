# swagger_client.RunApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_run**](RunApi.md#delete_run) | **DELETE** /run/{run_id} | Cancel an active run, you cannot delete finished runs
[**get_run**](RunApi.md#get_run) | **GET** /run/{run_id} | Retrieve the status of a previously submitted run
[**get_runs**](RunApi.md#get_runs) | **GET** /runs | List current and past runs
[**post_run**](RunApi.md#post_run) | **POST** /run | Run average score DeRegNet algorithm


# **delete_run**
> delete_run(run_id)

Cancel an active run, you cannot delete finished runs

Cancel a run

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
run_id = 'run_id_example' # str | ID of the run to be deleted

try:
    # Cancel an active run, you cannot delete finished runs
    api_instance.delete_run(run_id)
except ApiException as e:
    print("Exception when calling RunApi->delete_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of the run to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> RunInfo get_run(run_id)

Retrieve the status of a previously submitted run

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
run_id = 'run_id_example' # str | ID of pet to return

try:
    # Retrieve the status of a previously submitted run
    api_response = api_instance.get_run(run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| ID of pet to return | 

### Return type

[**RunInfo**](RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runs**
> list[RunInfo] get_runs(search_string=search_string, skip=skip, limit=limit)

List current and past runs

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List current and past runs
    api_response = api_instance.get_runs(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[RunInfo]**](RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_run**
> RunInfo post_run(body)

Run average score DeRegNet algorithm

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunApi()
body = swagger_client.RunInput() # RunInput | All data needed to run the algorithm

try:
    # Run average score DeRegNet algorithm
    api_response = api_instance.post_run(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->post_run: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


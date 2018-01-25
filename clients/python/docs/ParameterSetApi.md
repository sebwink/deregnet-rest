# swagger_client.ParameterSetApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_parameter_set**](ParameterSetApi.md#delete_parameter_set) | **DELETE** /parameter_set/{parameter_set_id} | Delete a previously uploaded parameter collection
[**get_parameter_set**](ParameterSetApi.md#get_parameter_set) | **GET** /parameter_set/{parameter_set_id} | Retrieve information on a previously uploaded score
[**get_parameter_set_data**](ParameterSetApi.md#get_parameter_set_data) | **GET** /parameter_set/{parameter_set_id}/data | Retrieve a parameter collection
[**get_parameter_set_default**](ParameterSetApi.md#get_parameter_set_default) | **GET** /parameter_set/default | Retrieve the defaul parameter collection
[**get_parameter_set_default_data**](ParameterSetApi.md#get_parameter_set_default_data) | **GET** /parameter_set/default/data | Retrieve information on a previously uploaded score
[**get_parameter_sets**](ParameterSetApi.md#get_parameter_sets) | **GET** /parameter_sets | List available previously uploaded parameter collections
[**post_parameter_set**](ParameterSetApi.md#post_parameter_set) | **POST** /parameter_set | Upload a parameters collection for use with DeRegNet algorithms


# **delete_parameter_set**
> delete_parameter_set(parameter_set_id)

Delete a previously uploaded parameter collection

Deletes a parameter collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()
parameter_set_id = 'parameter_set_id_example' # str | ID of the parameter collection to be deleted

try:
    # Delete a previously uploaded parameter collection
    api_instance.delete_parameter_set(parameter_set_id)
except ApiException as e:
    print("Exception when calling ParameterSetApi->delete_parameter_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_set_id** | **str**| ID of the parameter collection to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_set**
> ParameterSetInfo get_parameter_set(parameter_set_id)

Retrieve information on a previously uploaded score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()
parameter_set_id = 'parameter_set_id_example' # str | ID of parameter collection to retrieve information about

try:
    # Retrieve information on a previously uploaded score
    api_response = api_instance.get_parameter_set(parameter_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->get_parameter_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_set_id** | **str**| ID of parameter collection to retrieve information about | 

### Return type

[**ParameterSetInfo**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_set_data**
> ParameterSet get_parameter_set_data(parameter_set_id)

Retrieve a parameter collection

Returns a parameter collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()
parameter_set_id = 'parameter_set_id_example' # str | ID of the parameter collection to return

try:
    # Retrieve a parameter collection
    api_response = api_instance.get_parameter_set_data(parameter_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->get_parameter_set_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_set_id** | **str**| ID of the parameter collection to return | 

### Return type

[**ParameterSet**](ParameterSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_set_default**
> ParameterSetInfo get_parameter_set_default()

Retrieve the defaul parameter collection

Returns the default parameter collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()

try:
    # Retrieve the defaul parameter collection
    api_response = api_instance.get_parameter_set_default()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->get_parameter_set_default: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_set_default_data**
> ParameterSet get_parameter_set_default_data()

Retrieve information on a previously uploaded score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()

try:
    # Retrieve information on a previously uploaded score
    api_response = api_instance.get_parameter_set_default_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->get_parameter_set_default_data: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_sets**
> list[ParameterSetInfo] get_parameter_sets(search_string=search_string, skip=skip, limit=limit)

List available previously uploaded parameter collections

Returns a list with information about availabel parameter collections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List available previously uploaded parameter collections
    api_response = api_instance.get_parameter_sets(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->get_parameter_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[ParameterSetInfo]**](ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_parameter_set**
> ParameterSetInfo post_parameter_set(body)

Upload a parameters collection for use with DeRegNet algorithms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParameterSetApi()
body = swagger_client.ParameterSet() # ParameterSet | Parameters to be uploaded for later use with a DeRegNet algorithm

try:
    # Upload a parameters collection for use with DeRegNet algorithms
    api_response = api_instance.post_parameter_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterSetApi->post_parameter_set: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.NodesetApi

All URIs are relative to *https://localhost/deregnet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nodeset**](NodesetApi.md#delete_nodeset) | **DELETE** /nodeset/{nodeset_id} | Delete a previously uploaded node set
[**get_nodeset**](NodesetApi.md#get_nodeset) | **GET** /nodeset/{nodeset_id} | Retrieve information on a previously uploaded node set
[**get_nodesets**](NodesetApi.md#get_nodesets) | **GET** /nodesets | List available previously uploaded node sets
[**post_nodeset**](NodesetApi.md#post_nodeset) | **POST** /nodeset | Upload a node set for use with DeRegNet algorithms


# **delete_nodeset**
> delete_nodeset(nodeset_id)

Delete a previously uploaded node set

Deletes a node set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodesetApi()
nodeset_id = 'nodeset_id_example' # str | ID of the node set to be deleted

try:
    # Delete a previously uploaded node set
    api_instance.delete_nodeset(nodeset_id)
except ApiException as e:
    print("Exception when calling NodesetApi->delete_nodeset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeset_id** | **str**| ID of the node set to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodeset**
> NodeSetInfo get_nodeset(nodeset_id)

Retrieve information on a previously uploaded node set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodesetApi()
nodeset_id = 'nodeset_id_example' # str | ID of node set to return

try:
    # Retrieve information on a previously uploaded node set
    api_response = api_instance.get_nodeset(nodeset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesetApi->get_nodeset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeset_id** | **str**| ID of node set to return | 

### Return type

[**NodeSetInfo**](NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodesets**
> list[NodeSetInfo] get_nodesets(search_string=search_string, skip=skip, limit=limit)

List available previously uploaded node sets

Returns a list with information of all available node sets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodesetApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List available previously uploaded node sets
    api_response = api_instance.get_nodesets(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesetApi->get_nodesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[NodeSetInfo]**](NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nodeset**
> NodeSetInfo post_nodeset(body)

Upload a node set for use with DeRegNet algorithms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodesetApi()
body = swagger_client.NodeSet() # NodeSet | Node set to be uploaded for later use with a DeRegNet algorithm

try:
    # Upload a node set for use with DeRegNet algorithms
    api_response = api_instance.post_nodeset(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesetApi->post_nodeset: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


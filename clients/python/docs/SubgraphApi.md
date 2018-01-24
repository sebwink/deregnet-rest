# swagger_client.SubgraphApi

All URIs are relative to *https://virtserver.swaggerhub.com/sebwink/deregnet/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subgraph**](SubgraphApi.md#delete_subgraph) | **DELETE** /subgraph/{subgraph_id} | Delete a previously found subgraph
[**download_subgraph_as**](SubgraphApi.md#download_subgraph_as) | **GET** /subgraph/{subgraph_id}/{filetype} | Download a subgraph
[**get_subgraph**](SubgraphApi.md#get_subgraph) | **GET** /subgraph/{subgraph_id} | Retrieve the information about a subgraph
[**get_subgraphs**](SubgraphApi.md#get_subgraphs) | **GET** /subgraphs | List available found subgraphs


# **delete_subgraph**
> delete_subgraph(subgraph_id)

Delete a previously found subgraph

Deletes a subgraph

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubgraphApi()
subgraph_id = 'subgraph_id_example' # str | ID of the order that needs to be deleted

try:
    # Delete a previously found subgraph
    api_instance.delete_subgraph(subgraph_id)
except ApiException as e:
    print("Exception when calling SubgraphApi->delete_subgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraph_id** | **str**| ID of the order that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_subgraph_as**
> download_subgraph_as(subgraph_id, filetype)

Download a subgraph

With this GET Request you will retrieve a subgraph   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubgraphApi()
subgraph_id = 'subgraph_id_example' # str | The Name of the graph
filetype = 'filetype_example' # str | File type of file to be downloaded

try:
    # Download a subgraph
    api_instance.download_subgraph_as(subgraph_id, filetype)
except ApiException as e:
    print("Exception when calling SubgraphApi->download_subgraph_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraph_id** | **str**| The Name of the graph | 
 **filetype** | **str**| File type of file to be downloaded | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subgraph**
> SubgraphInfo get_subgraph(subgraph_id)

Retrieve the information about a subgraph

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubgraphApi()
subgraph_id = 'subgraph_id_example' # str | ID of subgraph about which to retrieve information

try:
    # Retrieve the information about a subgraph
    api_response = api_instance.get_subgraph(subgraph_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubgraphApi->get_subgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraph_id** | **str**| ID of subgraph about which to retrieve information | 

### Return type

[**SubgraphInfo**](SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subgraphs**
> list[SubgraphInfo] get_subgraphs(search_string=search_string, skip=skip, limit=limit)

List available found subgraphs

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubgraphApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List available found subgraphs
    api_response = api_instance.get_subgraphs(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubgraphApi->get_subgraphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[SubgraphInfo]**](SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


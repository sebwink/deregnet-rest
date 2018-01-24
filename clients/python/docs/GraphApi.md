# swagger_client.GraphApi

All URIs are relative to *https://virtserver.swaggerhub.com/sebwink/deregnet/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_graph**](GraphApi.md#delete_graph) | **DELETE** /graph/{graph_id} | Delete a previously uploaded network
[**get_graph**](GraphApi.md#get_graph) | **GET** /graph/{graph_id} | Retrieve information on a previously uploaded graph 
[**get_graphs**](GraphApi.md#get_graphs) | **GET** /graphs | List available previously uploaded graphs
[**post_graph**](GraphApi.md#post_graph) | **POST** /graph | Allows to initiate GraphML upload
[**post_graphml**](GraphApi.md#post_graphml) | **POST** /graph/{graph_id} | Uploads a GraphML file


# **delete_graph**
> delete_graph(graph_id)

Delete a previously uploaded network

Delete a previously uplaoded network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
graph_id = 'graph_id_example' # str | ID of the graph to be deleted

try:
    # Delete a previously uploaded network
    api_instance.delete_graph(graph_id)
except ApiException as e:
    print("Exception when calling GraphApi->delete_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| ID of the graph to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graph**
> GraphInfo get_graph(graph_id)

Retrieve information on a previously uploaded graph 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
graph_id = 'graph_id_example' # str | ID of graph to return

try:
    # Retrieve information on a previously uploaded graph 
    api_response = api_instance.get_graph(graph_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->get_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| ID of graph to return | 

### Return type

[**GraphInfo**](GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_graphs**
> list[GraphInfo] get_graphs(search_string=search_string, skip=skip, limit=limit)

List available previously uploaded graphs

Returns a list of all available graphs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
search_string = 'search_string_example' # str | pass an optional search string for narrowing the list (optional)
skip = 56 # int | number of records to skip for pagination (optional)
limit = 56 # int | maximum number of records to return (optional)

try:
    # List available previously uploaded graphs
    api_response = api_instance.get_graphs(search_string=search_string, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->get_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass an optional search string for narrowing the list | [optional] 
 **skip** | **int**| number of records to skip for pagination | [optional] 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**list[GraphInfo]**](GraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_graph**
> post_graph(inital_graph_info=inital_graph_info)

Allows to initiate GraphML upload

This Endpoint creates a Metadata-Object for a Graph. It returns the endpoint that is to be called with the  file containing the graph as payload/body in the header-attribute \"location\" 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
inital_graph_info = swagger_client.InitalGraphInfo() # InitalGraphInfo | The intial Information required for creating a new graph (optional)

try:
    # Allows to initiate GraphML upload
    api_instance.post_graph(inital_graph_info=inital_graph_info)
except ApiException as e:
    print("Exception when calling GraphApi->post_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inital_graph_info** | [**InitalGraphInfo**](InitalGraphInfo.md)| The intial Information required for creating a new graph | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_graphml**
> post_graphml(graph_id, file_to_upload)

Uploads a GraphML file

Adds a Graph to the system. The Graph Object with name:graphname must already be created by issuing a POST Request to /graph with repsective payload 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
graph_id = 'graph_id_example' # str | The Name of the graph
file_to_upload = '/path/to/file.txt' # file | The file containing the graph

try:
    # Uploads a GraphML file
    api_instance.post_graphml(graph_id, file_to_upload)
except ApiException as e:
    print("Exception when calling GraphApi->post_graphml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_id** | **str**| The Name of the graph | 
 **file_to_upload** | **file**| The file containing the graph | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


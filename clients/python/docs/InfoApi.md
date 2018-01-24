# swagger_client.InfoApi

All URIs are relative to *https://virtserver.swaggerhub.com/sebwink/deregnet/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_docs**](InfoApi.md#graph_docs) | **GET** /info/graph | Help page on graph endpoint
[**help**](InfoApi.md#help) | **GET** /info | General help page
[**index**](InfoApi.md#index) | **GET** / | Index, redirects to /info
[**info_docs**](InfoApi.md#info_docs) | **GET** /info/info | Help page on info endpoint
[**nodeset_docs**](InfoApi.md#nodeset_docs) | **GET** /info/nodeset | Help page on nodeset endpoint
[**parameter_set_docs**](InfoApi.md#parameter_set_docs) | **GET** /info/parameter_set | Help page on subgraph endpoint
[**run_docs**](InfoApi.md#run_docs) | **GET** /info/run | Help page on run endpoint
[**score_docs**](InfoApi.md#score_docs) | **GET** /info/score | Help page on score endpoint
[**subgraph_docs**](InfoApi.md#subgraph_docs) | **GET** /info/subgraph | Help page on subgraph endpoint


# **graph_docs**
> graph_docs()

Help page on graph endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on graph endpoint
    api_instance.graph_docs()
except ApiException as e:
    print("Exception when calling InfoApi->graph_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **help**
> help()

General help page

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # General help page
    api_instance.help()
except ApiException as e:
    print("Exception when calling InfoApi->help: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index**
> index()

Index, redirects to /info

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Index, redirects to /info
    api_instance.index()
except ApiException as e:
    print("Exception when calling InfoApi->index: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_docs**
> info_docs()

Help page on info endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on info endpoint
    api_instance.info_docs()
except ApiException as e:
    print("Exception when calling InfoApi->info_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodeset_docs**
> nodeset_docs()

Help page on nodeset endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on nodeset endpoint
    api_instance.nodeset_docs()
except ApiException as e:
    print("Exception when calling InfoApi->nodeset_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameter_set_docs**
> parameter_set_docs()

Help page on subgraph endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on subgraph endpoint
    api_instance.parameter_set_docs()
except ApiException as e:
    print("Exception when calling InfoApi->parameter_set_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_docs**
> run_docs()

Help page on run endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on run endpoint
    api_instance.run_docs()
except ApiException as e:
    print("Exception when calling InfoApi->run_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_docs**
> score_docs()

Help page on score endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on score endpoint
    api_instance.score_docs()
except ApiException as e:
    print("Exception when calling InfoApi->score_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subgraph_docs**
> subgraph_docs()

Help page on subgraph endpoint

Returns a single pet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InfoApi()

try:
    # Help page on subgraph endpoint
    api_instance.subgraph_docs()
except ApiException as e:
    print("Exception when calling InfoApi->subgraph_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


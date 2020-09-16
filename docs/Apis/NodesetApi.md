# NodesetApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteNodeset**](NodesetApi.md#deleteNodeset) | **DELETE** /nodeset/{nodeset_id} | Delete a previously uploaded node set
[**getNodeset**](NodesetApi.md#getNodeset) | **GET** /nodeset/{nodeset_id} | Retrieve information on a previously uploaded node set
[**getNodesets**](NodesetApi.md#getNodesets) | **GET** /nodesets | List available previously uploaded node sets
[**postNodeset**](NodesetApi.md#postNodeset) | **POST** /nodeset | Upload a node set for use with DeRegNet algorithms


<a name="deleteNodeset"></a>
# **deleteNodeset**
> deleteNodeset(nodesetId)

Delete a previously uploaded node set

    Deletes a node set

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodesetId** | **String**| ID of the node set to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getNodeset"></a>
# **getNodeset**
> NodeSetInfo getNodeset(nodesetId)

Retrieve information on a previously uploaded node set

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodesetId** | **String**| ID of node set to return | [default to null]

### Return type

[**NodeSetInfo**](..//Models/NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNodesets"></a>
# **getNodesets**
> List getNodesets(skip, limit)

List available previously uploaded node sets

    Returns a list with information of all available node sets

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postNodeset"></a>
# **postNodeset**
> NodeSetInfo postNodeset(body)

Upload a node set for use with DeRegNet algorithms

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSet**](..//Models/NodeSet.md)| Node set to be uploaded for later use with a DeRegNet algorithm |

### Return type

[**NodeSetInfo**](..//Models/NodeSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


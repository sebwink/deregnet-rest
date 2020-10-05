# SubgraphApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSubgraph**](SubgraphApi.md#deleteSubgraph) | **DELETE** /subgraph/{subgraph_id} | Delete a previously found subgraph
[**downloadSubgraphAs**](SubgraphApi.md#downloadSubgraphAs) | **GET** /subgraph/{subgraph_id}/{filetype} | Download a subgraph
[**getSubgraph**](SubgraphApi.md#getSubgraph) | **GET** /subgraph/{subgraph_id} | Retrieve the information about a subgraph
[**getSubgraphs**](SubgraphApi.md#getSubgraphs) | **GET** /subgraphs | List available found subgraphs


<a name="deleteSubgraph"></a>
# **deleteSubgraph**
> deleteSubgraph(subgraphId)

Delete a previously found subgraph

    Deletes a subgraph

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraphId** | **String**| ID of the order that needs to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="downloadSubgraphAs"></a>
# **downloadSubgraphAs**
> downloadSubgraphAs(subgraphId, filetype)

Download a subgraph

    With this GET Request you will retrieve a subgraph   

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraphId** | **String**| The Name of the graph | [default to null]
 **filetype** | **String**| File type of file to be downloaded | [default to null] [enum: graphml, sif, gmt, grp]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getSubgraph"></a>
# **getSubgraph**
> SubgraphInfo getSubgraph(subgraphId)

Retrieve the information about a subgraph

    Returns a single pet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subgraphId** | **String**| ID of subgraph about which to retrieve information | [default to null]

### Return type

[**SubgraphInfo**](..//Models/SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSubgraphs"></a>
# **getSubgraphs**
> List getSubgraphs(skip, limit)

List available found subgraphs

    Returns a single pet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/SubgraphInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


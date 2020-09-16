# ParameterSetApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteParameterSet**](ParameterSetApi.md#deleteParameterSet) | **DELETE** /parameter_set/{parameter_set_id} | Delete a previously uploaded parameter collection
[**getParameterSet**](ParameterSetApi.md#getParameterSet) | **GET** /parameter_set/{parameter_set_id} | Retrieve information on a previously uploaded score
[**getParameterSetData**](ParameterSetApi.md#getParameterSetData) | **GET** /parameter_set/{parameter_set_id}/data | Retrieve a parameter collection
[**getParameterSetDefault**](ParameterSetApi.md#getParameterSetDefault) | **GET** /parameter_set/default | Retrieve the defaul parameter collection
[**getParameterSetDefaultData**](ParameterSetApi.md#getParameterSetDefaultData) | **GET** /parameter_set/default/data | Retrieve information on a previously uploaded score
[**getParameterSets**](ParameterSetApi.md#getParameterSets) | **GET** /parameter_sets | List available previously uploaded parameter collections
[**postParameterSet**](ParameterSetApi.md#postParameterSet) | **POST** /parameter_set | Upload a parameters collection for use with DeRegNet algorithms


<a name="deleteParameterSet"></a>
# **deleteParameterSet**
> deleteParameterSet(parameterSetId)

Delete a previously uploaded parameter collection

    Deletes a parameter collection

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameterSetId** | **String**| ID of the parameter collection to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getParameterSet"></a>
# **getParameterSet**
> ParameterSetInfo getParameterSet(parameterSetId)

Retrieve information on a previously uploaded score

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameterSetId** | **String**| ID of parameter collection to retrieve information about | [default to null]

### Return type

[**ParameterSetInfo**](..//Models/ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getParameterSetData"></a>
# **getParameterSetData**
> ParameterSet getParameterSetData(parameterSetId)

Retrieve a parameter collection

    Returns a parameter collection

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameterSetId** | **String**| ID of the parameter collection to return | [default to null]

### Return type

[**ParameterSet**](..//Models/ParameterSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getParameterSetDefault"></a>
# **getParameterSetDefault**
> ParameterSetInfo getParameterSetDefault()

Retrieve the defaul parameter collection

    Returns the default parameter collection

### Parameters
This endpoint does not need any parameter.

### Return type

[**ParameterSetInfo**](..//Models/ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getParameterSetDefaultData"></a>
# **getParameterSetDefaultData**
> ParameterSet getParameterSetDefaultData()

Retrieve information on a previously uploaded score

### Parameters
This endpoint does not need any parameter.

### Return type

[**ParameterSet**](..//Models/ParameterSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getParameterSets"></a>
# **getParameterSets**
> List getParameterSets(skip, limit)

List available previously uploaded parameter collections

    Returns a list with information about availabel parameter collections

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postParameterSet"></a>
# **postParameterSet**
> ParameterSetInfo postParameterSet(body)

Upload a parameters collection for use with DeRegNet algorithms

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ParameterSet**](..//Models/ParameterSet.md)| Parameters to be uploaded for later use with a DeRegNet algorithm |

### Return type

[**ParameterSetInfo**](..//Models/ParameterSetInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


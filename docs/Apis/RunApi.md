# RunApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRun**](RunApi.md#deleteRun) | **DELETE** /run/{run_id} | Cancel an active run, you cannot delete finished runs
[**getRun**](RunApi.md#getRun) | **GET** /run/{run_id} | Retrieve the status of a previously submitted run
[**getRuns**](RunApi.md#getRuns) | **GET** /runs | List current and past runs
[**postRun**](RunApi.md#postRun) | **POST** /run | Run average score DeRegNet algorithm


<a name="deleteRun"></a>
# **deleteRun**
> deleteRun(runId)

Cancel an active run, you cannot delete finished runs

    Cancel a run

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runId** | **String**| ID of the run to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getRun"></a>
# **getRun**
> RunInfo getRun(runId)

Retrieve the status of a previously submitted run

    Returns a single pet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runId** | **String**| ID of pet to return | [default to null]

### Return type

[**RunInfo**](..//Models/RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRuns"></a>
# **getRuns**
> List getRuns(skip, limit)

List current and past runs

    Returns a single pet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postRun"></a>
# **postRun**
> RunInfo postRun(body)

Run average score DeRegNet algorithm

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunInput**](..//Models/RunInput.md)| All data needed to run the algorithm |

### Return type

[**RunInfo**](..//Models/RunInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


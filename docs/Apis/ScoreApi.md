# ScoreApi

All URIs are relative to *http://api.dereg.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteScore**](ScoreApi.md#deleteScore) | **DELETE** /score/{score_id} | Delete a previously uploaded node score
[**getScore**](ScoreApi.md#getScore) | **GET** /score/{score_id} | Retrieve information on a previously uploaded score
[**getScores**](ScoreApi.md#getScores) | **GET** /scores | List available previously uploaded node scores
[**postScore**](ScoreApi.md#postScore) | **POST** /score | Upload a node score for use with DeRegNet algorithms


<a name="deleteScore"></a>
# **deleteScore**
> deleteScore(scoreId)

Delete a previously uploaded node score

    Delete a previously uploaded node score

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoreId** | **String**| ID of the node score to be deleted | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getScore"></a>
# **getScore**
> ScoreInfo getScore(scoreId)

Retrieve information on a previously uploaded score

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoreId** | **String**| ID of node score to return | [default to null]

### Return type

[**ScoreInfo**](..//Models/ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getScores"></a>
# **getScores**
> List getScores(skip, limit)

List available previously uploaded node scores

    Returns a list with all available node scores

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Integer**| number of records to skip for pagination | [optional] [default to 0]
 **limit** | **Integer**| maximum number of records to return | [optional] [default to 1000]

### Return type

[**List**](..//Models/ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="postScore"></a>
# **postScore**
> ScoreInfo postScore(body)

Upload a node score for use with DeRegNet algorithms

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Score**](..//Models/Score.md)| Node scores to be uploaded for later use with a DeRegNet algorithm |

### Return type

[**ScoreInfo**](..//Models/ScoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


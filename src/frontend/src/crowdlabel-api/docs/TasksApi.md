# CrowdLabelApi.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claimTaskTasksTaskIdClaimPost**](TasksApi.md#claimTaskTasksTaskIdClaimPost) | **POST** /tasks/{task_id}/claim | Claim Task
[**completeTasksTaskIdCompletePost**](TasksApi.md#completeTasksTaskIdCompletePost) | **POST** /tasks/{task_id}/complete | Complete
[**deleteTaskTasksTaskIdDelete**](TasksApi.md#deleteTaskTasksTaskIdDelete) | **DELETE** /tasks/{task_id} | Delete Task
[**downloadTaskResultsTasksTaskIdDownloadGet**](TasksApi.md#downloadTaskResultsTasksTaskIdDownloadGet) | **GET** /tasks/{task_id}/download | Download Task Results
[**getCoverTasksTaskIdCoverImageGet**](TasksApi.md#getCoverTasksTaskIdCoverImageGet) | **GET** /tasks/{task_id}/cover-image | Get Cover
[**getProgressTasksTaskIdProgressGet**](TasksApi.md#getProgressTasksTaskIdProgressGet) | **GET** /tasks/{task_id}/progress | Get Progress
[**getTaskTasksTaskIdGet**](TasksApi.md#getTaskTasksTaskIdGet) | **GET** /tasks/{task_id} | Get Task
[**searchTasksTasksPut**](TasksApi.md#searchTasksTasksPut) | **PUT** /tasks/ | Search Tasks
[**uploadTaskTasksUploadPost**](TasksApi.md#uploadTaskTasksUploadPost) | **POST** /tasks/upload | Upload Task



## claimTaskTasksTaskIdClaimPost

> Task claimTaskTasksTaskIdClaimPost(taskId)

Claim Task

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.claimTaskTasksTaskIdClaimPost(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeTasksTaskIdCompletePost

> Object completeTasksTaskIdCompletePost(taskId)

Complete

For the respondent to mark the task as completed

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.completeTasksTaskIdCompletePost(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTaskTasksTaskIdDelete

> Object deleteTaskTasksTaskIdDelete(taskId)

Delete Task

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.deleteTaskTasksTaskIdDelete(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadTaskResultsTasksTaskIdDownloadGet

> Object downloadTaskResultsTasksTaskIdDownloadGet(taskId)

Download Task Results

Download results

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.downloadTaskResultsTasksTaskIdDownloadGet(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCoverTasksTaskIdCoverImageGet

> Object getCoverTasksTaskIdCoverImageGet(taskId)

Get Cover

Get cover image

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.getCoverTasksTaskIdCoverImageGet(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgressTasksTaskIdProgressGet

> getProgressTasksTaskIdProgressGet(taskId)

Get Progress

Respondent&#39;s progress within a task, which is the highest index answered question. -1 if no questions have been answered yet.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = null; // Object | 
apiInstance.getProgressTasksTaskIdProgressGet(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | [**Object**](.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaskTasksTaskIdGet

> Task getTaskTasksTaskIdGet(taskId)

Get Task

Get a task based on its task_id

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
apiInstance.getTaskTasksTaskIdGet(taskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchTasksTasksPut

> TaskSearchResponse searchTasksTasksPut(taskSearchRequest)

Search Tasks

Gets the tasks matching the search criteria  Returns: list of &#x60;Task&#x60;s matching the query within the specified &#x60;page&#x60; and &#x60;page_size&#x60;, and total number of &#x60;Task&#x60;s matching the query          The following are all valid search parameters:  &#x60;name&#x60;: name of the task, empty name searches for any task  &#x60;tags&#x60;: keywords that identify the type of task, for example \&quot;object-detection\&quot;  &#x60;requesters&#x60;: username of the requesters who created task, empty searches for any requester  &#x60;credits_min&#x60;, &#x60;credits_max&#x60;: minimum and maximum number of credits rewarded upon task completion; negative &#x60;credits_max&#x60; implies no upper limit  &#x60;questions_min&#x60;, &#x60;questions_max&#x60;: minimum and maximum number of questions in the task; negative &#x60;questions_max&#x60; implies no upper limit  &#x60;page&#x60;: the page; negative value counts backwards, e.g. -1 returns the last page  &#x60;page_size&#x60;: the size of each page; if -1 then &#x60;page&#x60; would not be considered and all results will be returned, e.g.:  - if &#x60;page&#x60; is 2 and &#x60;page_size&#x60; is 10, then it will return the 11th to 20th results, inclusive  - if &#x60;page&#x60; is _ and &#x60;page_size&#x60; is -1, then it will return all the results  - if &#x60;page&#x60; is -1, &#x60;page_size&#x60; is 10, and there are 26 results in total, then it will return the 21st to 26th results, inclusive  &#x60;sort_criteria&#x60;: search parameter that the results should be sorted against  &#x60;sort_ascending&#x60;: True to sort in ascending order, False to sort in descending order

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskSearchRequest = new CrowdLabelApi.TaskSearchRequest(); // TaskSearchRequest | 
apiInstance.searchTasksTasksPut(taskSearchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskSearchRequest** | [**TaskSearchRequest**](TaskSearchRequest.md)|  | 

### Return type

[**TaskSearchResponse**](TaskSearchResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadTaskTasksUploadPost

> [Question] uploadTaskTasksUploadPost(taskFile)

Upload Task

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskFile = "/path/to/file"; // File | 
apiInstance.uploadTaskTasksUploadPost(taskFile, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskFile** | **File**|  | 

### Return type

[**[Question]**](Question.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


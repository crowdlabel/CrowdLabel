# CrowdLabelApi.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claimTaskTasksTaskIdClaimPost**](TasksApi.md#claimTaskTasksTaskIdClaimPost) | **POST** /tasks/{task_id}/claim | Claim Task
[**deleteTaskTasksTaskIdDelete**](TasksApi.md#deleteTaskTasksTaskIdDelete) | **DELETE** /tasks/{task_id} | Delete Task
[**downloadTaskResultsTasksTaskIdDownloadGet**](TasksApi.md#downloadTaskResultsTasksTaskIdDownloadGet) | **GET** /tasks/{task_id}/download | Download Task Results
[**editTaskTasksTaskIdPatch**](TasksApi.md#editTaskTasksTaskIdPatch) | **PATCH** /tasks/{task_id} | Edit Task
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


## editTaskTasksTaskIdPatch

> Object editTaskTasksTaskIdPatch(taskId, opts)

Edit Task

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.TasksApi();
let taskId = 56; // Number | 
let opts = {
  'requestBody': [null] // [Object] | 
};
apiInstance.editTaskTasksTaskIdPatch(taskId, opts, (error, data, response) => {
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
 **requestBody** | [**[Object]**](Object.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTaskTasksTaskIdGet

> Object getTaskTasksTaskIdGet(taskId)

Get Task

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

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchTasksTasksPut

> TaskSearchResponse searchTasksTasksPut(taskSearchRequest)

Search Tasks

Task search

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

> Task uploadTaskTasksUploadPost(taskFile)

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

[**Task**](Task.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


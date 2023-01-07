# CrowdLabelApi.QuestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut**](QuestionsApi.md#createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut) | **PUT** /tasks/{task_id}/questions/{question_id}/answer | Create Answer
[**getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet**](QuestionsApi.md#getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet) | **GET** /tasks/{task_id}/questions/{question_id}/resource | Get Question Resource
[**getQuestionTasksTaskIdQuestionsQuestionIdGet**](QuestionsApi.md#getQuestionTasksTaskIdQuestionsQuestionIdGet) | **GET** /tasks/{task_id}/questions/{question_id} | Get Question



## createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut

> Answer createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut(taskId, questionId, answer1)

Create Answer

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.QuestionsApi();
let taskId = 56; // Number | 
let questionId = 56; // Number | 
let answer1 = new CrowdLabelApi.Answer1(); // Answer1 | 
apiInstance.createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut(taskId, questionId, answer1, (error, data, response) => {
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
 **questionId** | **Number**|  | 
 **answer1** | [**Answer1**](Answer1.md)|  | 

### Return type

[**Answer**](Answer.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet

> Object getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet(taskId, questionId)

Get Question Resource

Get the resource (if any) associated with the question

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.QuestionsApi();
let taskId = 56; // Number | 
let questionId = 56; // Number | 
apiInstance.getQuestionResourceTasksTaskIdQuestionsQuestionIdResourceGet(taskId, questionId, (error, data, response) => {
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
 **questionId** | **Number**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuestionTasksTaskIdQuestionsQuestionIdGet

> Question getQuestionTasksTaskIdQuestionsQuestionIdGet(taskId, questionId)

Get Question

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.QuestionsApi();
let taskId = 56; // Number | 
let questionId = 56; // Number | 
apiInstance.getQuestionTasksTaskIdQuestionsQuestionIdGet(taskId, questionId, (error, data, response) => {
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
 **questionId** | **Number**|  | 

### Return type

[**Question**](Question.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


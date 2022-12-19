# CrowdLabelApi.QuestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut**](QuestionsApi.md#createAnswerTasksTaskIdQuestionsQuestionIdAnswerPut) | **PUT** /tasks/{task_id}/questions/{question_id}/answer | Create Answer
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


## getQuestionTasksTaskIdQuestionsQuestionIdGet

> getQuestionTasksTaskIdQuestionsQuestionIdGet(questionId, taskId, opts)

Get Question

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.QuestionsApi();
let questionId = 56; // Number | 
let taskId = 56; // Number | 
let opts = {
  'requestBody': [null] // [Object] | 
};
apiInstance.getQuestionTasksTaskIdQuestionsQuestionIdGet(questionId, taskId, opts, (error, data, response) => {
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
 **questionId** | **Number**|  | 
 **taskId** | **Number**|  | 
 **requestBody** | [**[Object]**](Object.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


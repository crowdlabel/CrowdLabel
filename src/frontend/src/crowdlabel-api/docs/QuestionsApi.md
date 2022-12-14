# CrowdLabelApi.QuestionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAnswerQuestionsPost**](QuestionsApi.md#createAnswerQuestionsPost) | **POST** /questions | Create Answer
[**getQuestionQuestionsQuestionsQuestionIdGet**](QuestionsApi.md#getQuestionQuestionsQuestionsQuestionIdGet) | **GET** /questions/questions/{question_id} | Get Question



## createAnswerQuestionsPost

> Answer createAnswerQuestionsPost(taskId, questionId, bodyCreateAnswerQuestionsPost)

Create Answer

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.QuestionsApi();
let taskId = 56; // Number | 
let questionId = 56; // Number | 
let bodyCreateAnswerQuestionsPost = new CrowdLabelApi.BodyCreateAnswerQuestionsPost(); // BodyCreateAnswerQuestionsPost | 
apiInstance.createAnswerQuestionsPost(taskId, questionId, bodyCreateAnswerQuestionsPost, (error, data, response) => {
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
 **bodyCreateAnswerQuestionsPost** | [**BodyCreateAnswerQuestionsPost**](BodyCreateAnswerQuestionsPost.md)|  | 

### Return type

[**Answer**](Answer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getQuestionQuestionsQuestionsQuestionIdGet

> getQuestionQuestionsQuestionsQuestionIdGet(questionId, taskId, opts)

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
apiInstance.getQuestionQuestionsQuestionsQuestionIdGet(questionId, taskId, opts, (error, data, response) => {
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


# CrowdLabelApi.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginLoginPost**](AuthApi.md#loginLoginPost) | **POST** /login | Login
[**logoutLogoutPost**](AuthApi.md#logoutLogoutPost) | **POST** /logout | Logout
[**tokenTokenPost**](AuthApi.md#tokenTokenPost) | **POST** /token | Token



## loginLoginPost

> Token loginLoginPost(username, password, opts)

Login

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.AuthApi();
let username = "username_example"; // String | 
let password = "password_example"; // String | 
let opts = {
  'grantType': "grantType_example", // String | 
  'scope': "''", // String | 
  'clientId': "clientId_example", // String | 
  'clientSecret': "clientSecret_example" // String | 
};
apiInstance.loginLoginPost(username, password, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **password** | **String**|  | 
 **grantType** | **String**|  | [optional] 
 **scope** | **String**|  | [optional] [default to &#39;&#39;]
 **clientId** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## logoutLogoutPost

> Object logoutLogoutPost()

Logout

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.AuthApi();
apiInstance.logoutLogoutPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tokenTokenPost

> Token tokenTokenPost(username, password, opts)

Token

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.AuthApi();
let username = "username_example"; // String | 
let password = "password_example"; // String | 
let opts = {
  'grantType': "grantType_example", // String | 
  'scope': "''", // String | 
  'clientId': "clientId_example", // String | 
  'clientSecret': "clientSecret_example" // String | 
};
apiInstance.tokenTokenPost(username, password, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **password** | **String**|  | 
 **grantType** | **String**|  | [optional] 
 **scope** | **String**|  | [optional] [default to &#39;&#39;]
 **clientId** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


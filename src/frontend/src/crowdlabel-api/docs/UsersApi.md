# CrowdLabelApi.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availabilityUsersAvailabilityPut**](UsersApi.md#availabilityUsersAvailabilityPut) | **PUT** /users/availability | Availability
[**editCreditsUsersMeCreditsPost**](UsersApi.md#editCreditsUsersMeCreditsPost) | **POST** /users/me/credits | Edit Credits
[**editMeUsersMePatch**](UsersApi.md#editMeUsersMePatch) | **PATCH** /users/me | Edit Me
[**getMeUsersMeGet**](UsersApi.md#getMeUsersMeGet) | **GET** /users/me | Get Me
[**getPfpUsersMeProfilePictureGet**](UsersApi.md#getPfpUsersMeProfilePictureGet) | **GET** /users/me/profile-picture | Get Pfp
[**getUserUsersUsernameGet**](UsersApi.md#getUserUsersUsernameGet) | **GET** /users/{username} | Get User
[**registerUsersRegisterPost**](UsersApi.md#registerUsersRegisterPost) | **POST** /users/register | Register
[**uploadPfpUsersMeProfilePicturePost**](UsersApi.md#uploadPfpUsersMeProfilePicturePost) | **POST** /users/me/profile-picture | Upload Pfp
[**verifyEmailUsersVerifyEmailPost**](UsersApi.md#verifyEmailUsersVerifyEmailPost) | **POST** /users/verify-email | Verify Email



## availabilityUsersAvailabilityPut

> AvailabilityResponse availabilityUsersAvailabilityPut(availabilityRequest)

Availability

Checks the availability of a username or email. Returns &#x60;true&#x60; for a field if that field is available, &#x60;false&#x60; otherwise.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.UsersApi();
let availabilityRequest = new CrowdLabelApi.AvailabilityRequest(); // AvailabilityRequest | 
apiInstance.availabilityUsersAvailabilityPut(availabilityRequest, (error, data, response) => {
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
 **availabilityRequest** | [**AvailabilityRequest**](AvailabilityRequest.md)|  | 

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## editCreditsUsersMeCreditsPost

> Object editCreditsUsersMeCreditsPost(transactionRequest)

Edit Credits

Adds (positive amount) or subtracts (negative amount) from the credits

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
let transactionRequest = new CrowdLabelApi.TransactionRequest(); // TransactionRequest | 
apiInstance.editCreditsUsersMeCreditsPost(transactionRequest, (error, data, response) => {
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
 **transactionRequest** | [**TransactionRequest**](TransactionRequest.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## editMeUsersMePatch

> Object editMeUsersMePatch(newInfo)

Edit Me

Updates user info

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
let newInfo = new CrowdLabelApi.NewInfo(); // NewInfo | 
apiInstance.editMeUsersMePatch(newInfo, (error, data, response) => {
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
 **newInfo** | [**NewInfo**](NewInfo.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMeUsersMeGet

> ResponseGetMeUsersMeGet getMeUsersMeGet()

Get Me

Gets information for user who sent the request

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
apiInstance.getMeUsersMeGet((error, data, response) => {
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

[**ResponseGetMeUsersMeGet**](ResponseGetMeUsersMeGet.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPfpUsersMeProfilePictureGet

> Object getPfpUsersMeProfilePictureGet()

Get Pfp

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
apiInstance.getPfpUsersMeProfilePictureGet((error, data, response) => {
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


## getUserUsersUsernameGet

> User getUserUsersUsernameGet(username)

Get User

Gets information for the specified username.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
let username = "username_example"; // String | 
apiInstance.getUserUsersUsernameGet(username, (error, data, response) => {
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

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerUsersRegisterPost

> User registerUsersRegisterPost(registrationRequest)

Register

Register for an account. To be called after obtaining a verification code by calling &#x60;/verify-email&#x60;.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.UsersApi();
let registrationRequest = new CrowdLabelApi.RegistrationRequest(); // RegistrationRequest | 
apiInstance.registerUsersRegisterPost(registrationRequest, (error, data, response) => {
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
 **registrationRequest** | [**RegistrationRequest**](RegistrationRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadPfpUsersMeProfilePicturePost

> Object uploadPfpUsersMeProfilePicturePost(profilePicture)

Upload Pfp

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';
let defaultClient = CrowdLabelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2PasswordBearer
let OAuth2PasswordBearer = defaultClient.authentications['OAuth2PasswordBearer'];
OAuth2PasswordBearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CrowdLabelApi.UsersApi();
let profilePicture = "/path/to/file"; // File | 
apiInstance.uploadPfpUsersMeProfilePicturePost(profilePicture, (error, data, response) => {
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
 **profilePicture** | **File**|  | 

### Return type

**Object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## verifyEmailUsersVerifyEmailPost

> Email verifyEmailUsersVerifyEmailPost(email)

Verify Email

Attempts to send an email containing a verification code to the provided address.

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.UsersApi();
let email = new CrowdLabelApi.Email(); // Email | 
apiInstance.verifyEmailUsersVerifyEmailPost(email, (error, data, response) => {
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
 **email** | [**Email**](Email.md)|  | 

### Return type

[**Email**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


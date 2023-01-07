# CrowdLabelApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customSwaggerUiHtmlOpenapiJsonGet**](DefaultApi.md#customSwaggerUiHtmlOpenapiJsonGet) | **GET** /openapi.json | Custom Swagger Ui Html



## customSwaggerUiHtmlOpenapiJsonGet

> Object customSwaggerUiHtmlOpenapiJsonGet()

Custom Swagger Ui Html

### Example

```javascript
import CrowdLabelApi from 'crowd_label_api';

let apiInstance = new CrowdLabelApi.DefaultApi();
apiInstance.customSwaggerUiHtmlOpenapiJsonGet((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


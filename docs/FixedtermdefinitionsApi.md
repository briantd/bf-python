# billforward.FixedtermdefinitionsApi

All URIs are relative to *https://localhost:8080/RestAPI*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fixed_term_definition**](FixedtermdefinitionsApi.md#create_fixed_term_definition) | **POST** /fixed-term-definitions | Create
[**update_fixed_term_definition**](FixedtermdefinitionsApi.md#update_fixed_term_definition) | **PUT** /fixed-term-definitions | Update


# **create_fixed_term_definition**
> FixedTermDefinitionPagedMetadata create_fixed_term_definition(fixed_term_definiton)

Create

{\"nickname\":\"Create a new fixed term definition\",\"request\":\"createFixedTermDefinitionRequest.html\",\"response\":\"createFixedTermDefinitionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.FixedtermdefinitionsApi()
fixed_term_definiton = billforward.MutableBillingEntity() # MutableBillingEntity | The fixed-term-definition object to be updated.

try: 
    # Create
    api_response = api_instance.create_fixed_term_definition(fixed_term_definiton)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FixedtermdefinitionsApi->create_fixed_term_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_term_definiton** | [**MutableBillingEntity**](MutableBillingEntity.md)| The fixed-term-definition object to be updated. | 

### Return type

[**FixedTermDefinitionPagedMetadata**](FixedTermDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fixed_term_definition**
> FixedTermDefinitionPagedMetadata update_fixed_term_definition(fixed_term_definiton)

Update

{\"nickname\":\"Update a fixed-term definition\",\"request\":\"updateFixedTermDefinitionRequest.html\",\"response\":\"updateFixedTermDefinitionResponse.html\"}

### Example 
```python
import time
import billforward
from billforward.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = billforward.FixedtermdefinitionsApi()
fixed_term_definiton = billforward.MutableBillingEntity() # MutableBillingEntity | The fixed-term-definition object to be updated.

try: 
    # Update
    api_response = api_instance.update_fixed_term_definition(fixed_term_definiton)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FixedtermdefinitionsApi->update_fixed_term_definition: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_term_definiton** | [**MutableBillingEntity**](MutableBillingEntity.md)| The fixed-term-definition object to be updated. | 

### Return type

[**FixedTermDefinitionPagedMetadata**](FixedTermDefinitionPagedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/xml, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


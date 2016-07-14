# coding: utf-8

"""
    BillForward REST API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CouponruleApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_coupon_rule(self, coupon_rule, **kwargs):
        """
        Create a coupon-rule.
        {\"nickname\":\"Create a new rule\", \"request\" : \"createCouponRuleRequest.html\" ,\"response\" : \"createCouponRuleResponse.html\" }

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_coupon_rule(coupon_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CouponRule coupon_rule: The coupon-rule object to be created. (required)
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_coupon_rule_with_http_info(coupon_rule, **kwargs)
        else:
            (data) = self.create_coupon_rule_with_http_info(coupon_rule, **kwargs)
            return data

    def create_coupon_rule_with_http_info(self, coupon_rule, **kwargs):
        """
        Create a coupon-rule.
        {\"nickname\":\"Create a new rule\", \"request\" : \"createCouponRuleRequest.html\" ,\"response\" : \"createCouponRuleResponse.html\" }

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_coupon_rule_with_http_info(coupon_rule, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CouponRule coupon_rule: The coupon-rule object to be created. (required)
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_coupon_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coupon_rule' is set
        if ('coupon_rule' not in params) or (params['coupon_rule'] is None):
            raise ValueError("Missing the required parameter `coupon_rule` when calling `create_coupon_rule`")

        resource_path = '/coupon-rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'coupon_rule' in params:
            body_params = params['coupon_rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/xml', 'application/xml', 'application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CouponRulePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_coupon_rule(self, coupon_rule_id, **kwargs):
        """
        Retire a coupon-rule, specified by the coupon-rule-ID parameter.
        {\"nickname\":\"Delete a rule\",\"response\" : \"deleteCouponRuleByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_coupon_rule(coupon_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_rule_id: ID of the coupon-rule. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_coupon_rule_with_http_info(coupon_rule_id, **kwargs)
        else:
            (data) = self.delete_coupon_rule_with_http_info(coupon_rule_id, **kwargs)
            return data

    def delete_coupon_rule_with_http_info(self, coupon_rule_id, **kwargs):
        """
        Retire a coupon-rule, specified by the coupon-rule-ID parameter.
        {\"nickname\":\"Delete a rule\",\"response\" : \"deleteCouponRuleByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_coupon_rule_with_http_info(coupon_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_rule_id: ID of the coupon-rule. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_rule_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_coupon_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coupon_rule_id' is set
        if ('coupon_rule_id' not in params) or (params['coupon_rule_id'] is None):
            raise ValueError("Missing the required parameter `coupon_rule_id` when calling `delete_coupon_rule`")

        resource_path = '/coupon-rules/{coupon-rule-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'coupon_rule_id' in params:
            path_params['coupon-rule-ID'] = params['coupon_rule_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CouponRulePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_coupon_rules(self, **kwargs):
        """
        Returns a collection of coupon-rules. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all rules\",\"response\" : \"getCouponRuleAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_coupon_rules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first product-rate-plan to return.
        :param int records: The maximum number of product-rate-plans to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_coupon_rules_with_http_info(**kwargs)
        else:
            (data) = self.get_all_coupon_rules_with_http_info(**kwargs)
            return data

    def get_all_coupon_rules_with_http_info(self, **kwargs):
        """
        Returns a collection of coupon-rules. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all rules\",\"response\" : \"getCouponRuleAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_coupon_rules_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first product-rate-plan to return.
        :param int records: The maximum number of product-rate-plans to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_coupon_rules" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/coupon-rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'records' in params:
            query_params['records'] = params['records']
        if 'order_by' in params:
            query_params['order_by'] = params['order_by']
        if 'order' in params:
            query_params['order'] = params['order']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CouponRulePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_coupon_rule_by_coupon_definition_id(self, coupon_definition_id, **kwargs):
        """
        Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
        {\"nickname\":\"Retrieve by coupon definition\",\"response\" : \"getCouponRuleByCouponDefinitionID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_coupon_rule_by_coupon_definition_id(coupon_definition_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_definition_id: ID of the coupon-definition. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_coupon_rule_by_coupon_definition_id_with_http_info(coupon_definition_id, **kwargs)
        else:
            (data) = self.get_coupon_rule_by_coupon_definition_id_with_http_info(coupon_definition_id, **kwargs)
            return data

    def get_coupon_rule_by_coupon_definition_id_with_http_info(self, coupon_definition_id, **kwargs):
        """
        Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
        {\"nickname\":\"Retrieve by coupon definition\",\"response\" : \"getCouponRuleByCouponDefinitionID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_coupon_rule_by_coupon_definition_id_with_http_info(coupon_definition_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_definition_id: ID of the coupon-definition. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_definition_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_coupon_rule_by_coupon_definition_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coupon_definition_id' is set
        if ('coupon_definition_id' not in params) or (params['coupon_definition_id'] is None):
            raise ValueError("Missing the required parameter `coupon_definition_id` when calling `get_coupon_rule_by_coupon_definition_id`")

        resource_path = '/coupon-rules/coupon-definition/{coupon-definition-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'coupon_definition_id' in params:
            path_params['coupon-definition-ID'] = params['coupon_definition_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CouponRulePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_coupon_rule_by_id(self, coupon_rule_id, **kwargs):
        """
        Returns a single coupon-rule, specified by the coupon-rule-ID parameter.
        {\"nickname\":\"Retrieve an existing rule\",\"response\" : \"getCouponRuleByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_coupon_rule_by_id(coupon_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_rule_id: ID of the coupon-rule. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_coupon_rule_by_id_with_http_info(coupon_rule_id, **kwargs)
        else:
            (data) = self.get_coupon_rule_by_id_with_http_info(coupon_rule_id, **kwargs)
            return data

    def get_coupon_rule_by_id_with_http_info(self, coupon_rule_id, **kwargs):
        """
        Returns a single coupon-rule, specified by the coupon-rule-ID parameter.
        {\"nickname\":\"Retrieve an existing rule\",\"response\" : \"getCouponRuleByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_coupon_rule_by_id_with_http_info(coupon_rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_rule_id: ID of the coupon-rule. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: CouponRulePagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_rule_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_coupon_rule_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coupon_rule_id' is set
        if ('coupon_rule_id' not in params) or (params['coupon_rule_id'] is None):
            raise ValueError("Missing the required parameter `coupon_rule_id` when calling `get_coupon_rule_by_id`")

        resource_path = '/coupon-rules/{coupon-rule-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'coupon_rule_id' in params:
            path_params['coupon-rule-ID'] = params['coupon_rule_id']

        query_params = {}
        if 'organizations' in params:
            query_params['organizations'] = params['organizations']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CouponRulePagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
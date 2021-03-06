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


class FixedtermsApi(object):
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

    def update_fixed_term(self, payment_method, **kwargs):
        """
        Update
        {\"nickname\":\"Update a fixed term\",\"request\":\"updateFixedTermRequest.html\",\"response\":\"updateFixedTermResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_fixed_term(payment_method, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FixedTerm payment_method: The payment-method object to be updated. (required)
        :return: FixedTermPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_fixed_term_with_http_info(payment_method, **kwargs)
        else:
            (data) = self.update_fixed_term_with_http_info(payment_method, **kwargs)
            return data

    def update_fixed_term_with_http_info(self, payment_method, **kwargs):
        """
        Update
        {\"nickname\":\"Update a fixed term\",\"request\":\"updateFixedTermRequest.html\",\"response\":\"updateFixedTermResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_fixed_term_with_http_info(payment_method, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FixedTerm payment_method: The payment-method object to be updated. (required)
        :return: FixedTermPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_method']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fixed_term" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_method' is set
        if ('payment_method' not in params) or (params['payment_method'] is None):
            raise ValueError("Missing the required parameter `payment_method` when calling `update_fixed_term`")

        resource_path = '/fixed-terms'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_method' in params:
            body_params = params['payment_method']

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

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FixedTermPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

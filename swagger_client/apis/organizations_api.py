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


class OrganizationsApi(object):
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

    def create_organization(self, organization, **kwargs):
        """
        Create an organization.
        {\"nickname\":\"Create\",\"request\":\"createOrganizationRequest.html\",\"response\":\"createOrganizationResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_organization(organization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Organization organization: The organization object to be updated. (required)
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_organization_with_http_info(organization, **kwargs)
        else:
            (data) = self.create_organization_with_http_info(organization, **kwargs)
            return data

    def create_organization_with_http_info(self, organization, **kwargs):
        """
        Create an organization.
        {\"nickname\":\"Create\",\"request\":\"createOrganizationRequest.html\",\"response\":\"createOrganizationResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_organization_with_http_info(organization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Organization organization: The organization object to be updated. (required)
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params) or (params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `create_organization`")

        resource_path = '/organizations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'organization' in params:
            body_params = params['organization']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_my_organizations(self, **kwargs):
        """
        Returns a collection of all my asociated organizations. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get Mine\",\"response\":\"getOrganizationAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_my_organizations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first organization to return.
        :param int records: The maximum number of organizations to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_my_organizations_with_http_info(**kwargs)
        else:
            (data) = self.get_all_my_organizations_with_http_info(**kwargs)
            return data

    def get_all_my_organizations_with_http_info(self, **kwargs):
        """
        Returns a collection of all my asociated organizations. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get Mine\",\"response\":\"getOrganizationAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_my_organizations_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first organization to return.
        :param int records: The maximum number of organizations to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_my_organizations" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/organizations/mine'.replace('{format}', 'json')
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
        if 'include_retired' in params:
            query_params['include_retired'] = params['include_retired']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_organizations(self, **kwargs):
        """
        Returns a collection of all organizations. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get All\",\"response\":\"getOrganizationAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_organizations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first organization to return.
        :param int records: The maximum number of organizations to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_organizations_with_http_info(**kwargs)
        else:
            (data) = self.get_all_organizations_with_http_info(**kwargs)
            return data

    def get_all_organizations_with_http_info(self, **kwargs):
        """
        Returns a collection of all organizations. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get All\",\"response\":\"getOrganizationAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_organizations_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first organization to return.
        :param int records: The maximum number of organizations to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_organizations" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/organizations'.replace('{format}', 'json')
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
        if 'include_retired' in params:
            query_params['include_retired'] = params['include_retired']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_organization_by_customer_code(self, customer_code, **kwargs):
        """
        Returns a single organization, specified by the customer-code parameter.
        {\"nickname\":\"Retrieve by Customer-Code\",\"response\":\"getOrganizationByCustomer.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_customer_code(customer_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customer_code: The unique customer code of the organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_organization_by_customer_code_with_http_info(customer_code, **kwargs)
        else:
            (data) = self.get_organization_by_customer_code_with_http_info(customer_code, **kwargs)
            return data

    def get_organization_by_customer_code_with_http_info(self, customer_code, **kwargs):
        """
        Returns a single organization, specified by the customer-code parameter.
        {\"nickname\":\"Retrieve by Customer-Code\",\"response\":\"getOrganizationByCustomer.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_customer_code_with_http_info(customer_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customer_code: The unique customer code of the organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_code', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization_by_customer_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_code' is set
        if ('customer_code' not in params) or (params['customer_code'] is None):
            raise ValueError("Missing the required parameter `customer_code` when calling `get_organization_by_customer_code`")

        resource_path = '/organizations/customer-code/{customer-code}'.replace('{format}', 'json')
        path_params = {}
        if 'customer_code' in params:
            path_params['customer-code'] = params['customer_code']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_organization_by_id(self, organization_id, **kwargs):
        """
        Returns a single Organization, specified by the organization-ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getOrganizationByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_id(organization_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: ID of the organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_organization_by_id_with_http_info(organization_id, **kwargs)
        else:
            (data) = self.get_organization_by_id_with_http_info(organization_id, **kwargs)
            return data

    def get_organization_by_id_with_http_info(self, organization_id, **kwargs):
        """
        Returns a single Organization, specified by the organization-ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getOrganizationByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_id_with_http_info(organization_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str organization_id: ID of the organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in params) or (params['organization_id'] is None):
            raise ValueError("Missing the required parameter `organization_id` when calling `get_organization_by_id`")

        resource_path = '/organizations/{organization-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'organization_id' in params:
            path_params['organization-ID'] = params['organization_id']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_organization_by_name(self, name, **kwargs):
        """
        Returns a single Organization, specified by the name parameter.
        {\"nickname\":\"Retrieve by Name\",\"response\":\"getOrganizationByName.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_name(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The name of the Organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_organization_by_name_with_http_info(name, **kwargs)
        else:
            (data) = self.get_organization_by_name_with_http_info(name, **kwargs)
            return data

    def get_organization_by_name_with_http_info(self, name, **kwargs):
        """
        Returns a single Organization, specified by the name parameter.
        {\"nickname\":\"Retrieve by Name\",\"response\":\"getOrganizationByName.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_organization_by_name_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The name of the Organization. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_organization_by_name`")

        resource_path = '/organizations/name/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_organization(self, organization, **kwargs):
        """
        Update an organization.
        {\"nickname\":\"Updated\",\"request\":\"updateOrganizationRequest.html\",\"response\":\"updateOrganizationResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_organization(organization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Organization organization: The organization object to be updated. (required)
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_organization_with_http_info(organization, **kwargs)
        else:
            (data) = self.update_organization_with_http_info(organization, **kwargs)
            return data

    def update_organization_with_http_info(self, organization, **kwargs):
        """
        Update an organization.
        {\"nickname\":\"Updated\",\"request\":\"updateOrganizationRequest.html\",\"response\":\"updateOrganizationResponse.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_organization_with_http_info(organization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Organization organization: The organization object to be updated. (required)
        :return: OrganizationPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params) or (params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `update_organization`")

        resource_path = '/organizations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'organization' in params:
            body_params = params['organization']

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
                                            response_type='OrganizationPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
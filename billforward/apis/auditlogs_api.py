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


class AuditlogsApi(object):
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

    def get_all_audit_entries(self, **kwargs):
        """
        Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all\",\"response\":\"getAuditAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_audit_entries(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first audit-log entry to return.
        :param int records: The maximum number of audit-log entry to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_audit_entries_with_http_info(**kwargs)
        else:
            (data) = self.get_all_audit_entries_with_http_info(**kwargs)
            return data

    def get_all_audit_entries_with_http_info(self, **kwargs):
        """
        Returns a collection of all audit-log objects. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Get all\",\"response\":\"getAuditAll.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_audit_entries_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first audit-log entry to return.
        :param int records: The maximum number of audit-log entry to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
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
                    " to method get_all_audit_entries" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/audit-logs'.replace('{format}', 'json')
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
                                            response_type='AuditEntryPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_audit_entries_by_created_date(self, lower_threshold, upper_threshold, **kwargs):
        """
        Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by created time\",\"response\":\"getAuditByCreated.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entries_by_created_date(lower_threshold, upper_threshold, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str lower_threshold: The UTC DateTime specifying the start of the result period. (required)
        :param str upper_threshold: The UTC DateTime specifying the end of the result period. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first audit-log entry to return.
        :param int records: The maximum number of audit-log entry to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_entries_by_created_date_with_http_info(lower_threshold, upper_threshold, **kwargs)
        else:
            (data) = self.get_audit_entries_by_created_date_with_http_info(lower_threshold, upper_threshold, **kwargs)
            return data

    def get_audit_entries_by_created_date_with_http_info(self, lower_threshold, upper_threshold, **kwargs):
        """
        Returns a collection of audit-log objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by created time\",\"response\":\"getAuditByCreated.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entries_by_created_date_with_http_info(lower_threshold, upper_threshold, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str lower_threshold: The UTC DateTime specifying the start of the result period. (required)
        :param str upper_threshold: The UTC DateTime specifying the end of the result period. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first audit-log entry to return.
        :param int records: The maximum number of audit-log entry to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lower_threshold', 'upper_threshold', 'organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_entries_by_created_date" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lower_threshold' is set
        if ('lower_threshold' not in params) or (params['lower_threshold'] is None):
            raise ValueError("Missing the required parameter `lower_threshold` when calling `get_audit_entries_by_created_date`")
        # verify the required parameter 'upper_threshold' is set
        if ('upper_threshold' not in params) or (params['upper_threshold'] is None):
            raise ValueError("Missing the required parameter `upper_threshold` when calling `get_audit_entries_by_created_date`")

        resource_path = '/audit-logs/created/{lower-threshold}/{upper-threshold}'.replace('{format}', 'json')
        path_params = {}
        if 'lower_threshold' in params:
            path_params['lower-threshold'] = params['lower_threshold']
        if 'upper_threshold' in params:
            path_params['upper-threshold'] = params['upper_threshold']

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
                                            response_type='AuditEntryPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_audit_entry_by_entity_id(self, entity_id, **kwargs):
        """
        Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by entity-ID\",\"response\":\"getAuditByEntityID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_entity_id(entity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: The string ID of the entity whose changes are documented by the audit log. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first account to return.
        :param int records: The maximum number of accounts to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_entry_by_entity_id_with_http_info(entity_id, **kwargs)
        else:
            (data) = self.get_audit_entry_by_entity_id_with_http_info(entity_id, **kwargs)
            return data

    def get_audit_entry_by_entity_id_with_http_info(self, entity_id, **kwargs):
        """
        Returns a collection of audit-log entries, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by entity-ID\",\"response\":\"getAuditByEntityID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_entity_id_with_http_info(entity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_id: The string ID of the entity whose changes are documented by the audit log. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first account to return.
        :param int records: The maximum number of accounts to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_entry_by_entity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_audit_entry_by_entity_id`")

        resource_path = '/audit-logs/entity/{entity-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'entity_id' in params:
            path_params['entity-ID'] = params['entity_id']

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
                                            response_type='AuditEntryPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_audit_entry_by_entity_type(self, entity_type, **kwargs):
        """
        Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by entity type\",\"response\":\"getAuditByEntityType.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_entity_type(entity_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_type: The type of the entity whose changes are documented by the audit log. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first account to return.
        :param int records: The maximum number of accounts to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_entry_by_entity_type_with_http_info(entity_type, **kwargs)
        else:
            (data) = self.get_audit_entry_by_entity_type_with_http_info(entity_type, **kwargs)
            return data

    def get_audit_entry_by_entity_type_with_http_info(self, entity_type, **kwargs):
        """
        Returns a collection of audit-log entries, specified by the entity-type parameter. By default 10 values are returned. Records are returned in natural order.
        {\"nickname\":\"Retrieve by entity type\",\"response\":\"getAuditByEntityType.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_entity_type_with_http_info(entity_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entity_type: The type of the entity whose changes are documented by the audit log. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls.
        :param int offset: The offset from the first account to return.
        :param int records: The maximum number of accounts to return.
        :param str order_by: Specify a field used to order the result set.
        :param str order: Ihe direction of any ordering, either ASC or DESC.
        :param bool include_retired: Whether retired products should be returned.
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'organizations', 'offset', 'records', 'order_by', 'order', 'include_retired']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_entry_by_entity_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params) or (params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_audit_entry_by_entity_type`")

        resource_path = '/audit-logs/entity-type/{entity-type}'.replace('{format}', 'json')
        path_params = {}
        if 'entity_type' in params:
            path_params['entity-type'] = params['entity_type']

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
                                            response_type='AuditEntryPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_audit_entry_by_id(self, audit_id, **kwargs):
        """
        Returns a single audit-log entry, specified by the audit-ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getAuditByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_id(audit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str audit_id: The string ID of the audit-log entry. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls. Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_entry_by_id_with_http_info(audit_id, **kwargs)
        else:
            (data) = self.get_audit_entry_by_id_with_http_info(audit_id, **kwargs)
            return data

    def get_audit_entry_by_id_with_http_info(self, audit_id, **kwargs):
        """
        Returns a single audit-log entry, specified by the audit-ID parameter.
        {\"nickname\":\"Retrieve by id\",\"response\":\"getAuditByID.html\"}

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_entry_by_id_with_http_info(audit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str audit_id: The string ID of the audit-log entry. (required)
        :param list[str] organizations: A list of organization-IDs used to restrict the scope of API calls. Multiple organization-IDs may be specified by repeated use of the query parameter. Example: ...&organizations=org1&organizations=org2
        :return: AuditEntryPagedMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['audit_id', 'organizations']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_entry_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'audit_id' is set
        if ('audit_id' not in params) or (params['audit_id'] is None):
            raise ValueError("Missing the required parameter `audit_id` when calling `get_audit_entry_by_id`")

        resource_path = '/audit-logs/{audit-ID}'.replace('{format}', 'json')
        path_params = {}
        if 'audit_id' in params:
            path_params['audit-ID'] = params['audit_id']

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
                                            response_type='AuditEntryPagedMetadata',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
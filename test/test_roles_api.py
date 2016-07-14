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

import os
import sys
import unittest

import billforward
from billforward.rest import ApiException
from billforward.apis.roles_api import RolesApi


class TestRolesApi(unittest.TestCase):
    """ RolesApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.roles_api.RolesApi()

    def tearDown(self):
        pass

    def test_create_role(self):
        """
        Test case for create_role

        Create a new role.
        """
        pass

    def test_get_all_roles(self):
        """
        Test case for get_all_roles

        Retrieves a collection of all roles. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_role_by_id(self):
        """
        Test case for get_role_by_id

        Retrieves a single role, specified by the ID parameter.
        """
        pass

    def test_remove_permission_from_role(self):
        """
        Test case for remove_permission_from_role

        Revokes a particular permission
        """
        pass

    def test_revoke_role(self):
        """
        Test case for revoke_role

        Revokes a role
        """
        pass

    def test_update_role(self):
        """
        Test case for update_role

        Update a role.
        """
        pass


if __name__ == '__main__':
    unittest.main()

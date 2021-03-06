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
from billforward.apis.coupondefinition_api import CoupondefinitionApi


class TestCoupondefinitionApi(unittest.TestCase):
    """ CoupondefinitionApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.coupondefinition_api.CoupondefinitionApi()

    def tearDown(self):
        pass

    def test_create_coupon_definition(self):
        """
        Test case for create_coupon_definition

        Create a coupon-definition.
        """
        pass

    def test_delete_coupon_definition(self):
        """
        Test case for delete_coupon_definition

        Retire a coupon-definition, specified by the coupon-definition-ID parameter.
        """
        pass

    def test_get_all_coupon_definitions(self):
        """
        Test case for get_all_coupon_definitions

        Returns a collection of coupon-definitions. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_coupon_definition_by_id(self):
        """
        Test case for get_coupon_definition_by_id

        Returns a single coupon-definition, specified by the coupon-definition-ID parameter.
        """
        pass

    def test_update_coupon_definition(self):
        """
        Test case for update_coupon_definition

        Update a coupon-definition.
        """
        pass


if __name__ == '__main__':
    unittest.main()

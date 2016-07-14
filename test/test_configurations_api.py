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
from billforward.apis.configurations_api import ConfigurationsApi


class TestConfigurationsApi(unittest.TestCase):
    """ ConfigurationsApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.configurations_api.ConfigurationsApi()

    def tearDown(self):
        pass

    def test_create_api_configuration(self):
        """
        Test case for create_api_configuration

        Create a configuration.
        """
        pass

    def test_get_all_api_configurations(self):
        """
        Test case for get_all_api_configurations

        Returns a collection of configurations. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_api_configurations_by_type(self):
        """
        Test case for get_api_configurations_by_type

        Returns a single configuration, specified by the type parameter.
        """
        pass

    def test_update_api_configuration(self):
        """
        Test case for update_api_configuration

        Update a configuration.
        """
        pass


if __name__ == '__main__':
    unittest.main()

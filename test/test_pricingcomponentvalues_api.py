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
from billforward.apis.pricingcomponentvalues_api import PricingcomponentvaluesApi


class TestPricingcomponentvaluesApi(unittest.TestCase):
    """ PricingcomponentvaluesApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.pricingcomponentvalues_api.PricingcomponentvaluesApi()

    def tearDown(self):
        pass

    def test_create_pricing_component_value(self):
        """
        Test case for create_pricing_component_value

        Create a pricing-component-value.
        """
        pass

    def test_get_all_pricing_component_values(self):
        """
        Test case for get_all_pricing_component_values

        Returns a collection of pricing-component-values.By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_pricing_component_value(self):
        """
        Test case for get_pricing_component_value

        Returns a collection of pricing-component-values, specified by the pricing-component-ID parameter.By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_pricing_component_value_by_subscription_id(self):
        """
        Test case for get_pricing_component_value_by_subscription_id

        Returns a collection of pricing-component-values, specified by the subscription-ID parameter.By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_update_pricing_component_value(self):
        """
        Test case for update_pricing_component_value

        Update a pricing-component-value.
        """
        pass


if __name__ == '__main__':
    unittest.main()

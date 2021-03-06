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
from billforward.apis.productrateplans_api import ProductrateplansApi


class TestProductrateplansApi(unittest.TestCase):
    """ ProductrateplansApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.productrateplans_api.ProductrateplansApi()

    def tearDown(self):
        pass

    def test_add_taxation_strategy_to_rate_plan(self):
        """
        Test case for add_taxation_strategy_to_rate_plan

        Adds or re-enables the specified taxation-strategy for the given product-rate-plan.
        """
        pass

    def test_create_rate_plan(self):
        """
        Test case for create_rate_plan

        Create a new rate-plan.
        """
        pass

    def test_delete_metadata_for_rate_plan(self):
        """
        Test case for delete_metadata_for_rate_plan

        Remove any associated metadata.
        """
        pass

    def test_get_all_rate_plans(self):
        """
        Test case for get_all_rate_plans

        Returns a collection of product-rate-plans. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_available_taxation_strategies_for_rate_plan(self):
        """
        Test case for get_available_taxation_strategies_for_rate_plan

        Returns all available taxes for the specified product-rate-plan. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_metadata_for_rate_plan(self):
        """
        Test case for get_metadata_for_rate_plan

        Retrieve any associated metadata.
        """
        pass

    def test_get_product_rate_plan_by_id(self):
        """
        Test case for get_product_rate_plan_by_id

        Returns product-rate-plans, specified by the product-rate-plan id or name.
        """
        pass

    def test_get_rate_plan_by_product(self):
        """
        Test case for get_rate_plan_by_product

        Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_rate_plan_by_product_and_rate_plan(self):
        """
        Test case for get_rate_plan_by_product_and_rate_plan

        Returns a collection of product-rate-plans, specified by the product-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_remove_taxation_strategy_from_rate_plan(self):
        """
        Test case for remove_taxation_strategy_from_rate_plan

        Removes the specified taxation-strategy for the given product-rate-plan.
        """
        pass

    def test_retire_rate_plan(self):
        """
        Test case for retire_rate_plan

        Retires the product-rate-plan specified product-rate-plan-ID.
        """
        pass

    def test_set_metadata_for_rate_plan(self):
        """
        Test case for set_metadata_for_rate_plan

        Remove any existing metadata keys and create the provided data.
        """
        pass

    def test_update_rate_plan(self):
        """
        Test case for update_rate_plan

        Update a rate-plan.
        """
        pass

    def test_upsert_metadata_for_rate_plan(self):
        """
        Test case for upsert_metadata_for_rate_plan

        Update any existing metadata key-values and insert any new key-values, no keys will be removed.
        """
        pass


if __name__ == '__main__':
    unittest.main()

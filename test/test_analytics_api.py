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
from billforward.apis.analytics_api import AnalyticsApi


class TestAnalyticsApi(unittest.TestCase):
    """ AnalyticsApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.analytics_api.AnalyticsApi()

    def tearDown(self):
        pass

    def test_get_account_debts(self):
        """
        Test case for get_account_debts

        Gets outstanding debts per account, within a date range.
        """
        pass

    def test_get_account_ltv(self):
        """
        Test case for get_account_ltv

        Gets an account's life-time value, as of a given end date.
        """
        pass

    def test_get_account_payments(self):
        """
        Test case for get_account_payments

        Gets hourly payments per product, within a date range.
        """
        pass

    def test_get_billforward_managed_payments(self):
        """
        Test case for get_billforward_managed_payments

        Gets all payments managed by BillForward, within a date range.
        """
        pass

    def test_get_churn(self):
        """
        Test case for get_churn

        Gets churn, within a date range.
        """
        pass

    def test_get_debts(self):
        """
        Test case for get_debts

        Gets debts within a date range.
        """
        pass

    def test_get_payments(self):
        """
        Test case for get_payments

        Gets payments within a date range.
        """
        pass

    def test_get_product_payments(self):
        """
        Test case for get_product_payments

        Gets hourly payments per product, within a date range.
        """
        pass

    def test_get_product_rate_plan_payments(self):
        """
        Test case for get_product_rate_plan_payments

        Gets hourly payments per product, within a date range.
        """
        pass

    def test_get_subscription_ltv(self):
        """
        Test case for get_subscription_ltv

        Gets a subscription's life-time value, as of a given end date.
        """
        pass

    def test_get_upgrades(self):
        """
        Test case for get_upgrades

        Gets upgrades, within a date range.
        """
        pass


if __name__ == '__main__':
    unittest.main()

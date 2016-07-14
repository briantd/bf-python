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
from billforward.apis.charges_api import ChargesApi


class TestChargesApi(unittest.TestCase):
    """ ChargesApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.charges_api.ChargesApi()

    def tearDown(self):
        pass

    def test_get_all_subscription_charges(self):
        """
        Test case for get_all_subscription_charges

        Retrieves a collection of all charges. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_subscription_charge_by_account_id(self):
        """
        Test case for get_subscription_charge_by_account_id

        Retrieves a collection of charges, specified by the account-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_subscription_charge_by_id(self):
        """
        Test case for get_subscription_charge_by_id

        Retrieves a single charge, specified by the charge-id parameter.
        """
        pass

    def test_get_subscription_charge_by_state(self):
        """
        Test case for get_subscription_charge_by_state

        Retrieves a collection of charges, specified by the state parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_subscription_charge_by_version_id(self):
        """
        Test case for get_subscription_charge_by_version_id

        Retrieves a single charge, specified by the version-ID parameter.
        """
        pass

    def test_recalculate_subscription_charge(self):
        """
        Test case for recalculate_subscription_charge

        Recalculate a charge.
        """
        pass

    def test_void_subscription_charge(self):
        """
        Test case for void_subscription_charge

        Void the charge with the specified charge-ID.
        """
        pass


if __name__ == '__main__':
    unittest.main()

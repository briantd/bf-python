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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """ WebhooksApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.webhooks_api.WebhooksApi()

    def tearDown(self):
        pass

    def test_create_webhook(self):
        """
        Test case for create_webhook

        Create a webhook.
        """
        pass

    def test_create_webhook_v2(self):
        """
        Test case for create_webhook_v2

        Create a webhook.
        """
        pass

    def test_get_all_webhooks(self):
        """
        Test case for get_all_webhooks

        Returns a collection of Webhooks, specified by the accountID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_webhook_by_id(self):
        """
        Test case for get_webhook_by_id

        Returns a single webhook, specified by the webhook-ID parameter.
        """
        pass

    def test_retire_webhook(self):
        """
        Test case for retire_webhook

        Retires the specified webhook.
        """
        pass

    def test_update_webhook(self):
        """
        Test case for update_webhook

        Update a webhook.
        """
        pass

    def test_verify_webhook(self):
        """
        Test case for verify_webhook

        New webhooks must be verified before use, use the verificationID of the webhook to perform verification.
        """
        pass


if __name__ == '__main__':
    unittest.main()
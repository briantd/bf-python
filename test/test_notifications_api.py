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
from billforward.apis.notifications_api import NotificationsApi


class TestNotificationsApi(unittest.TestCase):
    """ NotificationsApi unit test stubs """

    def setUp(self):
        self.api = billforward.apis.notifications_api.NotificationsApi()

    def tearDown(self):
        pass

    def test_ack_notification(self):
        """
        Test case for ack_notification

        Acknowledge a newly recevied notification.
        """
        pass

    def test_get_all_notifications(self):
        """
        Test case for get_all_notifications

        Returns a collection of all notifications. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_notification_by_entity_id(self):
        """
        Test case for get_notification_by_entity_id

        Returns a collection of notifications, specified by the entity-ID parameter. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_notification_by_id(self):
        """
        Test case for get_notification_by_id

        Returns a single notification, specified by the notification-ID parameter.
        """
        pass

    def test_get_notifications_by_webhook_id(self):
        """
        Test case for get_notifications_by_webhook_id

        Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters for the given webhook id. By default 10 values are returned. Records are returned in natural order.
        """
        pass

    def test_get_notifications_within_date_range(self):
        """
        Test case for get_notifications_within_date_range

        Returns a collection of notification objects with created times within the period specified by the lower-threshold and upper-threshold parameters. By default 10 values are returned. Records are returned in natural order.
        """
        pass


if __name__ == '__main__':
    unittest.main()

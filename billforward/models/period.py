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

from pprint import pformat
from six import iteritems
import re


class Period(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, subscription_id=None, organization_id=None, invoice_id=None, state=None, period=None, start=None, stop=None, usage_type=None):
        """
        Period - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'subscription_id': 'str',
            'organization_id': 'str',
            'invoice_id': 'str',
            'state': 'str',
            'period': 'int',
            'start': 'datetime',
            'stop': 'datetime',
            'usage_type': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'subscription_id': 'subscriptionID',
            'organization_id': 'organizationID',
            'invoice_id': 'invoiceID',
            'state': 'state',
            'period': 'period',
            'start': 'start',
            'stop': 'stop',
            'usage_type': 'usageType'
        }

        self._created = created
        self._subscription_id = subscription_id
        self._organization_id = organization_id
        self._invoice_id = invoice_id
        self._state = state
        self._period = period
        self._start = start
        self._stop = stop
        self._usage_type = usage_type

    @property
    def created(self):
        """
        Gets the created of this Period.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this Period.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Period.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this Period.
        :type: datetime
        """

        self._created = created

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this Period.
        { \"description\" : \"ID of the subscription to which this billing period pertains.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The subscription_id of this Period.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this Period.
        { \"description\" : \"ID of the subscription to which this billing period pertains.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param subscription_id: The subscription_id of this Period.
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Period.
        { \"description\" : \"Organization associated with this billing period.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The organization_id of this Period.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Period.
        { \"description\" : \"Organization associated with this billing period.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param organization_id: The organization_id of this Period.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this Period.


        :return: The invoice_id of this Period.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this Period.


        :param invoice_id: The invoice_id of this Period.
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def state(self):
        """
        Gets the state of this Period.
        { \"description\" : \"The current state of this billing period. Initially a period is '\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }ACTIVE_STATE'. Once the 'stop' date is passed, the billing period becomes HISTORIC_STATE.

        :return: The state of this Period.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Period.
        { \"description\" : \"The current state of this billing period. Initially a period is '\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }ACTIVE_STATE'. Once the 'stop' date is passed, the billing period becomes HISTORIC_STATE.

        :param state: The state of this Period.
        :type: str
        """
        allowed_values = ["Active", "Historic"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def period(self):
        """
        Gets the period of this Period.
        { \"description\" : \"The incarnation of the subscription to which this billing period refers. The first incarnation of the subscription is in 'period 0'. A recurring subscription may enter 'period 1' and further.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The period of this Period.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this Period.
        { \"description\" : \"The incarnation of the subscription to which this billing period refers. The first incarnation of the subscription is in 'period 0'. A recurring subscription may enter 'period 1' and further.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param period: The period of this Period.
        :type: int
        """

        self._period = period

    @property
    def start(self):
        """
        Gets the start of this Period.
        { \"description\" : \"The start date of this billing period, UTC DateTime\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The start of this Period.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this Period.
        { \"description\" : \"The start date of this billing period, UTC DateTime\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param start: The start of this Period.
        :type: datetime
        """

        self._start = start

    @property
    def stop(self):
        """
        Gets the stop of this Period.
        { \"description\" : \"The end date of this billing period, UTC DateTime\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The stop of this Period.
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """
        Sets the stop of this Period.
        { \"description\" : \"The end date of this billing period, UTC DateTime\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param stop: The stop of this Period.
        :type: datetime
        """

        self._stop = stop

    @property
    def usage_type(self):
        """
        Gets the usage_type of this Period.
        { \"description\" : \"The type of usage measured within this billing period. Options are '\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }Temporal which refers to time-based usage and Itemized, which refers to one-off usages.

        :return: The usage_type of this Period.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """
        Sets the usage_type of this Period.
        { \"description\" : \"The type of usage measured within this billing period. Options are '\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }Temporal which refers to time-based usage and Itemized, which refers to one-off usages.

        :param usage_type: The usage_type of this Period.
        :type: str
        """
        allowed_values = ["Temporal", "Itemized"]
        if usage_type not in allowed_values:
            raise ValueError(
                "Invalid value for `usage_type` ({0}), must be one of {1}"
                .format(usage_type, allowed_values)
            )

        self._usage_type = usage_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
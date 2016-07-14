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


class EmailSubscription(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, type=None, state=None, _from=None, bcc=None, cc=None, subject_template=None, send_to_customer=False, attach_invoice=False):
        """
        EmailSubscription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'id': 'str',
            'organization_id': 'str',
            'type': 'str',
            'state': 'str',
            '_from': 'str',
            'bcc': 'str',
            'cc': 'str',
            'subject_template': 'str',
            'send_to_customer': 'bool',
            'attach_invoice': 'bool'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'organization_id': 'organizationID',
            'type': 'type',
            'state': 'state',
            '_from': 'from',
            'bcc': 'bcc',
            'cc': 'cc',
            'subject_template': 'subjectTemplate',
            'send_to_customer': 'sendToCustomer',
            'attach_invoice': 'attachInvoice'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._organization_id = organization_id
        self._type = type
        self._state = state
        self.__from = _from
        self._bcc = bcc
        self._cc = cc
        self._subject_template = subject_template
        self._send_to_customer = send_to_customer
        self._attach_invoice = attach_invoice

    @property
    def created(self):
        """
        Gets the created of this EmailSubscription.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this EmailSubscription.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this EmailSubscription.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this EmailSubscription.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this EmailSubscription.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this EmailSubscription.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this EmailSubscription.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this EmailSubscription.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this EmailSubscription.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this EmailSubscription.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this EmailSubscription.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this EmailSubscription.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this EmailSubscription.
        { \"description\" : \"ID of the email provider.\", \"verbs\":[\"GET\"] }

        :return: The id of this EmailSubscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmailSubscription.
        { \"description\" : \"ID of the email provider.\", \"verbs\":[\"GET\"] }

        :param id: The id of this EmailSubscription.
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this EmailSubscription.
        { \"description\" : \"ID of the organization associated with the email provider.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The organization_id of this EmailSubscription.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this EmailSubscription.
        { \"description\" : \"ID of the organization associated with the email provider.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param organization_id: The organization_id of this EmailSubscription.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def type(self):
        """
        Gets the type of this EmailSubscription.


        :return: The type of this EmailSubscription.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EmailSubscription.


        :param type: The type of this EmailSubscription.
        :type: str
        """
        allowed_values = ["FailedPayment", "InvoicePaid", "SubscriptionCancellation", "SubscriptionCancelled", "SubscriptionPlanMigrated", "SubscriptionPlanMigrating", "CardExpired", "CardExpiring"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """
        Gets the state of this EmailSubscription.


        :return: The state of this EmailSubscription.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this EmailSubscription.


        :param state: The state of this EmailSubscription.
        :type: str
        """
        allowed_values = ["Active", "Disabled"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def _from(self):
        """
        Gets the _from of this EmailSubscription.


        :return: The _from of this EmailSubscription.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this EmailSubscription.


        :param _from: The _from of this EmailSubscription.
        :type: str
        """

        self.__from = _from

    @property
    def bcc(self):
        """
        Gets the bcc of this EmailSubscription.


        :return: The bcc of this EmailSubscription.
        :rtype: str
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """
        Sets the bcc of this EmailSubscription.


        :param bcc: The bcc of this EmailSubscription.
        :type: str
        """

        self._bcc = bcc

    @property
    def cc(self):
        """
        Gets the cc of this EmailSubscription.


        :return: The cc of this EmailSubscription.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """
        Sets the cc of this EmailSubscription.


        :param cc: The cc of this EmailSubscription.
        :type: str
        """

        self._cc = cc

    @property
    def subject_template(self):
        """
        Gets the subject_template of this EmailSubscription.


        :return: The subject_template of this EmailSubscription.
        :rtype: str
        """
        return self._subject_template

    @subject_template.setter
    def subject_template(self, subject_template):
        """
        Sets the subject_template of this EmailSubscription.


        :param subject_template: The subject_template of this EmailSubscription.
        :type: str
        """

        self._subject_template = subject_template

    @property
    def send_to_customer(self):
        """
        Gets the send_to_customer of this EmailSubscription.


        :return: The send_to_customer of this EmailSubscription.
        :rtype: bool
        """
        return self._send_to_customer

    @send_to_customer.setter
    def send_to_customer(self, send_to_customer):
        """
        Sets the send_to_customer of this EmailSubscription.


        :param send_to_customer: The send_to_customer of this EmailSubscription.
        :type: bool
        """

        self._send_to_customer = send_to_customer

    @property
    def attach_invoice(self):
        """
        Gets the attach_invoice of this EmailSubscription.


        :return: The attach_invoice of this EmailSubscription.
        :rtype: bool
        """
        return self._attach_invoice

    @attach_invoice.setter
    def attach_invoice(self, attach_invoice):
        """
        Sets the attach_invoice of this EmailSubscription.


        :param attach_invoice: The attach_invoice of this EmailSubscription.
        :type: bool
        """

        self._attach_invoice = attach_invoice

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
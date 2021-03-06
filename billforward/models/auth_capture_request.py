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


class AuthCaptureRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, account_id=None, gateway=None, company_name=None, email=None, first_name=None, last_name=None, mobile=None, default_payment_method=False, organization_id=None):
        """
        AuthCaptureRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'account_id': 'str',
            'gateway': 'str',
            'company_name': 'str',
            'email': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'mobile': 'str',
            'default_payment_method': 'bool',
            'organization_id': 'str'
        }

        self.attribute_map = {
            'type': '@type',
            'account_id': 'accountID',
            'gateway': 'gateway',
            'company_name': 'companyName',
            'email': 'email',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'mobile': 'mobile',
            'default_payment_method': 'defaultPaymentMethod',
            'organization_id': 'organizationID'
        }

        self._type = type
        self._account_id = account_id
        self._gateway = gateway
        self._company_name = company_name
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._mobile = mobile
        self._default_payment_method = default_payment_method
        self._organization_id = organization_id

    @property
    def type(self):
        """
        Gets the type of this AuthCaptureRequest.


        :return: The type of this AuthCaptureRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuthCaptureRequest.


        :param type: The type of this AuthCaptureRequest.
        :type: str
        """
        allowed_values = ["StripeAuthCaptureRequest"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def account_id(self):
        """
        Gets the account_id of this AuthCaptureRequest.
        {\"description\":\"ID of the BillForward Account with which you would like to associate the created payment method.<br>If omitted, BillForward will associate the created PaymentMethod with a newly-created Account, whose Profile details will be populated using billing information from the funding instrument.\",\"verbs\":[\"POST\"]}

        :return: The account_id of this AuthCaptureRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this AuthCaptureRequest.
        {\"description\":\"ID of the BillForward Account with which you would like to associate the created payment method.<br>If omitted, BillForward will associate the created PaymentMethod with a newly-created Account, whose Profile details will be populated using billing information from the funding instrument.\",\"verbs\":[\"POST\"]}

        :param account_id: The account_id of this AuthCaptureRequest.
        :type: str
        """

        self._account_id = account_id

    @property
    def gateway(self):
        """
        Gets the gateway of this AuthCaptureRequest.
        {\"description\":\"The gateway with which your funding instrument has been vaulted.\",\"verbs\":[\"POST\"]}

        :return: The gateway of this AuthCaptureRequest.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this AuthCaptureRequest.
        {\"description\":\"The gateway with which your funding instrument has been vaulted.\",\"verbs\":[\"POST\"]}

        :param gateway: The gateway of this AuthCaptureRequest.
        :type: str
        """
        allowed_values = ["Balanced", "Braintree", "Cybersource", "Paypal", "Stripe", "AuthorizeNet", "Spreedly", "SagePay", "TrustCommerce", "Payvision", "Kash"]
        if gateway not in allowed_values:
            raise ValueError(
                "Invalid value for `gateway` ({0}), must be one of {1}"
                .format(gateway, allowed_values)
            )

        self._gateway = gateway

    @property
    def company_name(self):
        """
        Gets the company_name of this AuthCaptureRequest.
        {\"description\":\"The name of the company of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :return: The company_name of this AuthCaptureRequest.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this AuthCaptureRequest.
        {\"description\":\"The name of the company of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :param company_name: The company_name of this AuthCaptureRequest.
        :type: str
        """

        self._company_name = company_name

    @property
    def email(self):
        """
        Gets the email of this AuthCaptureRequest.
        {\"description\":\"The email address of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :return: The email of this AuthCaptureRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AuthCaptureRequest.
        {\"description\":\"The email address of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :param email: The email of this AuthCaptureRequest.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this AuthCaptureRequest.
        {\"description\":\"The first name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :return: The first_name of this AuthCaptureRequest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this AuthCaptureRequest.
        {\"description\":\"The first name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :param first_name: The first_name of this AuthCaptureRequest.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this AuthCaptureRequest.
        {\"description\":\"The last name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :return: The last_name of this AuthCaptureRequest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this AuthCaptureRequest.
        {\"description\":\"The last name of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :param last_name: The last_name of this AuthCaptureRequest.
        :type: str
        """

        self._last_name = last_name

    @property
    def mobile(self):
        """
        Gets the mobile of this AuthCaptureRequest.
        {\"description\":\"The mobile phone number of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :return: The mobile of this AuthCaptureRequest.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this AuthCaptureRequest.
        {\"description\":\"The mobile phone number of the customer from whose card a PaymentMethod is being produced. If provided: this metadata will be used to populate a Profile &mdash; should a BillForward Account be created by this request.\",\"verbs\":[\"POST\"]}

        :param mobile: The mobile of this AuthCaptureRequest.
        :type: str
        """

        self._mobile = mobile

    @property
    def default_payment_method(self):
        """
        Gets the default_payment_method of this AuthCaptureRequest.
        {\"default\":false,\"description\":\"Whether the PaymentMethod produced by this request should be elected as the 'default' payment method for the concerned BillForward Account. Whichever PaymentMethod is elected as an Account's default payment method, will be consulted whenever payment is demanded of that Account (i.e. upon the execution of any of the Account's invoices).\",\"verbs\":[\"POST\"]}

        :return: The default_payment_method of this AuthCaptureRequest.
        :rtype: bool
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """
        Sets the default_payment_method of this AuthCaptureRequest.
        {\"default\":false,\"description\":\"Whether the PaymentMethod produced by this request should be elected as the 'default' payment method for the concerned BillForward Account. Whichever PaymentMethod is elected as an Account's default payment method, will be consulted whenever payment is demanded of that Account (i.e. upon the execution of any of the Account's invoices).\",\"verbs\":[\"POST\"]}

        :param default_payment_method: The default_payment_method of this AuthCaptureRequest.
        :type: bool
        """

        self._default_payment_method = default_payment_method

    @property
    def organization_id(self):
        """
        Gets the organization_id of this AuthCaptureRequest.
        {\"description\":\"ID of the BillForward Organization within which the requested PaymentMethod should be created. If omitted, this will be auto-populated using your authentication credentials.\",\"verbs\":[\"POST\"]}

        :return: The organization_id of this AuthCaptureRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this AuthCaptureRequest.
        {\"description\":\"ID of the BillForward Organization within which the requested PaymentMethod should be created. If omitted, this will be auto-populated using your authentication credentials.\",\"verbs\":[\"POST\"]}

        :param organization_id: The organization_id of this AuthCaptureRequest.
        :type: str
        """

        self._organization_id = organization_id

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

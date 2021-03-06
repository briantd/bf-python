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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, password=None, username=None, password_reset_valid_till=None, bf_admin=False, account_non_expired=False, account_non_locked=False, credentials_non_expired=False, enabled=False, timezone=None):
        """
        User - a model defined in Swagger

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
            'password': 'list[Password]',
            'username': 'list[Username]',
            'password_reset_valid_till': 'datetime',
            'bf_admin': 'bool',
            'account_non_expired': 'bool',
            'account_non_locked': 'bool',
            'credentials_non_expired': 'bool',
            'enabled': 'bool',
            'timezone': 'TimeZone'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'organization_id': 'organizationID',
            'password': 'password',
            'username': 'username',
            'password_reset_valid_till': 'passwordResetValidTill',
            'bf_admin': 'bfAdmin',
            'account_non_expired': 'accountNonExpired',
            'account_non_locked': 'accountNonLocked',
            'credentials_non_expired': 'credentialsNonExpired',
            'enabled': 'enabled',
            'timezone': 'timezone'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._organization_id = organization_id
        self._password = password
        self._username = username
        self._password_reset_valid_till = password_reset_valid_till
        self._bf_admin = bf_admin
        self._account_non_expired = account_non_expired
        self._account_non_locked = account_non_locked
        self._credentials_non_expired = credentials_non_expired
        self._enabled = enabled
        self._timezone = timezone

    @property
    def created(self):
        """
        Gets the created of this User.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this User.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this User.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this User.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this User.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this User.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this User.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this User.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this User.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this User.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this User.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this User.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this User.
        {\"description\":\"ID of the user\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        {\"description\":\"ID of the user\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param id: The id of this User.
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this User.
        {\"description\":\"ID of the Organization to which the User belongs.\",\"verbs\":[\"GET\",\"POST\"]}

        :return: The organization_id of this User.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this User.
        {\"description\":\"ID of the Organization to which the User belongs.\",\"verbs\":[\"GET\",\"POST\"]}

        :param organization_id: The organization_id of this User.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def password(self):
        """
        Gets the password of this User.
        {\"description\":\"Passwords associated with the user. A user must have one currently active password to login.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The password of this User.
        :rtype: list[Password]
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this User.
        {\"description\":\"Passwords associated with the user. A user must have one currently active password to login.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param password: The password of this User.
        :type: list[Password]
        """

        self._password = password

    @property
    def username(self):
        """
        Gets the username of this User.
        {\"description\":\"Usernames associated with the user. A user may have more than one username currently active. Usernames are enforced to be formatted as e-mail addresses.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The username of this User.
        :rtype: list[Username]
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        {\"description\":\"Usernames associated with the user. A user may have more than one username currently active. Usernames are enforced to be formatted as e-mail addresses.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param username: The username of this User.
        :type: list[Username]
        """

        self._username = username

    @property
    def password_reset_valid_till(self):
        """
        Gets the password_reset_valid_till of this User.
        {\"description\":\"The UTC DateTime when a password reset would no longer be valid with the current code.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The password_reset_valid_till of this User.
        :rtype: datetime
        """
        return self._password_reset_valid_till

    @password_reset_valid_till.setter
    def password_reset_valid_till(self, password_reset_valid_till):
        """
        Sets the password_reset_valid_till of this User.
        {\"description\":\"The UTC DateTime when a password reset would no longer be valid with the current code.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param password_reset_valid_till: The password_reset_valid_till of this User.
        :type: datetime
        """

        self._password_reset_valid_till = password_reset_valid_till

    @property
    def bf_admin(self):
        """
        Gets the bf_admin of this User.


        :return: The bf_admin of this User.
        :rtype: bool
        """
        return self._bf_admin

    @bf_admin.setter
    def bf_admin(self, bf_admin):
        """
        Sets the bf_admin of this User.


        :param bf_admin: The bf_admin of this User.
        :type: bool
        """

        self._bf_admin = bf_admin

    @property
    def account_non_expired(self):
        """
        Gets the account_non_expired of this User.
        {\"description\":\"Whether the User has expired.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The account_non_expired of this User.
        :rtype: bool
        """
        return self._account_non_expired

    @account_non_expired.setter
    def account_non_expired(self, account_non_expired):
        """
        Sets the account_non_expired of this User.
        {\"description\":\"Whether the User has expired.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param account_non_expired: The account_non_expired of this User.
        :type: bool
        """

        self._account_non_expired = account_non_expired

    @property
    def account_non_locked(self):
        """
        Gets the account_non_locked of this User.
        {\"description\":\"Is the User locked.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The account_non_locked of this User.
        :rtype: bool
        """
        return self._account_non_locked

    @account_non_locked.setter
    def account_non_locked(self, account_non_locked):
        """
        Sets the account_non_locked of this User.
        {\"description\":\"Is the User locked.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param account_non_locked: The account_non_locked of this User.
        :type: bool
        """

        self._account_non_locked = account_non_locked

    @property
    def credentials_non_expired(self):
        """
        Gets the credentials_non_expired of this User.
        {\"description\":\"Are the User credentials expired.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The credentials_non_expired of this User.
        :rtype: bool
        """
        return self._credentials_non_expired

    @credentials_non_expired.setter
    def credentials_non_expired(self, credentials_non_expired):
        """
        Sets the credentials_non_expired of this User.
        {\"description\":\"Are the User credentials expired.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param credentials_non_expired: The credentials_non_expired of this User.
        :type: bool
        """

        self._credentials_non_expired = credentials_non_expired

    @property
    def enabled(self):
        """
        Gets the enabled of this User.
        {\"description\":\"Is the User enabled.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The enabled of this User.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this User.
        {\"description\":\"Is the User enabled.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param enabled: The enabled of this User.
        :type: bool
        """

        self._enabled = enabled

    @property
    def timezone(self):
        """
        Gets the timezone of this User.
        {\"description\":\"The timezone used when displaying time series data to the user.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :return: The timezone of this User.
        :rtype: TimeZone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this User.
        {\"description\":\"The timezone used when displaying time series data to the user.\",\"verbs\":[\"POST\",\"PUT\",\"GET\"]}

        :param timezone: The timezone of this User.
        :type: TimeZone
        """

        self._timezone = timezone

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

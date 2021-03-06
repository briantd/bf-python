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


class EmailProvider(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, organization_id=None, name=None, host=None, port=None, username=None, password=None, deleted=False):
        """
        EmailProvider - a model defined in Swagger

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
            'name': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'deleted': 'bool'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'organization_id': 'organizationID',
            'name': 'name',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'deleted': 'deleted'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._organization_id = organization_id
        self._name = name
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._deleted = deleted

    @property
    def created(self):
        """
        Gets the created of this EmailProvider.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this EmailProvider.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this EmailProvider.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this EmailProvider.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this EmailProvider.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this EmailProvider.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this EmailProvider.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this EmailProvider.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this EmailProvider.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this EmailProvider.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this EmailProvider.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this EmailProvider.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this EmailProvider.
        { \"description\" : \"ID of the email provider.\", \"verbs\":[\"GET\"] }

        :return: The id of this EmailProvider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmailProvider.
        { \"description\" : \"ID of the email provider.\", \"verbs\":[\"GET\"] }

        :param id: The id of this EmailProvider.
        :type: str
        """

        self._id = id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this EmailProvider.
        { \"description\" : \"ID of the organization associated with the email provider.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The organization_id of this EmailProvider.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this EmailProvider.
        { \"description\" : \"ID of the organization associated with the email provider.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param organization_id: The organization_id of this EmailProvider.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """
        Gets the name of this EmailProvider.


        :return: The name of this EmailProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailProvider.


        :param name: The name of this EmailProvider.
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """
        Gets the host of this EmailProvider.


        :return: The host of this EmailProvider.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this EmailProvider.


        :param host: The host of this EmailProvider.
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """
        Gets the port of this EmailProvider.


        :return: The port of this EmailProvider.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this EmailProvider.


        :param port: The port of this EmailProvider.
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """
        Gets the username of this EmailProvider.


        :return: The username of this EmailProvider.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this EmailProvider.


        :param username: The username of this EmailProvider.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this EmailProvider.


        :return: The password of this EmailProvider.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this EmailProvider.


        :param password: The password of this EmailProvider.
        :type: str
        """

        self._password = password

    @property
    def deleted(self):
        """
        Gets the deleted of this EmailProvider.
        { \"description\" : \"Has the dunning-line been deleted?\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The deleted of this EmailProvider.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this EmailProvider.
        { \"description\" : \"Has the dunning-line been deleted?\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param deleted: The deleted of this EmailProvider.
        :type: bool
        """

        self._deleted = deleted

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

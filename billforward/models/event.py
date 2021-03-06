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


class Event(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, type=None, livemode=False, created=None, data=None, request=None, user_id=None, pending_webhooks=None):
        """
        Event - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'livemode': 'bool',
            'created': 'int',
            'data': 'EventData',
            'request': 'str',
            'user_id': 'str',
            'pending_webhooks': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'livemode': 'livemode',
            'created': 'created',
            'data': 'data',
            'request': 'request',
            'user_id': 'user_id',
            'pending_webhooks': 'pending_webhooks'
        }

        self._id = id
        self._type = type
        self._livemode = livemode
        self._created = created
        self._data = data
        self._request = request
        self._user_id = user_id
        self._pending_webhooks = pending_webhooks

    @property
    def id(self):
        """
        Gets the id of this Event.


        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Event.


        :param id: The id of this Event.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Event.


        :return: The type of this Event.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Event.


        :param type: The type of this Event.
        :type: str
        """

        self._type = type

    @property
    def livemode(self):
        """
        Gets the livemode of this Event.


        :return: The livemode of this Event.
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """
        Sets the livemode of this Event.


        :param livemode: The livemode of this Event.
        :type: bool
        """

        self._livemode = livemode

    @property
    def created(self):
        """
        Gets the created of this Event.


        :return: The created of this Event.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Event.


        :param created: The created of this Event.
        :type: int
        """

        self._created = created

    @property
    def data(self):
        """
        Gets the data of this Event.


        :return: The data of this Event.
        :rtype: EventData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Event.


        :param data: The data of this Event.
        :type: EventData
        """

        self._data = data

    @property
    def request(self):
        """
        Gets the request of this Event.


        :return: The request of this Event.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this Event.


        :param request: The request of this Event.
        :type: str
        """

        self._request = request

    @property
    def user_id(self):
        """
        Gets the user_id of this Event.


        :return: The user_id of this Event.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Event.


        :param user_id: The user_id of this Event.
        :type: str
        """

        self._user_id = user_id

    @property
    def pending_webhooks(self):
        """
        Gets the pending_webhooks of this Event.


        :return: The pending_webhooks of this Event.
        :rtype: int
        """
        return self._pending_webhooks

    @pending_webhooks.setter
    def pending_webhooks(self, pending_webhooks):
        """
        Sets the pending_webhooks of this Event.


        :param pending_webhooks: The pending_webhooks of this Event.
        :type: int
        """

        self._pending_webhooks = pending_webhooks

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

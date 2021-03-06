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


class CouponDiscount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, pricing_component=None, pricing_component_name=None, pricing_component_id=None, unit_of_measure_name=None, unit_of_measure_id=None, units_free=None, percentage_discount=None, cash_discount=None):
        """
        CouponDiscount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'changed_by': 'str',
            'updated': 'datetime',
            'pricing_component': 'str',
            'pricing_component_name': 'str',
            'pricing_component_id': 'str',
            'unit_of_measure_name': 'str',
            'unit_of_measure_id': 'str',
            'units_free': 'int',
            'percentage_discount': 'float',
            'cash_discount': 'float'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'pricing_component': 'pricingComponent',
            'pricing_component_name': 'pricingComponentName',
            'pricing_component_id': 'pricingComponentID',
            'unit_of_measure_name': 'unitOfMeasureName',
            'unit_of_measure_id': 'unitOfMeasureID',
            'units_free': 'unitsFree',
            'percentage_discount': 'percentageDiscount',
            'cash_discount': 'cashDiscount'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._pricing_component = pricing_component
        self._pricing_component_name = pricing_component_name
        self._pricing_component_id = pricing_component_id
        self._unit_of_measure_name = unit_of_measure_name
        self._unit_of_measure_id = unit_of_measure_id
        self._units_free = units_free
        self._percentage_discount = percentage_discount
        self._cash_discount = cash_discount

    @property
    def created(self):
        """
        Gets the created of this CouponDiscount.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this CouponDiscount.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CouponDiscount.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this CouponDiscount.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this CouponDiscount.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this CouponDiscount.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this CouponDiscount.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this CouponDiscount.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this CouponDiscount.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this CouponDiscount.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this CouponDiscount.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this CouponDiscount.
        :type: datetime
        """

        self._updated = updated

    @property
    def pricing_component(self):
        """
        Gets the pricing_component of this CouponDiscount.
        { \"description\" : \"Name or ID of the pricing component to apply the discount to. If not set blank discount is applied at the invoice level.\", \"verbs\":[\"POST\"] }

        :return: The pricing_component of this CouponDiscount.
        :rtype: str
        """
        return self._pricing_component

    @pricing_component.setter
    def pricing_component(self, pricing_component):
        """
        Sets the pricing_component of this CouponDiscount.
        { \"description\" : \"Name or ID of the pricing component to apply the discount to. If not set blank discount is applied at the invoice level.\", \"verbs\":[\"POST\"] }

        :param pricing_component: The pricing_component of this CouponDiscount.
        :type: str
        """

        self._pricing_component = pricing_component

    @property
    def pricing_component_name(self):
        """
        Gets the pricing_component_name of this CouponDiscount.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The pricing_component_name of this CouponDiscount.
        :rtype: str
        """
        return self._pricing_component_name

    @pricing_component_name.setter
    def pricing_component_name(self, pricing_component_name):
        """
        Sets the pricing_component_name of this CouponDiscount.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param pricing_component_name: The pricing_component_name of this CouponDiscount.
        :type: str
        """

        self._pricing_component_name = pricing_component_name

    @property
    def pricing_component_id(self):
        """
        Gets the pricing_component_id of this CouponDiscount.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :return: The pricing_component_id of this CouponDiscount.
        :rtype: str
        """
        return self._pricing_component_id

    @pricing_component_id.setter
    def pricing_component_id(self, pricing_component_id):
        """
        Sets the pricing_component_id of this CouponDiscount.
        { \"description\" : \"\", \"verbs\":[\"GET\"] }

        :param pricing_component_id: The pricing_component_id of this CouponDiscount.
        :type: str
        """

        self._pricing_component_id = pricing_component_id

    @property
    def unit_of_measure_name(self):
        """
        Gets the unit_of_measure_name of this CouponDiscount.


        :return: The unit_of_measure_name of this CouponDiscount.
        :rtype: str
        """
        return self._unit_of_measure_name

    @unit_of_measure_name.setter
    def unit_of_measure_name(self, unit_of_measure_name):
        """
        Sets the unit_of_measure_name of this CouponDiscount.


        :param unit_of_measure_name: The unit_of_measure_name of this CouponDiscount.
        :type: str
        """

        self._unit_of_measure_name = unit_of_measure_name

    @property
    def unit_of_measure_id(self):
        """
        Gets the unit_of_measure_id of this CouponDiscount.


        :return: The unit_of_measure_id of this CouponDiscount.
        :rtype: str
        """
        return self._unit_of_measure_id

    @unit_of_measure_id.setter
    def unit_of_measure_id(self, unit_of_measure_id):
        """
        Sets the unit_of_measure_id of this CouponDiscount.


        :param unit_of_measure_id: The unit_of_measure_id of this CouponDiscount.
        :type: str
        """

        self._unit_of_measure_id = unit_of_measure_id

    @property
    def units_free(self):
        """
        Gets the units_free of this CouponDiscount.
        { \"description\" : \"Number of units that are free for a pricing-component.\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The units_free of this CouponDiscount.
        :rtype: int
        """
        return self._units_free

    @units_free.setter
    def units_free(self, units_free):
        """
        Sets the units_free of this CouponDiscount.
        { \"description\" : \"Number of units that are free for a pricing-component.\", \"verbs\":[\"POST\",\"GET\"] }

        :param units_free: The units_free of this CouponDiscount.
        :type: int
        """

        self._units_free = units_free

    @property
    def percentage_discount(self):
        """
        Gets the percentage_discount of this CouponDiscount.
        { \"description\" : \"Percentage to be discounted\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The percentage_discount of this CouponDiscount.
        :rtype: float
        """
        return self._percentage_discount

    @percentage_discount.setter
    def percentage_discount(self, percentage_discount):
        """
        Sets the percentage_discount of this CouponDiscount.
        { \"description\" : \"Percentage to be discounted\", \"verbs\":[\"POST\",\"GET\"] }

        :param percentage_discount: The percentage_discount of this CouponDiscount.
        :type: float
        """

        self._percentage_discount = percentage_discount

    @property
    def cash_discount(self):
        """
        Gets the cash_discount of this CouponDiscount.
        { \"description\" : \"Fixed monetary amount to be discounted\", \"verbs\":[\"POST\",\"GET\"] }

        :return: The cash_discount of this CouponDiscount.
        :rtype: float
        """
        return self._cash_discount

    @cash_discount.setter
    def cash_discount(self, cash_discount):
        """
        Sets the cash_discount of this CouponDiscount.
        { \"description\" : \"Fixed monetary amount to be discounted\", \"verbs\":[\"POST\",\"GET\"] }

        :param cash_discount: The cash_discount of this CouponDiscount.
        :type: float
        """

        self._cash_discount = cash_discount

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

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


class Notification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, changed_by=None, updated=None, id=None, domain=None, action=None, organization_id=None, webhook_id=None, entity_id=None, destination_url=None, format=None, ack_enabled=False, entity=None, changes=None, last_send_attempt=None, next_send_attempt=None, final_send_attempt=None, total_send_attempts=None, state=None, acked=None):
        """
        Notification - a model defined in Swagger

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
            'domain': 'str',
            'action': 'str',
            'organization_id': 'str',
            'webhook_id': 'str',
            'entity_id': 'str',
            'destination_url': 'str',
            'format': 'str',
            'ack_enabled': 'bool',
            'entity': 'list[str]',
            'changes': 'list[str]',
            'last_send_attempt': 'datetime',
            'next_send_attempt': 'datetime',
            'final_send_attempt': 'datetime',
            'total_send_attempts': 'int',
            'state': 'str',
            'acked': 'datetime'
        }

        self.attribute_map = {
            'created': 'created',
            'changed_by': 'changedBy',
            'updated': 'updated',
            'id': 'id',
            'domain': 'domain',
            'action': 'action',
            'organization_id': 'organizationID',
            'webhook_id': 'webhookID',
            'entity_id': 'entityID',
            'destination_url': 'destinationURL',
            'format': 'format',
            'ack_enabled': 'ackEnabled',
            'entity': 'entity',
            'changes': 'changes',
            'last_send_attempt': 'lastSendAttempt',
            'next_send_attempt': 'nextSendAttempt',
            'final_send_attempt': 'finalSendAttempt',
            'total_send_attempts': 'totalSendAttempts',
            'state': 'state',
            'acked': 'acked'
        }

        self._created = created
        self._changed_by = changed_by
        self._updated = updated
        self._id = id
        self._domain = domain
        self._action = action
        self._organization_id = organization_id
        self._webhook_id = webhook_id
        self._entity_id = entity_id
        self._destination_url = destination_url
        self._format = format
        self._ack_enabled = ack_enabled
        self._entity = entity
        self._changes = changes
        self._last_send_attempt = last_send_attempt
        self._next_send_attempt = next_send_attempt
        self._final_send_attempt = final_send_attempt
        self._total_send_attempts = total_send_attempts
        self._state = state
        self._acked = acked

    @property
    def created(self):
        """
        Gets the created of this Notification.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :return: The created of this Notification.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Notification.
        { \"description\" : \"The UTC DateTime when the object was created.\", \"verbs\":[] }

        :param created: The created of this Notification.
        :type: datetime
        """

        self._created = created

    @property
    def changed_by(self):
        """
        Gets the changed_by of this Notification.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :return: The changed_by of this Notification.
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """
        Sets the changed_by of this Notification.
        { \"description\" : \"ID of the user who last updated the entity.\", \"verbs\":[] }

        :param changed_by: The changed_by of this Notification.
        :type: str
        """

        self._changed_by = changed_by

    @property
    def updated(self):
        """
        Gets the updated of this Notification.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :return: The updated of this Notification.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Notification.
        { \"description\" : \"The UTC DateTime when the object was last updated.\", \"verbs\":[] }

        :param updated: The updated of this Notification.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this Notification.
        { \"description\" : \"ID of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The id of this Notification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Notification.
        { \"description\" : \"ID of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param id: The id of this Notification.
        :type: str
        """

        self._id = id

    @property
    def domain(self):
        """
        Gets the domain of this Notification.
        { \"description\" : \"The domain of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The domain of this Notification.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Notification.
        { \"description\" : \"The domain of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param domain: The domain of this Notification.
        :type: str
        """
        allowed_values = ["Notification", "Organization", "OrganizationGateway", "Product", "User", "Subscription", "Profile", "ProductRatePlan", "Client", "Invoice", "PricingComponentValue", "Account", "PricingComponentValueChange", "PricingComponentTier", "PricingComponent", "PricingCalculation", "Coupon", "CouponDiscount", "CouponDefinition", "CouponInstance", "CouponModifier", "CouponRule", "CouponBookDefinition", "CouponBook", "InvoiceLine", "Webhook", "WebhookSubscription", "SubscriptionCancellation", "NotificationSnapshot", "InvoicePayment", "Payment", "PaymentMethod", "PaymentMethodSubscriptionLink", "DunningLine", "CybersourceToken", "Card", "Alias", "PaypalSimplePaymentReconciliation", "FreePaymentReconciliation", "LocustworldPaymentReconciliation", "CouponInstanceExistingValue", "TaxLine", "TaxationStrategy", "TaxationLink", "Address", "AmendmentPriceNTime", "Authority", "UnitOfMeasure", "SearchResult", "Amendment", "AuditLog", "Password", "Username", "FixedTermDefinition", "FixedTerm", "Refund", "CreditNote", "Receipt", "AmendmentCompoundConstituent", "APIConfiguration", "StripeToken", "BraintreeToken", "BalancedToken", "AuthorizeNetToken", "PaypalToken", "SpreedlyToken", "SagePayToken", "TrustCommerceToken", "PayVisionToken", "SagePayOutstandingTransaction", "SagePayEnabledCardType", "SagePayTransaction", "GatewayRevenue", "Migration", "AdhocSubscription", "SubscriptionCharge", "ComponentChange", "Verification", "UsageRoundingStrategies", "PricingComponentValueMigrationChargeAmendmentMapping", "AmendmentDiscardAmendment", "EntityTime", "AggregatingComponent", "PricingComponentMigrationValue", "MetadataKeyValue", "Metadata", "AggregationLink", "BFPermission", "Role", "PermissionLink", "PayVisionTransaction", "KashToken", "DataSynchronizationJob", "DataSynchronizationJobError", "DataSynchronizationConfiguration", "DataSynchronizationAppConfiguration", "AggregationChildrenResponse", "InvoiceLinePayment", "EmailSubscription", "EmailProvider", "TimeResponse", "Email", "RevenueAttribution", "Unknown"]
        if domain not in allowed_values:
            raise ValueError(
                "Invalid value for `domain` ({0}), must be one of {1}"
                .format(domain, allowed_values)
            )

        self._domain = domain

    @property
    def action(self):
        """
        Gets the action of this Notification.
        { \"description\" : \"The action associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The action of this Notification.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Notification.
        { \"description\" : \"The action associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param action: The action of this Notification.
        :type: str
        """
        allowed_values = ["Accept", "Active", "AwaitingPayment", "AwaitingRefund", "Cancelled", "Completed", "Created", "Error", "Expiring", "Expired", "Failed", "Migrated", "NeedsAmendments", "Paid", "Pending", "Provisioned", "Refunded", "Reject", "Trial", "Unknown", "Unpaid", "Updated", "Voided", "PaymentFailed"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Notification.
        { \"description\" : \"Organization associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The organization_id of this Notification.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Notification.
        { \"description\" : \"Organization associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param organization_id: The organization_id of this Notification.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def webhook_id(self):
        """
        Gets the webhook_id of this Notification.
        { \"description\" : \"Webhook associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The webhook_id of this Notification.
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """
        Sets the webhook_id of this Notification.
        { \"description\" : \"Webhook associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param webhook_id: The webhook_id of this Notification.
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this Notification.
        { \"description\" : \"The id of the entity associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The entity_id of this Notification.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this Notification.
        { \"description\" : \"The id of the entity associated with the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param entity_id: The entity_id of this Notification.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def destination_url(self):
        """
        Gets the destination_url of this Notification.
        { \"description\" : \"The URL the notification will be sent to.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The destination_url of this Notification.
        :rtype: str
        """
        return self._destination_url

    @destination_url.setter
    def destination_url(self, destination_url):
        """
        Sets the destination_url of this Notification.
        { \"description\" : \"The URL the notification will be sent to.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param destination_url: The destination_url of this Notification.
        :type: str
        """

        self._destination_url = destination_url

    @property
    def format(self):
        """
        Gets the format of this Notification.
        { \"description\" : \"Format of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The format of this Notification.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this Notification.
        { \"description\" : \"Format of the notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param format: The format of this Notification.
        :type: str
        """
        allowed_values = ["JSON", "XML"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def ack_enabled(self):
        """
        Gets the ack_enabled of this Notification.
        { \"description\" : \"If true notifications will continue to be sent until an acknowledgment is received.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The ack_enabled of this Notification.
        :rtype: bool
        """
        return self._ack_enabled

    @ack_enabled.setter
    def ack_enabled(self, ack_enabled):
        """
        Sets the ack_enabled of this Notification.
        { \"description\" : \"If true notifications will continue to be sent until an acknowledgment is received.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param ack_enabled: The ack_enabled of this Notification.
        :type: bool
        """

        self._ack_enabled = ack_enabled

    @property
    def entity(self):
        """
        Gets the entity of this Notification.


        :return: The entity of this Notification.
        :rtype: list[str]
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Notification.


        :param entity: The entity of this Notification.
        :type: list[str]
        """

        self._entity = entity

    @property
    def changes(self):
        """
        Gets the changes of this Notification.


        :return: The changes of this Notification.
        :rtype: list[str]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this Notification.


        :param changes: The changes of this Notification.
        :type: list[str]
        """

        self._changes = changes

    @property
    def last_send_attempt(self):
        """
        Gets the last_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notifications's last send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The last_send_attempt of this Notification.
        :rtype: datetime
        """
        return self._last_send_attempt

    @last_send_attempt.setter
    def last_send_attempt(self, last_send_attempt):
        """
        Sets the last_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notifications's last send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param last_send_attempt: The last_send_attempt of this Notification.
        :type: datetime
        """

        self._last_send_attempt = last_send_attempt

    @property
    def next_send_attempt(self):
        """
        Gets the next_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notification's next send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The next_send_attempt of this Notification.
        :rtype: datetime
        """
        return self._next_send_attempt

    @next_send_attempt.setter
    def next_send_attempt(self, next_send_attempt):
        """
        Sets the next_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notification's next send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param next_send_attempt: The next_send_attempt of this Notification.
        :type: datetime
        """

        self._next_send_attempt = next_send_attempt

    @property
    def final_send_attempt(self):
        """
        Gets the final_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notification's final send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The final_send_attempt of this Notification.
        :rtype: datetime
        """
        return self._final_send_attempt

    @final_send_attempt.setter
    def final_send_attempt(self, final_send_attempt):
        """
        Sets the final_send_attempt of this Notification.
        { \"description\" : \"The UTC DateTime of the notification's final send attempt.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param final_send_attempt: The final_send_attempt of this Notification.
        :type: datetime
        """

        self._final_send_attempt = final_send_attempt

    @property
    def total_send_attempts(self):
        """
        Gets the total_send_attempts of this Notification.
        { \"description\" : \"The number of send attempts for this notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The total_send_attempts of this Notification.
        :rtype: int
        """
        return self._total_send_attempts

    @total_send_attempts.setter
    def total_send_attempts(self, total_send_attempts):
        """
        Sets the total_send_attempts of this Notification.
        { \"description\" : \"The number of send attempts for this notification.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param total_send_attempts: The total_send_attempts of this Notification.
        :type: int
        """

        self._total_send_attempts = total_send_attempts

    @property
    def state(self):
        """
        Gets the state of this Notification.
        { \"description\" : \"Whether the notification has been sent.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The state of this Notification.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Notification.
        { \"description\" : \"Whether the notification has been sent.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param state: The state of this Notification.
        :type: str
        """
        allowed_values = ["Unsent", "Sending", "Sent"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def acked(self):
        """
        Gets the acked of this Notification.
        { \"description\" : \"The UTC DateTime when the notification was acked if it is ack enabled.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :return: The acked of this Notification.
        :rtype: datetime
        """
        return self._acked

    @acked.setter
    def acked(self, acked):
        """
        Sets the acked of this Notification.
        { \"description\" : \"The UTC DateTime when the notification was acked if it is ack enabled.\", \"verbs\":[\"POST\",\"PUT\",\"GET\"] }

        :param acked: The acked of this Notification.
        :type: datetime
        """

        self._acked = acked

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

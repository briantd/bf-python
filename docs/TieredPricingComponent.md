# TieredPricingComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was created.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**changed_by** | **str** | { \&quot;description\&quot; : \&quot;ID of the user who last updated the entity.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**updated** | **datetime** | { \&quot;description\&quot; : \&quot;The UTC DateTime when the object was last updated.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**type** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;default\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;] } | 
**version_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } | 
**crm_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;GET\&quot;] } When associating a pricing component with a product rate plan, this ID should be used. | 
**product_rate_plan_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**unit_of_measure_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**organization_id** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[] } | 
**name** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**public_name** | **str** | {\&quot;description\&quot;:\&quot;A friendly non-unique name used to identify this pricing-component\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;]} | [optional] 
**description** | **str** | { \&quot;description\&quot; : \&quot;\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**charge_type** | **str** | { \&quot;description\&quot; : \&quot;The charge type of the pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**invoicing_type** | **str** | { \&quot;default\&quot; : \&quot;Aggregated\&quot;,  \&quot;description\&quot; : \&quot;For &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;setup&lt;/span&gt; pricing components &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Immediate&lt;/span&gt; invoicing will result in an invoice being issued on subscription being set to the AwaitingPayment state, irrespective of the subscription start date. &lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;Aggregated&lt;/span&gt; invoicing will add a charge to the first invoice of the subscription.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**charge_model** | **str** | { \&quot;description\&quot; : \&quot;The charge model of the pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**upgrade_mode** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;immediate&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;Default behaviour when a value is upgraded using this pricing component, this behaviour can be overridden when changing the value.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;immediate&lt;/span&gt; &amp;mdash; Upgrade will apply at the time the request is made.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;delayed&lt;/span&gt; &amp;mdash; Upgrade will apply at the end of the current billing cycle.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**downgrade_mode** | **str** | {\&quot;default\&quot;:\&quot;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;delayed&lt;/span&gt;\&quot;,\&quot;description\&quot;:\&quot;Default behaviour when a value is downgraded using this pricing component, this behaviour can be overridden when changing the value.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;immediate&lt;/span&gt; &amp;mdash; Downgrade will apply at the time the request is made.&lt;br&gt;&lt;span class&#x3D;\\\&quot;label label-default\\\&quot;&gt;delayed&lt;/span&gt; &amp;mdash; Downgrade will apply at the end of the current billing cycle.\&quot;,\&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;GET\&quot;]} | [optional] 
**default_quantity** | **int** | { \&quot;description\&quot; : \&quot;The default quantity of the pricing-component. If no value is supplied on a subscription this value will be used. This is useful for setting an expected purchase level of for introducing new pricing components to existing subscriptions and not having to back-fill values\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**min_quantity** | **int** | { \&quot;default\&quot; : \&quot;0\&quot;, \&quot;description\&quot; : \&quot;The minimum quantity of the pricing-component.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**max_quantity** | **int** | { \&quot;description\&quot; : \&quot;The maximum quantity of the pricing-component.\&quot;, \&quot;verbs\&quot;:[] } | [optional] 
**valid_from** | **datetime** | { \&quot;default\&quot; : \&quot;current time\&quot;, \&quot;description\&quot; : \&quot;The DateTime specifying when the pricing-component is valid from.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | 
**valid_till** | **datetime** | {  \&quot;default\&quot; : \&quot;null\&quot;, \&quot;description\&quot; : \&quot;The UTC DateTime specifying when the pricing-component is valid till.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**tiers** | [**list[PricingComponentTier]**](PricingComponentTier.md) | {  \&quot;default\&quot; : \&quot;[]\&quot;, \&quot;description\&quot; : \&quot;The pricing-component-tiers associated with the pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 
**unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md) | { \&quot;description\&quot; : \&quot;The unit-of-measure associated with the pricing-component.\&quot;, \&quot;verbs\&quot;:[\&quot;POST\&quot;,\&quot;PUT\&quot;,\&quot;GET\&quot;] } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


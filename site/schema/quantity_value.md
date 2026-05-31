---
search:
  boost: 5.0
---

# Slot: quantity_value 


_Numeric quantity value._



<div data-search-exclude markdown="1">



URI: [pbs:quantity_value](https://schema.pragmaticbim.ch/quantity_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [QuantityValue](QuantityValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:quantity_value |
| native | pbs:quantity_value |




## LinkML Source

<details>
```yaml
name: quantity_value
description: Numeric quantity value.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- QuantityValue
range: double
required: true
minimum_value: 0

```
</details></div>
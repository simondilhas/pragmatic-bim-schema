---
search:
  boost: 5.0
---

# Slot: quantity_unit 


_Unit of the quantity value._



<div data-search-exclude markdown="1">



URI: [pbs:quantity_unit](https://schema.pragmaticbim.ch/quantity_unit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | Minimal quantity record for costing and analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [QuantityValue](QuantityValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:quantity_unit |
| native | pbs:quantity_unit |




## LinkML Source

<details>
```yaml
name: quantity_unit
description: Unit of the quantity value.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- QuantityValue
range: string
required: true

```
</details></div>
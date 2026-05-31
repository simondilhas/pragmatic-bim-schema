---
search:
  boost: 5.0
---

# Slot: cost_quantity_type 


_Quantity type used as basis for this cost calculation._



<div data-search-exclude markdown="1">



URI: [pbs:cost_quantity_type](https://schema.pragmaticbim.ch/cost_quantity_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QuantityType](QuantityType.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:cost_quantity_type |
| native | pbs:cost_quantity_type |




## LinkML Source

<details>
```yaml
name: cost_quantity_type
description: Quantity type used as basis for this cost calculation.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: QuantityType

```
</details></div>
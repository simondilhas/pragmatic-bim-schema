---
search:
  boost: 5.0
---

# Slot: unit_cost 


_Unit cost for this cost item._



<div data-search-exclude markdown="1">



URI: [pbs:unit_cost](https://schema.pragmaticbim.ch/unit_cost)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [CostRecord](CostRecord.md) |

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
| self | pbs:unit_cost |
| native | pbs:unit_cost |




## LinkML Source

<details>
```yaml
name: unit_cost
description: Unit cost for this cost item.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: double
required: true
minimum_value: 0

```
</details></div>
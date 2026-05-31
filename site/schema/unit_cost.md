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
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated cost records. |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantities. |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

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
- AbstractCostRecord
range: double
required: true
minimum_value: 0

```
</details></div>
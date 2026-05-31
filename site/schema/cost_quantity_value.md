---
search:
  boost: 5.0
---

# Slot: cost_quantity_value 


_Quantity magnitude used as basis for this cost calculation._



<div data-search-exclude markdown="1">



URI: [pbs:cost_quantity_value](https://schema.pragmaticbim.ch/cost_quantity_value)
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
| self | pbs:cost_quantity_value |
| native | pbs:cost_quantity_value |




## LinkML Source

<details>
```yaml
name: cost_quantity_value
description: Quantity magnitude used as basis for this cost calculation.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- AbstractCostRecord
range: double
minimum_value: 0

```
</details></div>
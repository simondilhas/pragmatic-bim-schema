---
search:
  boost: 5.0
---

# Slot: component_cost_items 


_Cost records aggregated into this assembly record._



<div data-search-exclude markdown="1">



URI: [pbs:component_cost_items](https://schema.pragmaticbim.ch/component_cost_items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CostRecord](CostRecord.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:component_cost_items |
| native | pbs:component_cost_items |




## LinkML Source

<details>
```yaml
name: component_cost_items
description: Cost records aggregated into this assembly record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: CostRecord
multivalued: true
inlined: false

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: component_cost_items 


_Atomic cost items that are aggregated into this cost assembly._



<div data-search-exclude markdown="1">



URI: [pbs:component_cost_items](https://schema.pragmaticbim.ch/component_cost_items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CostItem](CostItem.md) |
| Domain Of | [CostAssembly](CostAssembly.md) |

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
description: Atomic cost items that are aggregated into this cost assembly.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostAssembly
range: CostItem
multivalued: true
inlined: false

```
</details></div>
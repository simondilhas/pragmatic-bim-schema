---
search:
  boost: 5.0
---

# Slot: cost_category 


_Cost category label kept intentionally open pending classification-backed modeling._



<div data-search-exclude markdown="1">



URI: [pbs:cost_category](https://schema.pragmaticbim.ch/cost_category)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:cost_category |
| native | pbs:cost_category |




## LinkML Source

<details>
```yaml
name: cost_category
description: Cost category label kept intentionally open pending classification-backed
  modeling.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: string

```
</details></div>
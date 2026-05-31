---
search:
  boost: 5.0
---

# Slot: related_entity 


_Entity or space subject for adjacency or distance constraints._



<div data-search-exclude markdown="1">



URI: [pbs:related_entity](https://schema.pragmaticbim.ch/related_entity)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [SpatialRequirement](SpatialRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_entity |
| native | pbs:related_entity |




## LinkML Source

<details>
```yaml
name: related_entity
description: Entity or space subject for adjacency or distance constraints.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialRequirement
range: Entity
inlined: false

```
</details></div>
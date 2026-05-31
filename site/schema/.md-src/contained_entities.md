---
search:
  boost: 5.0
---

# Slot: contained_entities 


_Generic containment for associated entities._



<div data-search-exclude markdown="1">



URI: [pbs:contained_entities](https://schema.pragmaticbim.ch/contained_entities)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [Space](Space.md), [System](System.md) |

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
| self | pbs:contained_entities |
| native | pbs:contained_entities |




## LinkML Source

<details>
```yaml
name: contained_entities
description: Generic containment for associated entities.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Space
- System
range: Entity
multivalued: true

```
</details></div>
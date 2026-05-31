---
search:
  boost: 5.0
---

# Slot: space_type 


_Classification of space (void, circulation, usable, service)._



<div data-search-exclude markdown="1">



URI: [pbs:space_type](https://schema.pragmaticbim.ch/space_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpaceType](SpaceType.md) |
| Domain Of | [Space](Space.md) |

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
| self | pbs:space_type |
| native | pbs:space_type |




## LinkML Source

<details>
```yaml
name: space_type
description: Classification of space (void, circulation, usable, service).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Space
range: SpaceType
required: true

```
</details></div>
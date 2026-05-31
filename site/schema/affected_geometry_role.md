---
search:
  boost: 5.0
---

# Slot: affected_geometry_role 


_Geometry role affected when change_type is geometry_change._



<div data-search-exclude markdown="1">



URI: [pbs:affected_geometry_role](https://schema.pragmaticbim.ch/affected_geometry_role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeometryChange](GeometryChange.md) | Geometry or representation change for a subject. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeometryRepresentationType](GeometryRepresentationType.md) |
| Domain Of | [GeometryChange](GeometryChange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:affected_geometry_role |
| native | pbs:affected_geometry_role |




## LinkML Source

<details>
```yaml
name: affected_geometry_role
description: Geometry role affected when change_type is geometry_change.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- GeometryChange
range: GeometryRepresentationType

```
</details></div>
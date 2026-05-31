---
search:
  boost: 5.0
---

# Slot: geometry_representation 


_Representation kind/dimension (for example body_3d, footprint_2d, point), independent of file format._



<div data-search-exclude markdown="1">



URI: [pbs:geometry_representation](https://schema.pragmaticbim.ch/geometry_representation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeometryRepresentation](GeometryRepresentation.md) | Minimal geometry reference for an entity, separating representation from encoding format. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeometryRepresentationType](GeometryRepresentationType.md) |
| Domain Of | [GeometryRepresentation](GeometryRepresentation.md) |

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
| self | pbs:geometry_representation |
| native | pbs:geometry_representation |




## LinkML Source

<details>
```yaml
name: geometry_representation
description: Representation kind/dimension (for example body_3d, footprint_2d, point),
  independent of file format.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- GeometryRepresentation
range: GeometryRepresentationType
required: true

```
</details></div>
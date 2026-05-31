---
search:
  boost: 5.0
---

# Slot: geometry_format 


_Optional serialization/encoding format (for example ifc, gltf, wkt, geojson), independent of representation kind._



<div data-search-exclude markdown="1">



URI: [pbs:geometry_format](https://schema.pragmaticbim.ch/geometry_format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeometryRepresentation](GeometryRepresentation.md) | Minimal geometry reference for an entity, separating representation from encoding format. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [GeometryRepresentation](GeometryRepresentation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:geometry_format |
| native | pbs:geometry_format |




## LinkML Source

<details>
```yaml
name: geometry_format
description: Optional serialization/encoding format (for example ifc, gltf, wkt, geojson),
  independent of representation kind.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- GeometryRepresentation
range: string

```
</details></div>
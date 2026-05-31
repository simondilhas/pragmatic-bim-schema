---
search:
  boost: 5.0
---

# Slot: geometry_reference 


_URI/path/hash/pointer to geometry payload._



<div data-search-exclude markdown="1">



URI: [pbs:geometry_reference](https://schema.pragmaticbim.ch/geometry_reference)
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
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:geometry_reference |
| native | pbs:geometry_reference |




## LinkML Source

<details>
```yaml
name: geometry_reference
description: URI/path/hash/pointer to geometry payload.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- GeometryRepresentation
range: string
required: true

```
</details></div>
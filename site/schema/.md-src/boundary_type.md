---
search:
  boost: 5.0
---

# Slot: boundary_type 


_Classification of boundary element (e.g., covering)._



<div data-search-exclude markdown="1">



URI: [pbs:boundary_type](https://schema.pragmaticbim.ch/boundary_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BoundaryType](BoundaryType.md) |
| Domain Of | [Boundary](Boundary.md) |

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
| self | pbs:boundary_type |
| native | pbs:boundary_type |




## LinkML Source

<details>
```yaml
name: boundary_type
description: Classification of boundary element (e.g., covering).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Boundary
range: BoundaryType
required: true

```
</details></div>
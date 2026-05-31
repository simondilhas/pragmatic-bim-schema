---
search:
  boost: 5.0
---

# Slot: bounded_space 


_Space bounded by this boundary element._



<div data-search-exclude markdown="1">



URI: [pbs:bounded_space](https://schema.pragmaticbim.ch/bounded_space)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [Boundary](Boundary.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [bounded_by](bounded_by.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:bounded_space |
| native | pbs:bounded_space |




## LinkML Source

<details>
```yaml
name: bounded_space
description: Space bounded by this boundary element.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Boundary
inverse: bounded_by
range: Space

```
</details></div>
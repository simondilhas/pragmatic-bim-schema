---
search:
  boost: 5.0
---

# Slot: bounded_by 


_Physical elements that bound a space._



<div data-search-exclude markdown="1">



URI: [pbs:bounded_by](https://schema.pragmaticbim.ch/bounded_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalElement](PhysicalElement.md) |
| Domain Of | [Space](Space.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [bounded_space](bounded_space.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:bounded_by |
| native | pbs:bounded_by |




## LinkML Source

<details>
```yaml
name: bounded_by
description: Physical elements that bound a space.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Space
inverse: bounded_space
range: PhysicalElement
multivalued: true

```
</details></div>
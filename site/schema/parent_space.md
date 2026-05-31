---
search:
  boost: 5.0
---

# Slot: parent_space 


_Parent space where the equipment is located._



<div data-search-exclude markdown="1">



URI: [pbs:parent_space](https://schema.pragmaticbim.ch/parent_space)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
| Domain Of | [Equipment](Equipment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [contained_entities](contained_entities.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_space |
| native | pbs:parent_space |




## LinkML Source

<details>
```yaml
name: parent_space
description: Parent space where the equipment is located.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Equipment
inverse: contained_entities
range: Space

```
</details></div>
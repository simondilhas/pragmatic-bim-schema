---
search:
  boost: 5.0
---

# Slot: parent_system 


_Parent systems that the equipment belongs to._



<div data-search-exclude markdown="1">



URI: [pbs:parent_system](https://schema.pragmaticbim.ch/parent_system)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [System](System.md) |
| Domain Of | [Equipment](Equipment.md) |

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
| self | pbs:parent_system |
| native | pbs:parent_system |




## LinkML Source

<details>
```yaml
name: parent_system
description: Parent systems that the equipment belongs to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Equipment
range: System
multivalued: true

```
</details></div>
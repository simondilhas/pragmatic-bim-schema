---
search:
  boost: 5.0
---

# Slot: equipment_type 


_Classification of equipment (for example HVAC, electrical, plumbing)._



<div data-search-exclude markdown="1">



URI: [pbs:equipment_type](https://schema.pragmaticbim.ch/equipment_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EquipmentType](EquipmentType.md) |
| Domain Of | [Equipment](Equipment.md) |

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
| self | pbs:equipment_type |
| native | pbs:equipment_type |




## LinkML Source

<details>
```yaml
name: equipment_type
description: Classification of equipment (for example HVAC, electrical, plumbing).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Equipment
range: EquipmentType
required: true

```
</details></div>
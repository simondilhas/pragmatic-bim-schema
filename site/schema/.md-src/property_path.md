---
search:
  boost: 5.0
---

# Slot: property_path 


_Canonical path to the changed field. Examples: Pset_WallCommon.FireRating, IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389._

__



<div data-search-exclude markdown="1">



URI: [pbs:property_path](https://schema.pragmaticbim.ch/property_path)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  yes  |
| [RequirementChange](RequirementChange.md) | Change to a requirement record or its fields. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PropertyChange](PropertyChange.md), [RequirementChange](RequirementChange.md) |

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
| self | pbs:property_path |
| native | pbs:property_path |




## LinkML Source

<details>
```yaml
name: property_path
description: 'Canonical path to the changed field. Examples: Pset_WallCommon.FireRating,
  IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PropertyChange
- RequirementChange
range: string
required: true

```
</details></div>
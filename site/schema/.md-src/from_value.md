---
search:
  boost: 5.0
---

# Slot: from_value 


_Prior value serialized as text. Absent or null for new subjects or fields._



<div data-search-exclude markdown="1">



URI: [pbs:from_value](https://schema.pragmaticbim.ch/from_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  no  |
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:from_value |
| native | pbs:from_value |




## LinkML Source

<details>
```yaml
name: from_value
description: Prior value serialized as text. Absent or null for new subjects or fields.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PropertyChange
- RequirementChange
range: string

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: to_value 


_New value serialized as text. Absent or null for deleted subjects or fields._



<div data-search-exclude markdown="1">



URI: [pbs:to_value](https://schema.pragmaticbim.ch/to_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PropertyDelta](PropertyDelta.md) | Field-level difference between two revision states. Supports IFC attributes, PropertySets, schema slots, document fields, and text spans. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PropertyDelta](PropertyDelta.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:to_value |
| native | pbs:to_value |




## LinkML Source

<details>
```yaml
name: to_value
description: New value serialized as text. Absent or null for deleted subjects or
  fields.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PropertyDelta
range: string

```
</details></div>
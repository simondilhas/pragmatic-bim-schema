---
search:
  boost: 5.0
---

# Slot: property_path_kind 


_Classification of the property path for downstream diff interpretation._



<div data-search-exclude markdown="1">



URI: [pbs:property_path_kind](https://schema.pragmaticbim.ch/property_path_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PropertyDelta](PropertyDelta.md) | Field-level difference between two revision states. Supports IFC attributes, PropertySets, schema slots, document fields, and text spans. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PropertyPathKind](PropertyPathKind.md) |
| Domain Of | [PropertyDelta](PropertyDelta.md) |

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
| self | pbs:property_path_kind |
| native | pbs:property_path_kind |




## LinkML Source

<details>
```yaml
name: property_path_kind
description: Classification of the property path for downstream diff interpretation.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PropertyDelta
range: PropertyPathKind
required: true

```
</details></div>
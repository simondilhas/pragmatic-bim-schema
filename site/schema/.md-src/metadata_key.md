---
search:
  boost: 5.0
---

# Slot: metadata_key 


_Metadata key, for example IfcWall.FireRating or Pset_WallCommon.Reference._



<div data-search-exclude markdown="1">



URI: [pbs:metadata_key](https://schema.pragmaticbim.ch/metadata_key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetadataEntry](MetadataEntry.md) | Generic metadata entry for storing IFC attributes, PropertySet fields, or project-specific key-value data. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MetadataEntry](MetadataEntry.md) |

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
| self | pbs:metadata_key |
| native | pbs:metadata_key |




## LinkML Source

<details>
```yaml
name: metadata_key
description: Metadata key, for example IfcWall.FireRating or Pset_WallCommon.Reference.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MetadataEntry
range: string
required: true

```
</details></div>
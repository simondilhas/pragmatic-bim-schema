---
search:
  boost: 2.0
---


# Enum: PropertyPathKind 




_Classification of a property path for diff interpretation across IFC and text sources._



<div data-search-exclude markdown="1">

URI: [pbs:PropertyPathKind](https://schema.pragmaticbim.ch/PropertyPathKind)

**Enum URI:** [pbs:PropertyPathKind](https://schema.pragmaticbim.ch/PropertyPathKind)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ifc_attribute | pbs:property_path_kind_ifc_attribute | Direct IFC entity attribute (for example IfcWall.Name). |
| ifc_pset | pbs:property_path_kind_ifc_pset | IFC PropertySet property (for example Pset_WallCommon.FireRating). |
| schema_slot | pbs:property_path_kind_schema_slot | Field on a schema entity (for example description, space_type). |
| document_field | pbs:property_path_kind_document_field | Structured field in an extracted document (for example section.4.2.title). |
| text_span | pbs:property_path_kind_text_span | Free-text span anchor (for example body:char_offset:1204-1389). |




## Slots

| Name | Description |
| ---  | --- |
| [property_path_kind](property_path_kind.md) | Classification of the property path for downstream diff interpretation. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: PropertyPathKind
description: Classification of a property path for diff interpretation across IFC
  and text sources.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:PropertyPathKind
permissible_values:
  ifc_attribute:
    text: ifc_attribute
    description: Direct IFC entity attribute (for example IfcWall.Name).
    meaning: pbs:property_path_kind_ifc_attribute
  ifc_pset:
    text: ifc_pset
    description: IFC PropertySet property (for example Pset_WallCommon.FireRating).
    meaning: pbs:property_path_kind_ifc_pset
  schema_slot:
    text: schema_slot
    description: Field on a schema entity (for example description, space_type).
    meaning: pbs:property_path_kind_schema_slot
  document_field:
    text: document_field
    description: Structured field in an extracted document (for example section.4.2.title).
    meaning: pbs:property_path_kind_document_field
  text_span:
    text: text_span
    description: Free-text span anchor (for example body:char_offset:1204-1389).
    meaning: pbs:property_path_kind_text_span

```
</details>

</div>
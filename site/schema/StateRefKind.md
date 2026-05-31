---
search:
  boost: 2.0
---


# Enum: StateRefKind 




_Kind of content referenced by a StateRef pointer._



<div data-search-exclude markdown="1">

URI: [pbs:StateRefKind](https://schema.pragmaticbim.ch/StateRefKind)

**Enum URI:** [pbs:StateRefKind](https://schema.pragmaticbim.ch/StateRefKind)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ifc_model | pbs:state_ref_kind_ifc_model | Whole IFC file or subset export. |
| geometry | pbs:state_ref_kind_geometry | Geometry payload or representation blob. |
| document | pbs:state_ref_kind_document | Original file in DMS or object storage. |
| text_extract | pbs:state_ref_kind_text_extract | Normalized or extracted text used for diffing. |
| entity_record | pbs:state_ref_kind_entity_record | Serialized entity record at a specific revision. |
| other | pbs:state_ref_kind_other | Other content kind not covered by controlled values. |




## Slots

| Name | Description |
| ---  | --- |
| [state_ref_kind](state_ref_kind.md) | Kind of content referenced (for example ifc_model, document, text_extract). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: StateRefKind
description: Kind of content referenced by a StateRef pointer.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:StateRefKind
permissible_values:
  ifc_model:
    text: ifc_model
    description: Whole IFC file or subset export.
    meaning: pbs:state_ref_kind_ifc_model
  geometry:
    text: geometry
    description: Geometry payload or representation blob.
    meaning: pbs:state_ref_kind_geometry
  document:
    text: document
    description: Original file in DMS or object storage.
    meaning: pbs:state_ref_kind_document
  text_extract:
    text: text_extract
    description: Normalized or extracted text used for diffing.
    meaning: pbs:state_ref_kind_text_extract
  entity_record:
    text: entity_record
    description: Serialized entity record at a specific revision.
    meaning: pbs:state_ref_kind_entity_record
  other:
    text: other
    description: Other content kind not covered by controlled values.
    meaning: pbs:state_ref_kind_other

```
</details>

</div>
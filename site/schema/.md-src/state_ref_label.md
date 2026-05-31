---
search:
  boost: 5.0
---

# Slot: state_ref_label 


_Optional human-readable label (for example LOD300 export, Spec v3 draft)._



<div data-search-exclude markdown="1">



URI: [pbs:state_ref_label](https://schema.pragmaticbim.ch/state_ref_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StateRef](StateRef.md) | Pointer to a content state at a specific revision. Covers IFC models, geometry payloads, documents, and extracted text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StateRef](StateRef.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:state_ref_label |
| native | pbs:state_ref_label |




## LinkML Source

<details>
```yaml
name: state_ref_label
description: Optional human-readable label (for example LOD300 export, Spec v3 draft).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- StateRef
range: string

```
</details></div>
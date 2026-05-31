---
search:
  boost: 5.0
---

# Slot: state_ref_kind 


_Kind of content referenced (for example ifc_model, document, text_extract)._



<div data-search-exclude markdown="1">



URI: [pbs:state_ref_kind](https://schema.pragmaticbim.ch/state_ref_kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StateRef](StateRef.md) | Pointer to a content state at a specific revision. Covers IFC models, geometry payloads, documents, and extracted text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateRefKind](StateRefKind.md) |
| Domain Of | [StateRef](StateRef.md) |

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
| self | pbs:state_ref_kind |
| native | pbs:state_ref_kind |




## LinkML Source

<details>
```yaml
name: state_ref_kind
description: Kind of content referenced (for example ifc_model, document, text_extract).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- StateRef
range: StateRefKind
required: true

```
</details></div>
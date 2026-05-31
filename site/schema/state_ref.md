---
search:
  boost: 5.0
---

# Slot: state_ref 


_URI, path, or content hash identifying the stored content state._



<div data-search-exclude markdown="1">



URI: [pbs:state_ref](https://schema.pragmaticbim.ch/state_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StateRef](StateRef.md) | Pointer to a content state at a specific revision. Covers IFC models, geometry payloads, documents, and extracted text. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:state_ref |
| native | pbs:state_ref |




## LinkML Source

<details>
```yaml
name: state_ref
description: URI, path, or content hash identifying the stored content state.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- StateRef
range: uriorcurie
required: true

```
</details></div>
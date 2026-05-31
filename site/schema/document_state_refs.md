---
search:
  boost: 5.0
---

# Slot: document_state_refs 


_Optional baseline document states for the comparison that produced this changeset._



<div data-search-exclude markdown="1">



URI: [pbs:document_state_refs](https://schema.pragmaticbim.ch/document_state_refs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateRef](StateRef.md) |
| Domain Of | [ChangeSet](ChangeSet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:document_state_refs |
| native | pbs:document_state_refs |




## LinkML Source

<details>
```yaml
name: document_state_refs
description: Optional baseline document states for the comparison that produced this
  changeset.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ChangeSet
range: StateRef
multivalued: true
inlined: true

```
</details></div>
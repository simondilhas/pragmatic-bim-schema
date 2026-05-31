---
search:
  boost: 5.0
---

# Slot: document_state_uris 


_Optional URIs or content hashes for baseline document states used in this comparison._



<div data-search-exclude markdown="1">



URI: [pbs:document_state_uris](https://schema.pragmaticbim.ch/document_state_uris)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:document_state_uris |
| native | pbs:document_state_uris |




## LinkML Source

<details>
```yaml
name: document_state_uris
description: Optional URIs or content hashes for baseline document states used in
  this comparison.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ChangeSet
range: uriorcurie
multivalued: true

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: ifc_state_uri 


_Optional URI, path, or content hash for the baseline IFC model state used in this comparison._



<div data-search-exclude markdown="1">



URI: [pbs:ifc_state_uri](https://schema.pragmaticbim.ch/ifc_state_uri)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:ifc_state_uri |
| native | pbs:ifc_state_uri |




## LinkML Source

<details>
```yaml
name: ifc_state_uri
description: Optional URI, path, or content hash for the baseline IFC model state
  used in this comparison.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ChangeSet
range: uriorcurie

```
</details></div>
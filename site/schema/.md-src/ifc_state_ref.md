---
search:
  boost: 5.0
---

# Slot: ifc_state_ref 


_Optional baseline IFC model state for the comparison that produced this changeset._



<div data-search-exclude markdown="1">



URI: [pbs:ifc_state_ref](https://schema.pragmaticbim.ch/ifc_state_ref)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:ifc_state_ref |
| native | pbs:ifc_state_ref |




## LinkML Source

<details>
```yaml
name: ifc_state_ref
description: Optional baseline IFC model state for the comparison that produced this
  changeset.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ChangeSet
range: StateRef
inlined: true

```
</details></div>
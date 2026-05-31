---
search:
  boost: 5.0
---

# Slot: changes 


_Change records included in this batch._



<div data-search-exclude markdown="1">



URI: [pbs:changes](https://schema.pragmaticbim.ch/changes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Change](Change.md) |
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
| self | pbs:changes |
| native | pbs:changes |




## LinkML Source

<details>
```yaml
name: changes
description: Change records included in this batch.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ChangeSet
range: Change
multivalued: true
inlined: true

```
</details></div>
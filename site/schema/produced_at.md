---
search:
  boost: 5.0
---

# Slot: produced_at 


_Timestamp when this changeset was produced._



<div data-search-exclude markdown="1">



URI: [dcterms:created](http://purl.org/dc/terms/created)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [ChangeSet](ChangeSet.md) |
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:created |
| native | pbs:produced_at |




## LinkML Source

<details>
```yaml
name: produced_at
description: Timestamp when this changeset was produced.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:created
domain_of:
- ChangeSet
range: datetime

```
</details></div>
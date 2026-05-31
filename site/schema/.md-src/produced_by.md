---
search:
  boost: 5.0
---

# Slot: produced_by 


_Agent or system that produced this changeset._



<div data-search-exclude markdown="1">



URI: [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [ChangeSet](ChangeSet.md) |
| Slot URI | [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasAttributedTo |
| native | pbs:produced_by |




## LinkML Source

<details>
```yaml
name: produced_by
description: Agent or system that produced this changeset.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: prov:wasAttributedTo
domain_of:
- ChangeSet
range: Agent
inlined: false

```
</details></div>
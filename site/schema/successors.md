---
search:
  boost: 5.0
---

# Slot: successors 


_Forward precedence links to successor records. Reverse lookup (find all predecessors of X) requires scanning all TimeRecord.successors — acceptable for document exchange, not for live graph queries._



<div data-search-exclude markdown="1">



URI: [pbs:successors](https://schema.pragmaticbim.ch/successors)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeLink](TimeLink.md) |
| Domain Of | [TimeRecord](TimeRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeRecord](TimeRecord.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:successors |
| native | pbs:successors |




## LinkML Source

<details>
```yaml
name: successors
description: Forward precedence links to successor records. Reverse lookup (find all
  predecessors of X) requires scanning all TimeRecord.successors — acceptable for
  document exchange, not for live graph queries.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
owner: TimeRecord
domain_of:
- TimeRecord
range: TimeLink
multivalued: true
inlined: true

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: time_plan 


_Parent time plan this record belongs to._



<div data-search-exclude markdown="1">



URI: [pbs:time_plan](https://schema.pragmaticbim.ch/time_plan)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeRecord](TimeRecord.md) |
| Domain Of | [TimeRecord](TimeRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:time_plan |
| native | pbs:time_plan |




## LinkML Source

<details>
```yaml
name: time_plan
description: Parent time plan this record belongs to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeRecord
range: TimeRecord
inlined: false

```
</details></div>
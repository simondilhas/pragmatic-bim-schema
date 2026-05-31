---
search:
  boost: 5.0
---

# Slot: actual_start_at 


_Actual start timestamp for the time record where known._



<div data-search-exclude markdown="1">



URI: [pbs:actual_start_at](https://schema.pragmaticbim.ch/actual_start_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
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
| self | pbs:actual_start_at |
| native | pbs:actual_start_at |




## LinkML Source

<details>
```yaml
name: actual_start_at
description: Actual start timestamp for the time record where known.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeRecord
range: datetime

```
</details></div>
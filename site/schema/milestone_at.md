---
search:
  boost: 5.0
---

# Slot: milestone_at 


_Target timestamp for a zero-duration milestone checkpoint._



<div data-search-exclude markdown="1">



URI: [pbs:milestone_at](https://schema.pragmaticbim.ch/milestone_at)
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
| self | pbs:milestone_at |
| native | pbs:milestone_at |




## LinkML Source

<details>
```yaml
name: milestone_at
description: Target timestamp for a zero-duration milestone checkpoint.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeRecord
range: datetime

```
</details></div>
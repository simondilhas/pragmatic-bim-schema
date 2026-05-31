---
search:
  boost: 5.0
---

# Slot: time_plan 


_Parent time plan this item or dependency belongs to._



<div data-search-exclude markdown="1">



URI: [pbs:time_plan](https://schema.pragmaticbim.ch/time_plan)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeItem](TimeItem.md) | Planned work item with baseline and actual dates, optionally linked to model entities and a time plan. |  no  |
| [TimeDependency](TimeDependency.md) | Precedence relationship between two time items within a plan, optionally with lag. |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a time plan. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimePlan](TimePlan.md) |
| Domain Of | [TimeItem](TimeItem.md), [TimeDependency](TimeDependency.md) |

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
description: Parent time plan this item or dependency belongs to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeItem
- TimeDependency
range: TimePlan
inlined: false

```
</details></div>
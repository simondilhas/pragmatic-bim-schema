---
search:
  boost: 5.0
---

# Slot: component_time_items 


_Time records contained in this plan; set milestone_at on a record to mark it as a checkpoint._



<div data-search-exclude markdown="1">



URI: [pbs:component_time_items](https://schema.pragmaticbim.ch/component_time_items)
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
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:component_time_items |
| native | pbs:component_time_items |




## LinkML Source

<details>
```yaml
name: component_time_items
description: Time records contained in this plan; set milestone_at on a record to
  mark it as a checkpoint.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeRecord
range: TimeRecord
multivalued: true
inlined: false

```
</details></div>
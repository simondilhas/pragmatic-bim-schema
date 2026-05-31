---
search:
  boost: 5.0
---

# Slot: milestone_at 


_Target timestamp for the milestone checkpoint._



<div data-search-exclude markdown="1">



URI: [pbs:milestone_at](https://schema.pragmaticbim.ch/milestone_at)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a time plan. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Milestone](Milestone.md) |

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
description: Target timestamp for the milestone checkpoint.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Milestone
range: datetime

```
</details></div>
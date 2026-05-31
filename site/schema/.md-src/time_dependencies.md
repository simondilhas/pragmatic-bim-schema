---
search:
  boost: 5.0
---

# Slot: time_dependencies 


_Dependency relationships used within this time plan._



<div data-search-exclude markdown="1">



URI: [pbs:time_dependencies](https://schema.pragmaticbim.ch/time_dependencies)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimePlan](TimePlan.md) | Grouped schedule container defining component items, milestones, and dependencies for a scoped plan. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeDependency](TimeDependency.md) |
| Domain Of | [TimePlan](TimePlan.md) |

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
| self | pbs:time_dependencies |
| native | pbs:time_dependencies |




## LinkML Source

<details>
```yaml
name: time_dependencies
description: Dependency relationships used within this time plan.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimePlan
range: TimeDependency
multivalued: true
inlined: false

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: component_time_items 


_Time items contained in this plan; milestone instances may also appear through the TimeItem subtype._



<div data-search-exclude markdown="1">



URI: [pbs:component_time_items](https://schema.pragmaticbim.ch/component_time_items)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimePlan](TimePlan.md) | Grouped schedule container defining component items, milestones, and dependencies for a scoped plan. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeItem](TimeItem.md) |
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
| self | pbs:component_time_items |
| native | pbs:component_time_items |




## LinkML Source

<details>
```yaml
name: component_time_items
description: Time items contained in this plan; milestone instances may also appear
  through the TimeItem subtype.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimePlan
range: TimeItem
multivalued: true
inlined: false

```
</details></div>
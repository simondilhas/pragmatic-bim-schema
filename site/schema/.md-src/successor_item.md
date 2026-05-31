---
search:
  boost: 5.0
---

# Slot: successor_item 


_Time item whose timing is constrained by the predecessor item._



<div data-search-exclude markdown="1">



URI: [pbs:successor_item](https://schema.pragmaticbim.ch/successor_item)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeDependency](TimeDependency.md) | Precedence relationship between two time items within a plan, optionally with lag. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeItem](TimeItem.md) |
| Domain Of | [TimeDependency](TimeDependency.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:successor_item |
| native | pbs:successor_item |




## LinkML Source

<details>
```yaml
name: successor_item
description: Time item whose timing is constrained by the predecessor item.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeDependency
range: TimeItem
inlined: false

```
</details></div>
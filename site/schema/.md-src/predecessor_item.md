---
search:
  boost: 5.0
---

# Slot: predecessor_item 


_Time item that must occur before the successor item._



<div data-search-exclude markdown="1">



URI: [pbs:predecessor_item](https://schema.pragmaticbim.ch/predecessor_item)
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
| self | pbs:predecessor_item |
| native | pbs:predecessor_item |




## LinkML Source

<details>
```yaml
name: predecessor_item
description: Time item that must occur before the successor item.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeDependency
range: TimeItem
inlined: false

```
</details></div>
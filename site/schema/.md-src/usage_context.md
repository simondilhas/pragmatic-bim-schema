---
search:
  boost: 5.0
---

# Slot: usage_context 


_Optional usage context such as work, personal, support, billing, or emergency._



<div data-search-exclude markdown="1">



URI: [pbs:usage_context](https://schema.pragmaticbim.ch/usage_context)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ContactPoint](ContactPoint.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:usage_context |
| native | pbs:usage_context |




## LinkML Source

<details>
```yaml
name: usage_context
description: Optional usage context such as work, personal, support, billing, or emergency.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ContactPoint
range: string

```
</details></div>
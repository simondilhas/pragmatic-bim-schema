---
search:
  boost: 5.0
---

# Slot: dependency_type 


_Precedence logic used between the predecessor and successor items._



<div data-search-exclude markdown="1">



URI: [pbs:dependency_type](https://schema.pragmaticbim.ch/dependency_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeDependency](TimeDependency.md) | Precedence relationship between two time items within a plan, optionally with lag. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeDependencyType](TimeDependencyType.md) |
| Domain Of | [TimeDependency](TimeDependency.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:dependency_type |
| native | pbs:dependency_type |




## LinkML Source

<details>
```yaml
name: dependency_type
description: Precedence logic used between the predecessor and successor items.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- TimeDependency
range: TimeDependencyType
required: true

```
</details></div>
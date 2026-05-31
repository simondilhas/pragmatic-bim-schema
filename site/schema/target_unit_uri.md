---
search:
  boost: 5.0
---

# Slot: target_unit_uri 


_Optional URI identifying the target unit (for example QUDT)._



<div data-search-exclude markdown="1">



URI: [pbs:target_unit_uri](https://schema.pragmaticbim.ch/target_unit_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [PerformanceRequirement](PerformanceRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:target_unit_uri |
| native | pbs:target_unit_uri |




## LinkML Source

<details>
```yaml
name: target_unit_uri
description: Optional URI identifying the target unit (for example QUDT).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
range: uriorcurie

```
</details></div>
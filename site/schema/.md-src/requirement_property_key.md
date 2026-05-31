---
search:
  boost: 5.0
---

# Slot: requirement_property_key 


_Canonical performance key for the target (for example u_value, resistance_rating). Aligns with performance property keys where applicable._

__



<div data-search-exclude markdown="1">



URI: [pbs:requirement_property_key](https://schema.pragmaticbim.ch/requirement_property_key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PerformanceRequirement](PerformanceRequirement.md) |

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
| self | pbs:requirement_property_key |
| native | pbs:requirement_property_key |




## LinkML Source

<details>
```yaml
name: requirement_property_key
description: 'Canonical performance key for the target (for example u_value, resistance_rating).
  Aligns with performance property keys where applicable.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceRequirement
range: string
required: true

```
</details></div>
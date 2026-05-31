---
search:
  boost: 5.0
---

# Slot: min_clear_distance 


_Minimum clear distance in metres when adjacency_kind is min_clear_distance._



<div data-search-exclude markdown="1">



URI: [pbs:min_clear_distance](https://schema.pragmaticbim.ch/min_clear_distance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [SpatialRequirement](SpatialRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:min_clear_distance |
| native | pbs:min_clear_distance |




## LinkML Source

<details>
```yaml
name: min_clear_distance
description: Minimum clear distance in metres when adjacency_kind is min_clear_distance.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialRequirement
range: double
minimum_value: 0

```
</details></div>
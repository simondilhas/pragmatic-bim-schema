---
search:
  boost: 5.0
---

# Slot: min_height 


_Minimum required height or clear height in metres._



<div data-search-exclude markdown="1">



URI: [pbs:min_height](https://schema.pragmaticbim.ch/min_height)
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
| self | pbs:min_height |
| native | pbs:min_height |




## LinkML Source

<details>
```yaml
name: min_height
description: Minimum required height or clear height in metres.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialRequirement
range: double
minimum_value: 0

```
</details></div>
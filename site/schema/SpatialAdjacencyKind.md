---
search:
  boost: 2.0
---


# Enum: SpatialAdjacencyKind 




_Spatial adjacency semantics for spatial requirements._



<div data-search-exclude markdown="1">

URI: [pbs:SpatialAdjacencyKind](https://schema.pragmaticbim.ch/SpatialAdjacencyKind)

**Enum URI:** [pbs:SpatialAdjacencyKind](https://schema.pragmaticbim.ch/SpatialAdjacencyKind)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| adjacent_to | pbs:spatial_adjacency_adjacent_to | Subject must be adjacent to the related entity or space. |
| not_adjacent_to | pbs:spatial_adjacency_not_adjacent_to | Subject must not be adjacent to the related entity or space. |
| min_clear_distance | pbs:spatial_adjacency_min_clear_distance | Minimum clear distance to the related entity or space. |




## Slots

| Name | Description |
| ---  | --- |
| [adjacency_kind](adjacency_kind.md) | Adjacency semantics when this spatial requirement involves another subject. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SpatialAdjacencyKind
description: Spatial adjacency semantics for spatial requirements.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SpatialAdjacencyKind
permissible_values:
  adjacent_to:
    text: adjacent_to
    description: Subject must be adjacent to the related entity or space.
    meaning: pbs:spatial_adjacency_adjacent_to
  not_adjacent_to:
    text: not_adjacent_to
    description: Subject must not be adjacent to the related entity or space.
    meaning: pbs:spatial_adjacency_not_adjacent_to
  min_clear_distance:
    text: min_clear_distance
    description: Minimum clear distance to the related entity or space.
    meaning: pbs:spatial_adjacency_min_clear_distance

```
</details>

</div>
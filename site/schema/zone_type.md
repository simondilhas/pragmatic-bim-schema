---
search:
  boost: 5.0
---

# Slot: zone_type 


_Optional zone classification; intended for SpatialContext nodes where context_type is zone._



<div data-search-exclude markdown="1">



URI: [pbs:zone_type](https://schema.pragmaticbim.ch/zone_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, level, or zone. |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics. |  no  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics. |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics. |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structures. |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics. |  no  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics. |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ZoneType](ZoneType.md) |
| Domain Of | [SpatialContext](SpatialContext.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:zone_type |
| native | pbs:zone_type |




## LinkML Source

<details>
```yaml
name: zone_type
description: Optional zone classification; intended for SpatialContext nodes where
  context_type is zone.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialContext
range: ZoneType

```
</details></div>
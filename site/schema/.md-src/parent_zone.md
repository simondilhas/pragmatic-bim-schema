---
search:
  boost: 5.0
---

# Slot: parent_zone 


_Parent zone context reference._



<div data-search-exclude markdown="1">



URI: [pbs:parent_zone](https://schema.pragmaticbim.ch/parent_zone)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, level, or zone. |  yes  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |
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
| Range | [ZoneContext](ZoneContext.md) |
| Domain Of | [SpatialContext](SpatialContext.md), [Space](Space.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_zone |
| native | pbs:parent_zone |




## LinkML Source

<details>
```yaml
name: parent_zone
description: Parent zone context reference.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- SpatialContext
- Space
range: ZoneContext

```
</details></div>
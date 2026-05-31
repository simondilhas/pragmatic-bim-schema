---
search:
  boost: 5.0
---

# Slot: parent_building 


_Parent building context reference._



<div data-search-exclude markdown="1">



URI: [pbs:parent_building](https://schema.pragmaticbim.ch/parent_building)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level context. |  yes  |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, level, or zone. |  yes  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  yes  |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  yes  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones. |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element. |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators). |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |
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
| Range | [Entity](Entity.md) |
| Domain Of | [PhysicalElement](PhysicalElement.md), [SpatialContext](SpatialContext.md), [Space](Space.md), [System](System.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:parent_building |
| native | pbs:parent_building |




## LinkML Source

<details>
```yaml
name: parent_building
description: Parent building context reference.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PhysicalElement
- SpatialContext
- Space
- System
range: Entity

```
</details></div>
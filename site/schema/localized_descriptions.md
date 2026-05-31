---
search:
  boost: 5.0
---

# Slot: localized_descriptions 


_Localized variants of description._



<div data-search-exclude markdown="1">



URI: [pbs:localized_descriptions](https://schema.pragmaticbim.ch/localized_descriptions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Entity](Entity.md) | Common base class for all schema entities. |  no  |
| [Agent](Agent.md) | Abstract base class for people or organizations acting in workflow and communication roles. |  no  |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. |  no  |
| [Company](Company.md) | Organization, company, or legal entity participating in the project or asset lifecycle. |  no  |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and traceability. |  no  |
| [PhysicalElement](PhysicalElement.md) | Base class for physical elements that can be placed in built asset/level context. |  no  |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones. |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element. |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators). |  no  |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |
| [Boundary](Boundary.md) | Physical element acting as a boundary treatment (for example covering). |  no  |
| [Equipment](Equipment.md) | Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system. |  no  |
| [VirtualEntity](VirtualEntity.md) | Abstract base class for non-physical, conceptual, or informational entities. |  no  |
| [SpatialContext](SpatialContext.md) | Context node used to represent project, perimeter, legal site, built asset, level, or zone. |  no  |
| [ProjectContext](ProjectContext.md) | Spatial context node constrained to project semantics. |  no  |
| [PerimeterContext](PerimeterContext.md) | Spatial context node constrained to perimeter semantics. |  no  |
| [LegalSiteContext](LegalSiteContext.md) | Spatial context node constrained to legal site semantics. |  no  |
| [BuiltAssetContext](BuiltAssetContext.md) | Abstract spatial context for built assets such as buildings and civil structures. |  no  |
| [BuildingContext](BuildingContext.md) | Spatial context node constrained to building semantics. |  no  |
| [CivilStructureContext](CivilStructureContext.md) | Spatial context node constrained to civil structure semantics. |  no  |
| [LevelContext](LevelContext.md) | Spatial context node constrained to level/storey semantics. |  no  |
| [ZoneContext](ZoneContext.md) | Spatial context node constrained to zone semantics. |  no  |
| [Space](Space.md) | Spatial container used for occupancy, circulation, service, or analysis. |  no  |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  no  |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. |  no  |
| [AbstractTimeRecord](AbstractTimeRecord.md) | Abstract base for reusable time/schedule record fields shared by atomic and grouped time records. |  no  |
| [TimeItem](TimeItem.md) | Planned work item with baseline and actual dates, optionally linked to model entities and a time plan. |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a time plan. |  no  |
| [TimePlan](TimePlan.md) | Grouped schedule container defining component items, milestones, and dependencies for a scoped plan. |  no  |
| [TimeDependency](TimeDependency.md) | Precedence relationship between two time items within a plan, optionally with lag. |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated cost records. |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantities. |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items. |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LocalizedText](LocalizedText.md) |
| Domain Of | [Entity](Entity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:localized_descriptions |
| native | pbs:localized_descriptions |




## LinkML Source

<details>
```yaml
name: localized_descriptions
description: Localized variants of description.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Entity
range: LocalizedText
multivalued: true
inlined: true

```
</details></div>
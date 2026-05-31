---
search:
  boost: 5.0
---

# Slot: ifc_global_id 


_IFC GlobalId of the mapped entity._



<div data-search-exclude markdown="1">



URI: [pbs:ifc_global_id](https://schema.pragmaticbim.ch/ifc_global_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Entity](Entity.md) | Common base class for all schema entities. |  no  |
| [Change](Change.md) | Detected difference for one subject between two revisions (content_kind change). Supports IFC model diffs, document/text diffs, and schema-entity field changes. Use change_type together with the concrete subclass for interpretation. |  no  |
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
| [TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |  no  |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |
| [Material](Material.md) | Material definition that can be associated with one or more entities. |  no  |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  no  |
| [GeometryChange](GeometryChange.md) | Geometry or representation change for a subject. |  no  |
| [RequirementChange](RequirementChange.md) | Change to a requirement record or its fields. |  no  |
| [MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |  no  |
| [AdditionChange](AdditionChange.md) | New entity or requirement introduced in to_revision. |  no  |
| [DeletionChange](DeletionChange.md) | Entity or requirement removed in to_revision. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Entity](Entity.md), [Change](Change.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-3][0-9A-Za-z_$]{21}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:ifc_global_id |
| native | pbs:ifc_global_id |




## LinkML Source

<details>
```yaml
name: ifc_global_id
description: IFC GlobalId of the mapped entity.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Entity
- Change
range: string
pattern: ^[0-3][0-9A-Za-z_$]{21}$

```
</details></div>
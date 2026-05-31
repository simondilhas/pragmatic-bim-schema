---
search:
  boost: 5.0
---

# Slot: applies_to_entities 


_Model entities this record applies to (requirements, cost items, schedule items, etc.)._



<div data-search-exclude markdown="1">



URI: [pbs:applies_to_entities](https://schema.pragmaticbim.ch/applies_to_entities)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Requirement](Requirement.md) | Prescriptive requirement record (content_kind requirement). Not an Entity; may apply to one or more model entities. Domain is discriminated by concrete subclass (PerformanceRequirement, SpatialRequirement, etc.), not a separate slot. |  no  |
| [TimeRecord](TimeRecord.md) | Planned work record with baseline and actual dates, optionally linked to model entities and a time plan. — Set milestone_at to mark as a zero-duration checkpoint. — Populate component_time_items to act as a plan container. |  no  |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  no  |
| [BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [Requirement](Requirement.md), [TimeRecord](TimeRecord.md), [CostRecord](CostRecord.md) |

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
| self | pbs:applies_to_entities |
| native | pbs:applies_to_entities |




## LinkML Source

<details>
```yaml
name: applies_to_entities
description: Model entities this record applies to (requirements, cost items, schedule
  items, etc.).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Requirement
- TimeRecord
- CostRecord
range: Entity
multivalued: true
inlined: false

```
</details></div>
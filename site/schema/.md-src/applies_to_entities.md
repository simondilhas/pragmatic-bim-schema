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
| [Requirement](Requirement.md) | Prescriptive requirement record (content_kind requirement). Not an Entity; may apply to one or more model entities. |  no  |
| [AbstractTimeRecord](AbstractTimeRecord.md) | Abstract base for reusable time/schedule record fields shared by atomic and grouped time records. |  no  |
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated cost records. |  no  |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  no  |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  no  |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  no  |
| [BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |  no  |
| [TimeItem](TimeItem.md) | Planned work item with baseline and actual dates, optionally linked to model entities and a time plan. |  no  |
| [Milestone](Milestone.md) | Zero-duration checkpoint or delivery target within a time plan. |  no  |
| [TimePlan](TimePlan.md) | Grouped schedule container defining component items, milestones, and dependencies for a scoped plan. |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantities. |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Entity](Entity.md) |
| Domain Of | [Requirement](Requirement.md), [AbstractTimeRecord](AbstractTimeRecord.md), [AbstractCostRecord](AbstractCostRecord.md) |

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
- AbstractTimeRecord
- AbstractCostRecord
range: Entity
multivalued: true
inlined: false

```
</details></div>
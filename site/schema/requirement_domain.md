---
search:
  boost: 5.0
---

# Slot: requirement_domain 


_Domain of this requirement record (performance, spatial, regulatory, brief)._



<div data-search-exclude markdown="1">



URI: [pbs:requirement_domain](https://schema.pragmaticbim.ch/requirement_domain)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Requirement](Requirement.md) | Prescriptive requirement record (content_kind requirement). Not an Entity; may apply to one or more model entities. |  no  |
| [PerformanceRequirement](PerformanceRequirement.md) | Performance target requirement (U-value, fire rating, airflow, acoustic, etc.). |  yes  |
| [SpatialRequirement](SpatialRequirement.md) | Spatial constraint requirement (min area, min height, adjacency, etc.). |  yes  |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  yes  |
| [BriefRequirement](BriefRequirement.md) | Client or programme requirement, including free-standing brief items. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RequirementDomain](RequirementDomain.md) |
| Domain Of | [Requirement](Requirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:requirement_domain |
| native | pbs:requirement_domain |




## LinkML Source

<details>
```yaml
name: requirement_domain
description: Domain of this requirement record (performance, spatial, regulatory,
  brief).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Requirement
range: RequirementDomain
required: true

```
</details></div>
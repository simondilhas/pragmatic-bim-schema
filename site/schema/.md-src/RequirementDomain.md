---
search:
  boost: 2.0
---


# Enum: RequirementDomain 




_Domain of a prescriptive requirement record._



<div data-search-exclude markdown="1">

URI: [pbs:RequirementDomain](https://schema.pragmaticbim.ch/RequirementDomain)

**Enum URI:** [pbs:RequirementDomain](https://schema.pragmaticbim.ch/RequirementDomain)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| performance | pbs:requirement_domain_performance | Performance targets (U-value, fire rating, airflow, acoustic, etc.). |
| spatial | pbs:requirement_domain_spatial | Spatial constraints (min area, min height, adjacency, etc.). |
| regulatory | pbs:requirement_domain_regulatory | Regulatory references (building code, norm, standard). |
| brief | pbs:requirement_domain_brief | Client or programme requirement, including free-standing brief items. |




## Slots

| Name | Description |
| ---  | --- |
| [requirement_domain](requirement_domain.md) | Domain of this requirement record (performance, spatial, regulatory, brief). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: RequirementDomain
description: Domain of a prescriptive requirement record.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:RequirementDomain
permissible_values:
  performance:
    text: performance
    description: Performance targets (U-value, fire rating, airflow, acoustic, etc.).
    meaning: pbs:requirement_domain_performance
  spatial:
    text: spatial
    description: Spatial constraints (min area, min height, adjacency, etc.).
    meaning: pbs:requirement_domain_spatial
  regulatory:
    text: regulatory
    description: Regulatory references (building code, norm, standard).
    meaning: pbs:requirement_domain_regulatory
  brief:
    text: brief
    description: Client or programme requirement, including free-standing brief items.
    meaning: pbs:requirement_domain_brief

```
</details>

</div>
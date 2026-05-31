---
search:
  boost: 5.0
---

# Slot: system_discipline 


_Classification of system discipline (electrical, sanitary, ventilation, heating)._



<div data-search-exclude markdown="1">



URI: [pbs:system_discipline](https://schema.pragmaticbim.ch/system_discipline)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SystemDiscipline](SystemDiscipline.md) |
| Domain Of | [System](System.md) |

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
| self | pbs:system_discipline |
| native | pbs:system_discipline |




## LinkML Source

<details>
```yaml
name: system_discipline
description: Classification of system discipline (electrical, sanitary, ventilation,
  heating).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- System
range: SystemDiscipline
required: true

```
</details></div>
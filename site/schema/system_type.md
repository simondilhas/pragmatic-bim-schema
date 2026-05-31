---
search:
  boost: 5.0
---

# Slot: system_type 


_Classification of system role (unit, network, terminal)._



<div data-search-exclude markdown="1">



URI: [pbs:system_type](https://schema.pragmaticbim.ch/system_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SystemType](SystemType.md) |
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
| self | pbs:system_type |
| native | pbs:system_type |




## LinkML Source

<details>
```yaml
name: system_type
description: Classification of system role (unit, network, terminal).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- System
range: SystemType
required: true

```
</details></div>
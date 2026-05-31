---
search:
  boost: 5.0
---

# Slot: connection_physical_type 


_Classification of physical connector type (for example door, window, duct, pipe, cable)._



<div data-search-exclude markdown="1">



URI: [pbs:connection_physical_type](https://schema.pragmaticbim.ch/connection_physical_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionPhysicalType](ConnectionPhysicalType.md) |
| Domain Of | [ConnectionPhysical](ConnectionPhysical.md) |

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
| self | pbs:connection_physical_type |
| native | pbs:connection_physical_type |




## LinkML Source

<details>
```yaml
name: connection_physical_type
description: Classification of physical connector type (for example door, window,
  duct, pipe, cable).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: ConnectionPhysicalType
required: true

```
</details></div>
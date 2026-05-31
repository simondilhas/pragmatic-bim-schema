---
search:
  boost: 5.0
---

# Slot: connection_virtual_requirement_drivers 


_Main requirement drivers for this virtual connection._



<div data-search-exclude markdown="1">



URI: [pbs:connection_virtual_requirement_drivers](https://schema.pragmaticbim.ch/connection_virtual_requirement_drivers)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionRequirementDriver](ConnectionRequirementDriver.md) |
| Domain Of | [ConnectionVirtual](ConnectionVirtual.md) |

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
| self | pbs:connection_virtual_requirement_drivers |
| native | pbs:connection_virtual_requirement_drivers |




## LinkML Source

<details>
```yaml
name: connection_virtual_requirement_drivers
description: Main requirement drivers for this virtual connection.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionVirtual
range: ConnectionRequirementDriver
multivalued: true

```
</details></div>
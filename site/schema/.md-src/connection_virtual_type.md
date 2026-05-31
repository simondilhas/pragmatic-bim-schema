---
search:
  boost: 5.0
---

# Slot: connection_virtual_type 


_Classification of virtual connection semantics (for example structural_joint, adjacency, access)._



<div data-search-exclude markdown="1">



URI: [pbs:connection_virtual_type](https://schema.pragmaticbim.ch/connection_virtual_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConnectionVirtualType](ConnectionVirtualType.md) |
| Domain Of | [ConnectionVirtual](ConnectionVirtual.md) |

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
| self | pbs:connection_virtual_type |
| native | pbs:connection_virtual_type |




## LinkML Source

<details>
```yaml
name: connection_virtual_type
description: Classification of virtual connection semantics (for example structural_joint,
  adjacency, access).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionVirtual
range: ConnectionVirtualType
required: true

```
</details></div>
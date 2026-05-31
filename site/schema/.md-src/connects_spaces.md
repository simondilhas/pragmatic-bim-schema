---
search:
  boost: 5.0
---

# Slot: connects_spaces 


_Spaces connected by this virtual connection._



<div data-search-exclude markdown="1">



URI: [pbs:connects_spaces](https://schema.pragmaticbim.ch/connects_spaces)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionVirtual](ConnectionVirtual.md) | Logical or topological connection between spaces and/or physical elements. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Space](Space.md) |
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
| self | pbs:connects_spaces |
| native | pbs:connects_spaces |




## LinkML Source

<details>
```yaml
name: connects_spaces
description: Spaces connected by this virtual connection.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionVirtual
range: Space
multivalued: true

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: serves_zones 


_Zone context nodes served by this system._



<div data-search-exclude markdown="1">



URI: [pbs:serves_zones](https://schema.pragmaticbim.ch/serves_zones)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [System](System.md) | Building service system grouping that serves spaces or zones. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ZoneContext](ZoneContext.md) |
| Domain Of | [System](System.md) |

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
| self | pbs:serves_zones |
| native | pbs:serves_zones |




## LinkML Source

<details>
```yaml
name: serves_zones
description: Zone context nodes served by this system.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- System
range: ZoneContext
multivalued: true

```
</details></div>
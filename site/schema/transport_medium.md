---
search:
  boost: 5.0
---

# Slot: transport_medium 


_Primary transport medium carried or enabled by the connector (for example human_access, air, liquid, electricity)._



<div data-search-exclude markdown="1">



URI: [pbs:transport_medium](https://schema.pragmaticbim.ch/transport_medium)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConnectionPhysical](ConnectionPhysical.md) | Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TransportMedium](TransportMedium.md) |
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
| self | pbs:transport_medium |
| native | pbs:transport_medium |




## LinkML Source

<details>
```yaml
name: transport_medium
description: Primary transport medium carried or enabled by the connector (for example
  human_access, air, liquid, electricity).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ConnectionPhysical
range: TransportMedium
required: true

```
</details></div>
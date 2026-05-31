---
search:
  boost: 2.0
---


# Enum: ZoneType 




_Classification of zone purpose and organizational intent._



<div data-search-exclude markdown="1">

URI: [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)

**Enum URI:** [pbs:ZoneType](https://schema.pragmaticbim.ch/ZoneType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| occupancy_unit | ifcowl:IfcSpatialZone | Occupancy unit zone (for example apartment, office suite, or retail unit). |
| tenant | ifcowl:IfcSpatialZone | Tenant area zone used for leasing and occupancy boundaries. |
| functional | ifcowl:IfcSpatialZone | Functional grouping zone (for example clinical, retail, office support). |
| cost | ifcowl:IfcGroup | Cost grouping zone for estimation and controlling. |
| fire | ifcowl:IfcSpatialZone | Fire compartment or fire strategy grouping zone. |
| security | ifcowl:IfcSpatialZone | Security management zone for access control and surveillance planning. |




## Slots

| Name | Description |
| ---  | --- |
| [zone_type](zone_type.md) | Optional zone classification; intended for SpatialContext nodes where context_type is zone. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ZoneType
description: Classification of zone purpose and organizational intent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ZoneType
permissible_values:
  occupancy_unit:
    text: occupancy_unit
    description: Occupancy unit zone (for example apartment, office suite, or retail
      unit).
    meaning: ifcowl:IfcSpatialZone
  tenant:
    text: tenant
    description: Tenant area zone used for leasing and occupancy boundaries.
    meaning: ifcowl:IfcSpatialZone
  functional:
    text: functional
    description: Functional grouping zone (for example clinical, retail, office support).
    meaning: ifcowl:IfcSpatialZone
  cost:
    text: cost
    description: Cost grouping zone for estimation and controlling.
    meaning: ifcowl:IfcGroup
  fire:
    text: fire
    description: Fire compartment or fire strategy grouping zone.
    meaning: ifcowl:IfcSpatialZone
  security:
    text: security
    description: Security management zone for access control and surveillance planning.
    meaning: ifcowl:IfcSpatialZone

```
</details>

</div>
---
search:
  boost: 2.0
---


# Enum: ConnectionRequirementDriver 




_Main requirement drivers for connection element performance._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionRequirementDriver](https://schema.pragmaticbim.ch/ConnectionRequirementDriver)

**Enum URI:** [pbs:ConnectionRequirementDriver](https://schema.pragmaticbim.ch/ConnectionRequirementDriver)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| fire | pbs:connection_requirement_driver_fire |  |
| security | pbs:connection_requirement_driver_security |  |
| accessibility | pbs:connection_requirement_driver_accessibility |  |
| acoustic | pbs:connection_requirement_driver_acoustic |  |
| thermal | pbs:connection_requirement_driver_thermal |  |
| visual | pbs:connection_requirement_driver_visual |  |
| structural | pbs:connection_requirement_driver_structural |  |




## Slots

| Name | Description |
| ---  | --- |
| [connection_physical_requirement_drivers](connection_physical_requirement_drivers.md) | Performance requirement drivers for this physical connection element. Multiple values are allowed because one connection may need to satisfy several requirements. |
| [connection_virtual_requirement_drivers](connection_virtual_requirement_drivers.md) | Main requirement drivers for this virtual connection. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionRequirementDriver
description: Main requirement drivers for connection element performance.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionRequirementDriver
permissible_values:
  fire:
    text: fire
    meaning: pbs:connection_requirement_driver_fire
  security:
    text: security
    meaning: pbs:connection_requirement_driver_security
  accessibility:
    text: accessibility
    meaning: pbs:connection_requirement_driver_accessibility
  acoustic:
    text: acoustic
    meaning: pbs:connection_requirement_driver_acoustic
  thermal:
    text: thermal
    meaning: pbs:connection_requirement_driver_thermal
  visual:
    text: visual
    meaning: pbs:connection_requirement_driver_visual
  structural:
    text: structural
    meaning: pbs:connection_requirement_driver_structural

```
</details>

</div>
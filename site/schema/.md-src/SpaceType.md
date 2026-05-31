---
search:
  boost: 2.0
---


# Enum: SpaceType 




_Classification of space semantics used by modeling and downstream conversion._



<div data-search-exclude markdown="1">

URI: [pbs:SpaceType](https://schema.pragmaticbim.ch/SpaceType)

**Enum URI:** [pbs:SpaceType](https://schema.pragmaticbim.ch/SpaceType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| void | ifcowl:IfcSpace | Non-occupiable or intentionally empty space in the model. |
| circulation | ifcowl:IfcSpace | Space primarily intended for movement and access. |
| usable | ifcowl:IfcSpace | Space intended for regular occupancy or primary use. |
| service | ifcowl:IfcSpace | Space primarily intended for technical/service functions. |
| modeled_gross_floor_area | ifcowl:IfcSpace | Space classification used when representing gross floor area as modeled space. |
| modeled_gross_volume | ifcowl:IfcSpace | Space classification used when representing gross volume as modeled space. |




## Slots

| Name | Description |
| ---  | --- |
| [space_type](space_type.md) | Classification of space (void, circulation, usable, service). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SpaceType
description: Classification of space semantics used by modeling and downstream conversion.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SpaceType
permissible_values:
  void:
    text: void
    description: Non-occupiable or intentionally empty space in the model.
    meaning: ifcowl:IfcSpace
  circulation:
    text: circulation
    description: Space primarily intended for movement and access.
    meaning: ifcowl:IfcSpace
  usable:
    text: usable
    description: Space intended for regular occupancy or primary use.
    meaning: ifcowl:IfcSpace
  service:
    text: service
    description: Space primarily intended for technical/service functions.
    meaning: ifcowl:IfcSpace
  modeled_gross_floor_area:
    text: modeled_gross_floor_area
    description: Space classification used when representing gross floor area as modeled
      space.
    meaning: ifcowl:IfcSpace
  modeled_gross_volume:
    text: modeled_gross_volume
    description: Space classification used when representing gross volume as modeled
      space.
    meaning: ifcowl:IfcSpace

```
</details>

</div>
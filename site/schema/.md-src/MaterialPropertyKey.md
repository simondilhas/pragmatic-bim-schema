---
search:
  boost: 2.0
---


# Enum: MaterialPropertyKey 




_Canonical material-related keys derived from IFC PropertySets and material metadata._



<div data-search-exclude markdown="1">

URI: [pbs:MaterialPropertyKey](https://schema.pragmaticbim.ch/MaterialPropertyKey)

**Enum URI:** [pbs:MaterialPropertyKey](https://schema.pragmaticbim.ch/MaterialPropertyKey)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| material_name | pbs:material_property_name |  |
| material_class | pbs:material_property_class |  |
| density | pbs:material_property_density |  |
| thermal_conductivity | pbs:material_property_thermal_conductivity |  |




## Slots

| Name | Description |
| ---  | --- |
| [property_key](property_key.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: MaterialPropertyKey
description: Canonical material-related keys derived from IFC PropertySets and material
  metadata.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:MaterialPropertyKey
permissible_values:
  material_name:
    text: material_name
    meaning: pbs:material_property_name
  material_class:
    text: material_class
    meaning: pbs:material_property_class
  density:
    text: density
    meaning: pbs:material_property_density
  thermal_conductivity:
    text: thermal_conductivity
    meaning: pbs:material_property_thermal_conductivity

```
</details>

</div>
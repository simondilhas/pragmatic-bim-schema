---
search:
  boost: 2.0
---


# Enum: SeparatorSlabType 




_Classification of slab-based separator elements._



<div data-search-exclude markdown="1">

URI: [pbs:SeparatorSlabType](https://schema.pragmaticbim.ch/SeparatorSlabType)

**Enum URI:** [pbs:SeparatorSlabType](https://schema.pragmaticbim.ch/SeparatorSlabType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| floor | ifcowl:IfcSlabTypeEnum.FLOOR |  |
| roof | ifcowl:IfcSlabTypeEnum.ROOF |  |
| baseslab | ifcowl:IfcSlabTypeEnum.BASESLAB |  |
| balcony | ifcowl:IfcSlabTypeEnum.FLOOR | Balcony slab; mapped to FLOOR as the closest IFC slab type. |




## Slots

| Name | Description |
| ---  | --- |
| [separator_slab_type](separator_slab_type.md) | Classification of slab-based separator element (for example floor/roof/base slab). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SeparatorSlabType
description: Classification of slab-based separator elements.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SeparatorSlabType
permissible_values:
  floor:
    text: floor
    meaning: ifcowl:IfcSlabTypeEnum.FLOOR
  roof:
    text: roof
    meaning: ifcowl:IfcSlabTypeEnum.ROOF
  baseslab:
    text: baseslab
    meaning: ifcowl:IfcSlabTypeEnum.BASESLAB
  balcony:
    text: balcony
    description: Balcony slab; mapped to FLOOR as the closest IFC slab type.
    meaning: ifcowl:IfcSlabTypeEnum.FLOOR

```
</details>

</div>
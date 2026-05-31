---
search:
  boost: 2.0
---


# Enum: QuantityType 



<div data-search-exclude markdown="1">

URI: [pbs:QuantityType](https://schema.pragmaticbim.ch/QuantityType)

**Enum URI:** [pbs:QuantityType](https://schema.pragmaticbim.ch/QuantityType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| area_net_horizontal | ifcowl:IfcQuantityArea | Net horizontal area, typically usable floor area excluding non-net parts. |
| area_gross_horizontal | ifcowl:IfcQuantityArea | Gross horizontal area, typically measured to outer boundaries. |
| area_net_vertical | ifcowl:IfcQuantityArea | Net vertical area, typically wall or facade area excluding deductions. |
| area_gross_vertical | ifcowl:IfcQuantityArea | Gross vertical area, typically full wall or facade area including non-net portions. |
| volume_net | ifcowl:IfcQuantityVolume | Net enclosed volume after subtracting non-counted voids or deductions. |
| volume_gross | ifcowl:IfcQuantityVolume | Gross enclosed volume measured to external or gross boundaries. |
| length | ifcowl:IfcQuantityLength | Linear extent of an element or feature. |
| width | ifcowl:IfcQuantityLength | Width dimension of an element, opening, or space proxy. |
| height | ifcowl:IfcQuantityLength | Height dimension of an element, opening, or space proxy. |
| perimeter | ifcowl:IfcQuantityLength | Boundary length around a 2D shape or footprint. |




## Slots

| Name | Description |
| ---  | --- |
| [quantity_type](quantity_type.md) | Controlled quantity type. |
| [cost_quantity_type](cost_quantity_type.md) | Quantity type used as basis for this cost calculation. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: QuantityType
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:QuantityType
permissible_values:
  area_net_horizontal:
    text: area_net_horizontal
    description: Net horizontal area, typically usable floor area excluding non-net
      parts.
    meaning: ifcowl:IfcQuantityArea
  area_gross_horizontal:
    text: area_gross_horizontal
    description: Gross horizontal area, typically measured to outer boundaries.
    meaning: ifcowl:IfcQuantityArea
  area_net_vertical:
    text: area_net_vertical
    description: Net vertical area, typically wall or facade area excluding deductions.
    meaning: ifcowl:IfcQuantityArea
  area_gross_vertical:
    text: area_gross_vertical
    description: Gross vertical area, typically full wall or facade area including
      non-net portions.
    meaning: ifcowl:IfcQuantityArea
  volume_net:
    text: volume_net
    description: Net enclosed volume after subtracting non-counted voids or deductions.
    meaning: ifcowl:IfcQuantityVolume
  volume_gross:
    text: volume_gross
    description: Gross enclosed volume measured to external or gross boundaries.
    meaning: ifcowl:IfcQuantityVolume
  length:
    text: length
    description: Linear extent of an element or feature.
    meaning: ifcowl:IfcQuantityLength
  width:
    text: width
    description: Width dimension of an element, opening, or space proxy.
    meaning: ifcowl:IfcQuantityLength
  height:
    text: height
    description: Height dimension of an element, opening, or space proxy.
    meaning: ifcowl:IfcQuantityLength
  perimeter:
    text: perimeter
    description: Boundary length around a 2D shape or footprint.
    meaning: ifcowl:IfcQuantityLength

```
</details>

</div>
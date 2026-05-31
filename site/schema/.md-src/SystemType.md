---
search:
  boost: 2.0
---


# Enum: SystemType 




_Role of an MEP-related element or grouping in the service chain._



<div data-search-exclude markdown="1">

URI: [pbs:SystemType](https://schema.pragmaticbim.ch/SystemType)

**Enum URI:** [pbs:SystemType](https://schema.pragmaticbim.ch/SystemType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| unit | ifcowl:IfcUnitaryEquipment | Generating or converting unit (for example AHU, chiller, heat pump). |
| network | ifcowl:IfcDistributionFlowElement | Distribution network element carrying flow (for example ducts, pipes, cable carriers). |
| terminal | ifcowl:IfcFlowTerminal | End/terminal element located in served spaces. |




## Slots

| Name | Description |
| ---  | --- |
| [system_type](system_type.md) | Classification of system role (unit, network, terminal). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: SystemType
description: Role of an MEP-related element or grouping in the service chain.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:SystemType
permissible_values:
  unit:
    text: unit
    description: Generating or converting unit (for example AHU, chiller, heat pump).
    meaning: ifcowl:IfcUnitaryEquipment
  network:
    text: network
    description: Distribution network element carrying flow (for example ducts, pipes,
      cable carriers).
    meaning: ifcowl:IfcDistributionFlowElement
  terminal:
    text: terminal
    description: End/terminal element located in served spaces.
    meaning: ifcowl:IfcFlowTerminal

```
</details>

</div>
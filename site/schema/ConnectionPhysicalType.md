---
search:
  boost: 2.0
---


# Enum: ConnectionPhysicalType 




_Classification of physical connector elements that connect spaces._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionPhysicalType](https://schema.pragmaticbim.ch/ConnectionPhysicalType)

**Enum URI:** [pbs:ConnectionPhysicalType](https://schema.pragmaticbim.ch/ConnectionPhysicalType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| door | ifcowl:IfcDoor | Human access connector via a door element. |
| window | ifcowl:IfcWindow | Visual/daylight connector via a window element. |
| duct | ifcowl:IfcDuctSegment | Air distribution connector segment. |
| pipe | ifcowl:IfcPipeSegment | Fluid/gas distribution connector segment. |
| cable | ifcowl:IfcCableSegment | Electrical/data cable connector segment. |
| conduit | ifcowl:IfcConduitSegment | Electrical/data conduit connector segment. |
| opening_other | ifcowl:IfcOpeningElement | Other opening-style connector not covered by door/window. |
| network_other | ifcowl:IfcFlowSegment | Other network connector segment not covered by controlled values. |




## Slots

| Name | Description |
| ---  | --- |
| [connection_physical_type](connection_physical_type.md) | Classification of physical connector type (for example door, window, duct, pipe, cable). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionPhysicalType
description: Classification of physical connector elements that connect spaces.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionPhysicalType
permissible_values:
  door:
    text: door
    description: Human access connector via a door element.
    meaning: ifcowl:IfcDoor
  window:
    text: window
    description: Visual/daylight connector via a window element.
    meaning: ifcowl:IfcWindow
  duct:
    text: duct
    description: Air distribution connector segment.
    meaning: ifcowl:IfcDuctSegment
  pipe:
    text: pipe
    description: Fluid/gas distribution connector segment.
    meaning: ifcowl:IfcPipeSegment
  cable:
    text: cable
    description: Electrical/data cable connector segment.
    meaning: ifcowl:IfcCableSegment
  conduit:
    text: conduit
    description: Electrical/data conduit connector segment.
    meaning: ifcowl:IfcConduitSegment
  opening_other:
    text: opening_other
    description: Other opening-style connector not covered by door/window.
    meaning: ifcowl:IfcOpeningElement
  network_other:
    text: network_other
    description: Other network connector segment not covered by controlled values.
    meaning: ifcowl:IfcFlowSegment

```
</details>

</div>
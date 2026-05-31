---
search:
  boost: 5.0
---

# Slot: property_value_number 


_Numeric value when property_value_type is number._



<div data-search-exclude markdown="1">



URI: [pbs:property_value_number](https://schema.pragmaticbim.ch/property_value_number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceProperty](PerformanceProperty.md) | Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses. |  no  |
| [FireProperty](FireProperty.md) | Normalized fire-related property. |  no  |
| [AcousticProperty](AcousticProperty.md) | Normalized acoustic-related property. |  no  |
| [ThermalProperty](ThermalProperty.md) | Normalized thermal-related property. |  no  |
| [StructuralProperty](StructuralProperty.md) | Normalized structural-related property. |  no  |
| [SecurityProperty](SecurityProperty.md) | Normalized security-related property. |  no  |
| [MaterialProperty](MaterialProperty.md) | Normalized material-related property. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [PerformanceProperty](PerformanceProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:property_value_number |
| native | pbs:property_value_number |




## LinkML Source

<details>
```yaml
name: property_value_number
description: Numeric value when property_value_type is number.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceProperty
range: double

```
</details></div>
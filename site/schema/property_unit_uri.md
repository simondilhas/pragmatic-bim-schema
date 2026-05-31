---
search:
  boost: 5.0
---

# Slot: property_unit_uri 


_Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT._



<div data-search-exclude markdown="1">



URI: [pbs:property_unit_uri](https://schema.pragmaticbim.ch/property_unit_uri)
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
| Range | [Uriorcurie](Uriorcurie.md) |
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
| self | pbs:property_unit_uri |
| native | pbs:property_unit_uri |




## LinkML Source

<details>
```yaml
name: property_unit_uri
description: Optional URI that identifies the normalized property unit in an external
  vocabulary such as QUDT.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceProperty
range: uriorcurie

```
</details></div>
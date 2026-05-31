---
search:
  boost: 5.0
---

# Slot: property_key 


_Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum._



<div data-search-exclude markdown="1">



URI: [pbs:property_key](https://schema.pragmaticbim.ch/property_key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceProperty](PerformanceProperty.md) | Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses. |  no  |
| [FireProperty](FireProperty.md) | Normalized fire-related property. |  yes  |
| [AcousticProperty](AcousticProperty.md) | Normalized acoustic-related property. |  yes  |
| [ThermalProperty](ThermalProperty.md) | Normalized thermal-related property. |  yes  |
| [StructuralProperty](StructuralProperty.md) | Normalized structural-related property. |  yes  |
| [SecurityProperty](SecurityProperty.md) | Normalized security-related property. |  yes  |
| [MaterialProperty](MaterialProperty.md) | Normalized material-related property. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PerformanceProperty](PerformanceProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:property_key |
| native | pbs:property_key |




## LinkML Source

<details>
```yaml
name: property_key
description: Canonical key inside the domain; constrained via subclass slot_usage
  to a domain-specific enum.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceProperty
range: string
required: true

```
</details></div>
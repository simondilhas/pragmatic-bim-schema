---
search:
  boost: 5.0
---

# Slot: source_pset 


_Original IFC PropertySet name (for example Pset_WallCommon)._



<div data-search-exclude markdown="1">



URI: [pbs:source_pset](https://schema.pragmaticbim.ch/source_pset)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PerformanceProperty](PerformanceProperty.md) | Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses. |  no  |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  yes  |
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
| Range | [String](String.md) |
| Domain Of | [PerformanceProperty](PerformanceProperty.md), [PropertyChange](PropertyChange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:source_pset |
| native | pbs:source_pset |




## LinkML Source

<details>
```yaml
name: source_pset
description: Original IFC PropertySet name (for example Pset_WallCommon).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PerformanceProperty
- PropertyChange
range: string

```
</details></div>
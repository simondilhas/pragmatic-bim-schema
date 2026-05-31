---
search:
  boost: 5.0
---

# Slot: classification_scheme 


_Name of the classification scheme (for example ifc, uniclass, omniclass, custom)._



<div data-search-exclude markdown="1">



URI: [pbs:classification_scheme](https://schema.pragmaticbim.ch/classification_scheme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Classification](Classification.md) | Generic classification entry from any scheme (for example IFC, Uniclass, OmniClass, custom). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Classification](Classification.md) |

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
| self | pbs:classification_scheme |
| native | pbs:classification_scheme |




## LinkML Source

<details>
```yaml
name: classification_scheme
description: Name of the classification scheme (for example ifc, uniclass, omniclass,
  custom).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Classification
range: string
required: true

```
</details></div>
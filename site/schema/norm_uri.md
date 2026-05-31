---
search:
  boost: 5.0
---

# Slot: norm_uri 


_URI identifying the norm, standard, or building code._



<div data-search-exclude markdown="1">



URI: [pbs:norm_uri](https://schema.pragmaticbim.ch/norm_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulatoryRequirement](RegulatoryRequirement.md) | Regulatory reference requirement (building code, norm, standard). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [RegulatoryRequirement](RegulatoryRequirement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:norm_uri |
| native | pbs:norm_uri |




## LinkML Source

<details>
```yaml
name: norm_uri
description: URI identifying the norm, standard, or building code.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- RegulatoryRequirement
range: uriorcurie

```
</details></div>
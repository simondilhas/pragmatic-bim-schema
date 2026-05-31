---
search:
  boost: 5.0
---

# Slot: classification_uri 


_Optional URI/CURIE that identifies the classification concept in an external registry._



<div data-search-exclude markdown="1">



URI: [pbs:classification_uri](https://schema.pragmaticbim.ch/classification_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Classification](Classification.md) | Generic classification entry from any scheme (for example IFC, Uniclass, OmniClass, custom). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Classification](Classification.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:classification_uri |
| native | pbs:classification_uri |




## LinkML Source

<details>
```yaml
name: classification_uri
description: Optional URI/CURIE that identifies the classification concept in an external
  registry.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Classification
range: uriorcurie

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: decision_type 


_Decision type expressed as a URI/CURIE from a controlled vocabulary._



<div data-search-exclude markdown="1">



URI: [dcterms:type](http://purl.org/dc/terms/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [dcterms:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:type |
| native | pbs:decision_type |




## LinkML Source

<details>
```yaml
name: decision_type
description: Decision type expressed as a URI/CURIE from a controlled vocabulary.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:type
domain_of:
- Decision
range: uriorcurie

```
</details></div>
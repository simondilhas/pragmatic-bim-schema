---
search:
  boost: 5.0
---

# Slot: rationale 


_Human-readable rationale that explains why the decision was made._



<div data-search-exclude markdown="1">



URI: [dcterms:description](http://purl.org/dc/terms/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [dcterms:description](http://purl.org/dc/terms/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:description |
| native | pbs:rationale |




## LinkML Source

<details>
```yaml
name: rationale
description: Human-readable rationale that explains why the decision was made.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:description
domain_of:
- Decision
range: string

```
</details></div>
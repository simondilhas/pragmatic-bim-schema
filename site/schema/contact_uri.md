---
search:
  boost: 5.0
---

# Slot: contact_uri 


_URI for the contact endpoint or profile where applicable._



<div data-search-exclude markdown="1">



URI: [pbs:contact_uri](https://schema.pragmaticbim.ch/contact_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [ContactPoint](ContactPoint.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:contact_uri |
| native | pbs:contact_uri |




## LinkML Source

<details>
```yaml
name: contact_uri
description: URI for the contact endpoint or profile where applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ContactPoint
range: uriorcurie

```
</details></div>
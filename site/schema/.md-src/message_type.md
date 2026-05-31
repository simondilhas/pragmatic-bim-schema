---
search:
  boost: 5.0
---

# Slot: message_type 


_Message type expressed as a URI/CURIE from a controlled vocabulary._



<div data-search-exclude markdown="1">



URI: [dcterms:type](http://purl.org/dc/terms/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and traceability. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Message](Message.md) |
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
| native | pbs:message_type |




## LinkML Source

<details>
```yaml
name: message_type
description: Message type expressed as a URI/CURIE from a controlled vocabulary.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: dcterms:type
domain_of:
- Message
range: uriorcurie

```
</details></div>
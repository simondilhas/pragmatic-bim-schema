---
search:
  boost: 5.0
---

# Slot: message_body 


_Human-readable message content._



<div data-search-exclude markdown="1">



URI: [schema:text](http://schema.org/text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and traceability. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:text](http://schema.org/text) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:text |
| native | pbs:message_body |




## LinkML Source

<details>
```yaml
name: message_body
description: Human-readable message content.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:text
domain_of:
- Message
range: string

```
</details></div>
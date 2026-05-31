---
search:
  boost: 5.0
---

# Slot: message_subject 


_Optional subject or headline for the message._



<div data-search-exclude markdown="1">



URI: [schema:headline](http://schema.org/headline)
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
| Slot URI | [schema:headline](http://schema.org/headline) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:headline |
| native | pbs:message_subject |




## LinkML Source

<details>
```yaml
name: message_subject
description: Optional subject or headline for the message.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:headline
domain_of:
- Message
range: string

```
</details></div>
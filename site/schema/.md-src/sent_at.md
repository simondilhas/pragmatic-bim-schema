---
search:
  boost: 5.0
---

# Slot: sent_at 


_Timestamp when the message was sent._



<div data-search-exclude markdown="1">



URI: [schema:dateSent](http://schema.org/dateSent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and traceability. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:dateSent](http://schema.org/dateSent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:dateSent |
| native | pbs:sent_at |




## LinkML Source

<details>
```yaml
name: sent_at
description: Timestamp when the message was sent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:dateSent
domain_of:
- Message
range: datetime

```
</details></div>
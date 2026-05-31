---
search:
  boost: 5.0
---

# Slot: sender 


_Agent that sent the message._



<div data-search-exclude markdown="1">



URI: [schema:sender](http://schema.org/sender)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Message](Message.md) | Message or communication record linked to an entity for coordination and traceability. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Message](Message.md) |
| Slot URI | [schema:sender](http://schema.org/sender) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:sender |
| native | pbs:sender |




## LinkML Source

<details>
```yaml
name: sender
description: Agent that sent the message.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:sender
domain_of:
- Message
range: Agent
inlined: false

```
</details></div>
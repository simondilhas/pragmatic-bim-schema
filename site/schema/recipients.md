---
search:
  boost: 5.0
---

# Slot: recipients 


_Agents that received the message._



<div data-search-exclude markdown="1">



URI: [schema:recipient](http://schema.org/recipient)
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
| Slot URI | [schema:recipient](http://schema.org/recipient) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:recipient |
| native | pbs:recipients |




## LinkML Source

<details>
```yaml
name: recipients
description: Agents that received the message.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:recipient
domain_of:
- Message
range: Agent
multivalued: true
inlined: false

```
</details></div>
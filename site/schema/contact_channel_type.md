---
search:
  boost: 5.0
---

# Slot: contact_channel_type 


_Communication channel type such as email, phone, website, linkedin, whatsapp, signal, slack, teams, or telegram._



<div data-search-exclude markdown="1">



URI: [pbs:contact_channel_type](https://schema.pragmaticbim.ch/contact_channel_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContactPoint](ContactPoint.md) | Structured communication endpoint or profile for an agent. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | pbs:contact_channel_type |
| native | pbs:contact_channel_type |




## LinkML Source

<details>
```yaml
name: contact_channel_type
description: Communication channel type such as email, phone, website, linkedin, whatsapp,
  signal, slack, teams, or telegram.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ContactPoint
range: string

```
</details></div>
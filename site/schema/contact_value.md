---
search:
  boost: 5.0
---

# Slot: contact_value 


_Human-readable contact value such as an email address, phone number, handle, or username._



<div data-search-exclude markdown="1">



URI: [pbs:contact_value](https://schema.pragmaticbim.ch/contact_value)
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
| self | pbs:contact_value |
| native | pbs:contact_value |




## LinkML Source

<details>
```yaml
name: contact_value
description: Human-readable contact value such as an email address, phone number,
  handle, or username.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- ContactPoint
range: string

```
</details></div>
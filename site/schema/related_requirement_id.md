---
search:
  boost: 5.0
---

# Slot: related_requirement_id 


_Requirement identifier for match_change records._



<div data-search-exclude markdown="1">



URI: [pbs:related_requirement_id](https://schema.pragmaticbim.ch/related_requirement_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MatchChange](MatchChange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_requirement_id |
| native | pbs:related_requirement_id |




## LinkML Source

<details>
```yaml
name: related_requirement_id
description: Requirement identifier for match_change records.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MatchChange
range: string
required: true

```
</details></div>
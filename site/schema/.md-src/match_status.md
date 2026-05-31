---
search:
  boost: 5.0
---

# Slot: match_status 


_Whether the subject met the requirement at the target revision._



<div data-search-exclude markdown="1">



URI: [pbs:match_status](https://schema.pragmaticbim.ch/match_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MatchStatus](MatchStatus.md) |
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
| self | pbs:match_status |
| native | pbs:match_status |




## LinkML Source

<details>
```yaml
name: match_status
description: Whether the subject met the requirement at the target revision.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- MatchChange
range: MatchStatus
required: true

```
</details></div>
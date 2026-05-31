---
search:
  boost: 2.0
---


# Enum: MatchStatus 




_Whether an entity satisfies a related requirement at the target revision._



<div data-search-exclude markdown="1">

URI: [pbs:MatchStatus](https://schema.pragmaticbim.ch/MatchStatus)

**Enum URI:** [pbs:MatchStatus](https://schema.pragmaticbim.ch/MatchStatus)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| met | pbs:match_status_met | Subject satisfies the requirement. |
| unmet | pbs:match_status_unmet | Subject no longer satisfies the requirement. |
| unknown | pbs:match_status_unknown | Match could not be determined. |




## Slots

| Name | Description |
| ---  | --- |
| [match_status](match_status.md) | Whether the subject met the requirement at the target revision. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: MatchStatus
description: Whether an entity satisfies a related requirement at the target revision.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:MatchStatus
permissible_values:
  met:
    text: met
    description: Subject satisfies the requirement.
    meaning: pbs:match_status_met
  unmet:
    text: unmet
    description: Subject no longer satisfies the requirement.
    meaning: pbs:match_status_unmet
  unknown:
    text: unknown
    description: Match could not be determined.
    meaning: pbs:match_status_unknown

```
</details>

</div>
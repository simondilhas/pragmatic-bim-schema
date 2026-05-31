---
search:
  boost: 2.0
---


# Enum: TimeDependencyType 




_Precedence logic between two time items._



<div data-search-exclude markdown="1">

URI: [pbs:TimeDependencyType](https://schema.pragmaticbim.ch/TimeDependencyType)

**Enum URI:** [pbs:TimeDependencyType](https://schema.pragmaticbim.ch/TimeDependencyType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| finish_to_start | pbs:time_dependency_type_finish_to_start | Successor starts when the predecessor finishes. |
| start_to_start | pbs:time_dependency_type_start_to_start | Successor starts when the predecessor starts. |
| finish_to_finish | pbs:time_dependency_type_finish_to_finish | Successor finishes when the predecessor finishes. |
| start_to_finish | pbs:time_dependency_type_start_to_finish | Successor finishes when the predecessor starts. |




## Slots

| Name | Description |
| ---  | --- |
| [dependency_type](dependency_type.md) | Precedence logic used between the predecessor and successor items. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: TimeDependencyType
description: Precedence logic between two time items.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:TimeDependencyType
permissible_values:
  finish_to_start:
    text: finish_to_start
    description: Successor starts when the predecessor finishes.
    meaning: pbs:time_dependency_type_finish_to_start
  start_to_start:
    text: start_to_start
    description: Successor starts when the predecessor starts.
    meaning: pbs:time_dependency_type_start_to_start
  finish_to_finish:
    text: finish_to_finish
    description: Successor finishes when the predecessor finishes.
    meaning: pbs:time_dependency_type_finish_to_finish
  start_to_finish:
    text: start_to_finish
    description: Successor finishes when the predecessor starts.
    meaning: pbs:time_dependency_type_start_to_finish

```
</details>

</div>
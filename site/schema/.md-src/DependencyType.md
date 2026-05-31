---
search:
  boost: 2.0
---


# Enum: DependencyType 




_Precedence logic between two time records (FS finish-to-start, SS start-to-start, FF finish-to-finish, SF start-to-finish)._



<div data-search-exclude markdown="1">

URI: [pbs:DependencyType](https://schema.pragmaticbim.ch/DependencyType)

**Enum URI:** [pbs:DependencyType](https://schema.pragmaticbim.ch/DependencyType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| FS | pbs:dependency_type_finish_to_start | Successor starts when the predecessor finishes. |
| SS | pbs:dependency_type_start_to_start | Successor starts when the predecessor starts. |
| FF | pbs:dependency_type_finish_to_finish | Successor finishes when the predecessor finishes. |
| SF | pbs:dependency_type_start_to_finish | Successor finishes when the predecessor starts. |




## Slots

| Name | Description |
| ---  | --- |
| [dependency_type](dependency_type.md) | FS | SS | FF | SF |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: DependencyType
description: Precedence logic between two time records (FS finish-to-start, SS start-to-start,
  FF finish-to-finish, SF start-to-finish).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:DependencyType
permissible_values:
  FS:
    text: FS
    description: Successor starts when the predecessor finishes.
    meaning: pbs:dependency_type_finish_to_start
  SS:
    text: SS
    description: Successor starts when the predecessor starts.
    meaning: pbs:dependency_type_start_to_start
  FF:
    text: FF
    description: Successor finishes when the predecessor finishes.
    meaning: pbs:dependency_type_finish_to_finish
  SF:
    text: SF
    description: Successor finishes when the predecessor starts.
    meaning: pbs:dependency_type_start_to_finish

```
</details>

</div>
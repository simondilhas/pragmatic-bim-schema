---
search:
  boost: 2.0
---


# Enum: RequirementTargetOperator 




_Comparison operator for numeric or textual requirement targets._



<div data-search-exclude markdown="1">

URI: [pbs:RequirementTargetOperator](https://schema.pragmaticbim.ch/RequirementTargetOperator)

**Enum URI:** [pbs:RequirementTargetOperator](https://schema.pragmaticbim.ch/RequirementTargetOperator)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| equals | pbs:requirement_target_operator_equals |  |
| minimum | pbs:requirement_target_operator_minimum |  |
| maximum | pbs:requirement_target_operator_maximum |  |
| range | pbs:requirement_target_operator_range |  |




## Slots

| Name | Description |
| ---  | --- |
| [target_operator](target_operator.md) | Comparison operator for the requirement target. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: RequirementTargetOperator
description: Comparison operator for numeric or textual requirement targets.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:RequirementTargetOperator
permissible_values:
  equals:
    text: equals
    meaning: pbs:requirement_target_operator_equals
  minimum:
    text: minimum
    meaning: pbs:requirement_target_operator_minimum
  maximum:
    text: maximum
    meaning: pbs:requirement_target_operator_maximum
  range:
    text: range
    meaning: pbs:requirement_target_operator_range

```
</details>

</div>
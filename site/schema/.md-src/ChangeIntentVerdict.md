---
search:
  boost: 2.0
---


# Enum: ChangeIntentVerdict 




_Intent stability verdict from an automated judge (for example iterthink STABLE/NEW)._



<div data-search-exclude markdown="1">

URI: [pbs:ChangeIntentVerdict](https://schema.pragmaticbim.ch/ChangeIntentVerdict)

**Enum URI:** [pbs:ChangeIntentVerdict](https://schema.pragmaticbim.ch/ChangeIntentVerdict)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| stable | pbs:change_intent_verdict_stable | Change preserves design intent; downstream rules may treat as cosmetic. |
| new_intent | pbs:change_intent_verdict_new_intent | Change alters design intent; may require re-evaluation or new tasks. |




## Slots

| Name | Description |
| ---  | --- |
| [intent_verdict](intent_verdict.md) | Intent stability verdict from an automated judge (for example iterthink STABLE/NEW). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ChangeIntentVerdict
description: Intent stability verdict from an automated judge (for example iterthink
  STABLE/NEW).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ChangeIntentVerdict
permissible_values:
  stable:
    text: stable
    description: Change preserves design intent; downstream rules may treat as cosmetic.
    meaning: pbs:change_intent_verdict_stable
  new_intent:
    text: new_intent
    description: Change alters design intent; may require re-evaluation or new tasks.
    meaning: pbs:change_intent_verdict_new_intent

```
</details>

</div>
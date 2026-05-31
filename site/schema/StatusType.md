---
search:
  boost: 2.0
---


# Enum: StatusType 




_Lifecycle or QA gate status used for model progression and approvals._



<div data-search-exclude markdown="1">

URI: [pbs:StatusType](https://schema.pragmaticbim.ch/StatusType)

**Enum URI:** [pbs:StatusType](https://schema.pragmaticbim.ch/StatusType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| draft | pbs:status_draft | Work-in-progress state before formal review. |
| submitted | pbs:status_submitted | Submitted state for review or approval. |
| reviewed | pbs:status_reviewed | Reviewed state pending final approval decision. |
| approved | pbs:status_approved | Approved state accepted for downstream use. |
| rejected | pbs:status_rejected | Rejected state not accepted for downstream use. |
| archived | pbs:status_archived | Archived state no longer in use. |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | Lifecycle or QA status. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: StatusType
description: Lifecycle or QA gate status used for model progression and approvals.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:StatusType
permissible_values:
  draft:
    text: draft
    description: Work-in-progress state before formal review.
    meaning: pbs:status_draft
  submitted:
    text: submitted
    description: Submitted state for review or approval.
    meaning: pbs:status_submitted
  reviewed:
    text: reviewed
    description: Reviewed state pending final approval decision.
    meaning: pbs:status_reviewed
  approved:
    text: approved
    description: Approved state accepted for downstream use.
    meaning: pbs:status_approved
  rejected:
    text: rejected
    description: Rejected state not accepted for downstream use.
    meaning: pbs:status_rejected
  archived:
    text: archived
    description: Archived state no longer in use.
    meaning: pbs:status_archived

```
</details>

</div>
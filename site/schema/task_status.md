---
search:
  boost: 5.0
---

# Slot: task_status 


_Task status URI/CURIE aligned with action status vocabularies._



<div data-search-exclude markdown="1">



URI: [schema:actionStatus](http://schema.org/actionStatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workflows. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:actionStatus](http://schema.org/actionStatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:actionStatus |
| native | pbs:task_status |




## LinkML Source

<details>
```yaml
name: task_status
description: Task status URI/CURIE aligned with action status vocabularies.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:actionStatus
domain_of:
- Task
range: uriorcurie

```
</details></div>
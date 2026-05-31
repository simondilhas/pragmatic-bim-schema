---
search:
  boost: 5.0
---

# Slot: due_at 


_Due timestamp for task completion._



<div data-search-exclude markdown="1">



URI: [schema:deadline](http://schema.org/deadline)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workflows. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:deadline](http://schema.org/deadline) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:deadline |
| native | pbs:due_at |




## LinkML Source

<details>
```yaml
name: due_at
description: Due timestamp for task completion.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:deadline
domain_of:
- Task
range: datetime

```
</details></div>
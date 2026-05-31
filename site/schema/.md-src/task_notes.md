---
search:
  boost: 5.0
---

# Slot: task_notes 


_Additional notes or implementation details for the task._



<div data-search-exclude markdown="1">



URI: [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workflows. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:comment |
| native | pbs:task_notes |




## LinkML Source

<details>
```yaml
name: task_notes
description: Additional notes or implementation details for the task.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: rdfs:comment
domain_of:
- Task
range: string

```
</details></div>
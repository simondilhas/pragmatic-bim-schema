---
search:
  boost: 5.0
---

# Slot: assignee 


_Responsible agent._



<div data-search-exclude markdown="1">



URI: [schema:agent](http://schema.org/agent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Task](Task.md) | Action/task record linked to an entity for implementation and follow-up workflows. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Task](Task.md) |
| Slot URI | [schema:agent](http://schema.org/agent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:agent |
| native | pbs:assignee |




## LinkML Source

<details>
```yaml
name: assignee
description: Responsible agent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:agent
domain_of:
- Task
range: Agent
inlined: false

```
</details></div>
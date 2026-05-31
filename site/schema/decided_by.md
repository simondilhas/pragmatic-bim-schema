---
search:
  boost: 5.0
---

# Slot: decided_by 


_Agent responsible for the decision._



<div data-search-exclude markdown="1">



URI: [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Decision](Decision.md) | Decision record linked to an entity for workflow traceability and governance. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain Of | [Decision](Decision.md) |
| Slot URI | [prov:wasAttributedTo](http://www.w3.org/ns/prov#wasAttributedTo) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasAttributedTo |
| native | pbs:decided_by |




## LinkML Source

<details>
```yaml
name: decided_by
description: Agent responsible for the decision.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: prov:wasAttributedTo
domain_of:
- Decision
range: Agent
inlined: false

```
</details></div>
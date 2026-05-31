---
search:
  boost: 5.0
---

# Slot: postal_addresses 


_Structured postal or physical addresses associated with this agent._



<div data-search-exclude markdown="1">



URI: [pbs:postal_addresses](https://schema.pragmaticbim.ch/postal_addresses)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Agent](Agent.md) | Abstract base class for people or organizations acting in workflow and communication roles. |  no  |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. |  no  |
| [Company](Company.md) | Organization, company, or legal entity participating in the project or asset lifecycle. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PostalAddress](PostalAddress.md) |
| Domain Of | [Agent](Agent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:postal_addresses |
| native | pbs:postal_addresses |




## LinkML Source

<details>
```yaml
name: postal_addresses
description: Structured postal or physical addresses associated with this agent.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Agent
range: PostalAddress
multivalued: true
inlined: true

```
</details></div>
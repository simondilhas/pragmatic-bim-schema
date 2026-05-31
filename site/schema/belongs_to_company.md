---
search:
  boost: 5.0
---

# Slot: belongs_to_company 


_Optional company that the person belongs to._



<div data-search-exclude markdown="1">



URI: [pbs:belongs_to_company](https://schema.pragmaticbim.ch/belongs_to_company)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Individual stakeholder, contributor, assignee, or responsible party represented in the schema. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Company](Company.md) |
| Domain Of | [Person](Person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:belongs_to_company |
| native | pbs:belongs_to_company |




## LinkML Source

<details>
```yaml
name: belongs_to_company
description: Optional company that the person belongs to.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Person
range: Company
inlined: false

```
</details></div>
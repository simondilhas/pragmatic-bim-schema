---
search:
  boost: 5.0
---

# Slot: currency 


_ISO 4217 currency code (for example EUR, USD)._



<div data-search-exclude markdown="1">



URI: [pbs:currency](https://schema.pragmaticbim.ch/currency)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation and calculation, optionally linked to entities. Populate component_cost_items to act as an assembly (aggregated unit price). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Z]{3}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:currency |
| native | pbs:currency |




## LinkML Source

<details>
```yaml
name: currency
description: ISO 4217 currency code (for example EUR, USD).
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: string
required: true
pattern: ^[A-Z]{3}$

```
</details></div>
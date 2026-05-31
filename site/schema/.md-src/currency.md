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
| [AbstractCostRecord](AbstractCostRecord.md) | Abstract base for reusable cost record fields shared by atomic and aggregated cost records. |  no  |
| [CostItem](CostItem.md) | Cost record used for estimation and calculation, optionally linked to quantities. |  no  |
| [CostAssembly](CostAssembly.md) | Aggregated unit price assembled from multiple cost items. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractCostRecord](AbstractCostRecord.md) |

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
- AbstractCostRecord
range: string
required: true
pattern: ^[A-Z]{3}$

```
</details></div>
---
search:
  boost: 5.0
---

# Slot: address_country_code 


_Optional ISO 3166-1 alpha-2 or alpha-3 country code._



<div data-search-exclude markdown="1">



URI: [pbs:address_country_code](https://schema.pragmaticbim.ch/address_country_code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PostalAddress](PostalAddress.md) | Structured postal or physical address for an agent. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PostalAddress](PostalAddress.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:address_country_code |
| native | pbs:address_country_code |




## LinkML Source

<details>
```yaml
name: address_country_code
description: Optional ISO 3166-1 alpha-2 or alpha-3 country code.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PostalAddress
range: string

```
</details></div>
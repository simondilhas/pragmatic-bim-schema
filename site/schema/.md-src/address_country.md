---
search:
  boost: 5.0
---

# Slot: address_country 


_Country name._



<div data-search-exclude markdown="1">



URI: [schema:addressCountry](http://schema.org/addressCountry)
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
| Slot URI | [schema:addressCountry](http://schema.org/addressCountry) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:addressCountry |
| native | pbs:address_country |




## LinkML Source

<details>
```yaml
name: address_country
description: Country name.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:addressCountry
domain_of:
- PostalAddress
range: string

```
</details></div>
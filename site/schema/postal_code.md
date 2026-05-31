---
search:
  boost: 5.0
---

# Slot: postal_code 


_Postal or ZIP code._



<div data-search-exclude markdown="1">



URI: [schema:postalCode](http://schema.org/postalCode)
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
| Slot URI | [schema:postalCode](http://schema.org/postalCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:postalCode |
| native | pbs:postal_code |




## LinkML Source

<details>
```yaml
name: postal_code
description: Postal or ZIP code.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:postalCode
domain_of:
- PostalAddress
range: string

```
</details></div>
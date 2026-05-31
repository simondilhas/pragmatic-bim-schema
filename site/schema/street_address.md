---
search:
  boost: 5.0
---

# Slot: street_address 


_Street name and house number or equivalent address line._



<div data-search-exclude markdown="1">



URI: [schema:streetAddress](http://schema.org/streetAddress)
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
| Slot URI | [schema:streetAddress](http://schema.org/streetAddress) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:streetAddress |
| native | pbs:street_address |




## LinkML Source

<details>
```yaml
name: street_address
description: Street name and house number or equivalent address line.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:streetAddress
domain_of:
- PostalAddress
range: string

```
</details></div>
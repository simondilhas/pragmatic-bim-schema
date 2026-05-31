---
search:
  boost: 5.0
---

# Slot: post_office_box_number 


_Post office box number where applicable._



<div data-search-exclude markdown="1">



URI: [schema:postOfficeBoxNumber](http://schema.org/postOfficeBoxNumber)
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
| Slot URI | [schema:postOfficeBoxNumber](http://schema.org/postOfficeBoxNumber) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:postOfficeBoxNumber |
| native | pbs:post_office_box_number |




## LinkML Source

<details>
```yaml
name: post_office_box_number
description: Post office box number where applicable.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
slot_uri: schema:postOfficeBoxNumber
domain_of:
- PostalAddress
range: string

```
</details></div>
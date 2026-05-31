---
search:
  boost: 5.0
---

# Slot: target_item 


_The successor TimeRecord._



<div data-search-exclude markdown="1">



URI: [pbs:target_item](https://schema.pragmaticbim.ch/target_item)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeLink](TimeLink.md) | Inline typed precedence link from a TimeRecord to one successor. Not a VirtualEntity — no id, no mixin. Owned by the predecessor record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeRecord](TimeRecord.md) |
| Domain Of | [TimeLink](TimeLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeLink](TimeLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:target_item |
| native | pbs:target_item |




## LinkML Source

<details>
```yaml
name: target_item
description: The successor TimeRecord.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
owner: TimeLink
domain_of:
- TimeLink
range: TimeRecord
required: true

```
</details></div>
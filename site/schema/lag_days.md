---
search:
  boost: 5.0
---

# Slot: lag_days 

<div data-search-exclude markdown="1">



URI: [pbs:lag_days](https://schema.pragmaticbim.ch/lag_days)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeLink](TimeLink.md) | Inline typed precedence link from a TimeRecord to one successor. Not a VirtualEntity — no id, no mixin. Owned by the predecessor record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TimeLink](TimeLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `0` |
| Owner | [TimeLink](TimeLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:lag_days |
| native | pbs:lag_days |




## LinkML Source

<details>
```yaml
name: lag_days
from_schema: https://schema.pragmaticbim.ch
rank: 1000
ifabsent: '0'
owner: TimeLink
domain_of:
- TimeLink
range: integer

```
</details></div>
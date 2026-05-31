---
search:
  boost: 5.0
---

# Slot: dependency_type 


_FS | SS | FF | SF_



<div data-search-exclude markdown="1">



URI: [pbs:dependency_type](https://schema.pragmaticbim.ch/dependency_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeLink](TimeLink.md) | Inline typed precedence link from a TimeRecord to one successor. Not a VirtualEntity — no id, no mixin. Owned by the predecessor record. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DependencyType](DependencyType.md) |
| Domain Of | [TimeLink](TimeLink.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `FS` |
| Owner | [TimeLink](TimeLink.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:dependency_type |
| native | pbs:dependency_type |




## LinkML Source

<details>
```yaml
name: dependency_type
description: FS | SS | FF | SF
from_schema: https://schema.pragmaticbim.ch
rank: 1000
ifabsent: FS
owner: TimeLink
domain_of:
- TimeLink
range: DependencyType

```
</details></div>
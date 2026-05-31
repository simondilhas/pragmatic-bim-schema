---
search:
  boost: 5.0
---

# Slot: to_revision 


_Target revision number for this change._



<div data-search-exclude markdown="1">



URI: [pbs:to_revision](https://schema.pragmaticbim.ch/to_revision)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions (content_kind change). Supports IFC model diffs, document/text diffs, and schema-entity field changes. Use change_type together with the concrete subclass for interpretation. |  yes  |
| [ChangeSet](ChangeSet.md) | Batch of Change records produced by comparing two model or document revisions. |  no  |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  no  |
| [GeometryChange](GeometryChange.md) | Geometry or representation change for a subject. |  no  |
| [RequirementChange](RequirementChange.md) | Change to a requirement record or its fields. |  no  |
| [MatchChange](MatchChange.md) | Entity match status against a requirement changed (previously met / no longer meets). |  no  |
| [AdditionChange](AdditionChange.md) | New entity or requirement introduced in to_revision. |  no  |
| [DeletionChange](DeletionChange.md) | Entity or requirement removed in to_revision. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Change](Change.md), [ChangeSet](ChangeSet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:to_revision |
| native | pbs:to_revision |




## LinkML Source

<details>
```yaml
name: to_revision
description: Target revision number for this change.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
- ChangeSet
range: integer
required: true
minimum_value: 0

```
</details></div>
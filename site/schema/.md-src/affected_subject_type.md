---
search:
  boost: 5.0
---

# Slot: affected_subject_type 


_LinkML class name of the changed subject (for example Space, SeparatorWall, Document)._

__



<div data-search-exclude markdown="1">



URI: [pbs:affected_subject_type](https://schema.pragmaticbim.ch/affected_subject_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Change](Change.md) | Detected difference for one subject between two revisions (content_kind change). Supports IFC model diffs, document/text diffs, and schema-entity field changes. Use change_type together with the concrete subclass for interpretation. |  yes  |
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
| Range | [String](String.md) |
| Domain Of | [Change](Change.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:affected_subject_type |
| native | pbs:affected_subject_type |




## LinkML Source

<details>
```yaml
name: affected_subject_type
description: 'LinkML class name of the changed subject (for example Space, SeparatorWall,
  Document).

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Change
range: string
required: true

```
</details></div>
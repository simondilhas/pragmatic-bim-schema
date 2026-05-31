---
search:
  boost: 2.0
---


# Enum: ChangeType 




_Category of change detected between two revisions._



<div data-search-exclude markdown="1">

URI: [pbs:ChangeType](https://schema.pragmaticbim.ch/ChangeType)

**Enum URI:** [pbs:ChangeType](https://schema.pragmaticbim.ch/ChangeType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| geometry_change | pbs:change_type_geometry_change | Geometry or representation changed. |
| property_change | pbs:change_type_property_change | Attribute, PropertySet, or schema slot changed. |
| requirement_change | pbs:change_type_requirement_change | Requirement record or field changed. |
| match_change | pbs:change_type_match_change | Entity match status against a requirement changed (met / unmet). |
| addition | pbs:change_type_addition | New entity or requirement introduced. |
| deletion | pbs:change_type_deletion | Entity or requirement removed. |




## Slots

| Name | Description |
| ---  | --- |
| [change_type](change_type.md) | Category of change detected between two revisions. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ChangeType
description: Category of change detected between two revisions.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ChangeType
permissible_values:
  geometry_change:
    text: geometry_change
    description: Geometry or representation changed.
    meaning: pbs:change_type_geometry_change
  property_change:
    text: property_change
    description: Attribute, PropertySet, or schema slot changed.
    meaning: pbs:change_type_property_change
  requirement_change:
    text: requirement_change
    description: Requirement record or field changed.
    meaning: pbs:change_type_requirement_change
  match_change:
    text: match_change
    description: Entity match status against a requirement changed (met / unmet).
    meaning: pbs:change_type_match_change
  addition:
    text: addition
    description: New entity or requirement introduced.
    meaning: pbs:change_type_addition
  deletion:
    text: deletion
    description: Entity or requirement removed.
    meaning: pbs:change_type_deletion

```
</details>

</div>
---
search:
  boost: 2.0
---


# Enum: ContentKind 




_Top-level content category for adapter projection and schema routing._



<div data-search-exclude markdown="1">

URI: [pbs:ContentKind](https://schema.pragmaticbim.ch/ContentKind)

**Enum URI:** [pbs:ContentKind](https://schema.pragmaticbim.ch/ContentKind)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| physical | pbs:content_kind_physical | Tangible BIM element from the physical elements module. |
| virtual | pbs:content_kind_virtual | Non-physical conceptual entity (space, system, time/cost record, etc.). |
| context | pbs:content_kind_context | Spatial context node (project, site, building, level, zone). |
| requirement | pbs:content_kind_requirement | Prescriptive requirement record. |
| change | pbs:content_kind_change | Revision diff or audit record. |













## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ContentKind
description: Top-level content category for adapter projection and schema routing.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ContentKind
permissible_values:
  physical:
    text: physical
    description: Tangible BIM element from the physical elements module.
    meaning: pbs:content_kind_physical
  virtual:
    text: virtual
    description: Non-physical conceptual entity (space, system, time/cost record,
      etc.).
    meaning: pbs:content_kind_virtual
  context:
    text: context
    description: Spatial context node (project, site, building, level, zone).
    meaning: pbs:content_kind_context
  requirement:
    text: requirement
    description: Prescriptive requirement record.
    meaning: pbs:content_kind_requirement
  change:
    text: change
    description: Revision diff or audit record.
    meaning: pbs:content_kind_change

```
</details>

</div>
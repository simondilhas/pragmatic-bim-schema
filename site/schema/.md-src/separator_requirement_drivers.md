---
search:
  boost: 5.0
---

# Slot: separator_requirement_drivers 


_Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements._

__



<div data-search-exclude markdown="1">



URI: [pbs:separator_requirement_drivers](https://schema.pragmaticbim.ch/separator_requirement_drivers)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Separator](Separator.md) | Abstract base class for elements that separate spaces or zones. |  no  |
| [SeparatorWall](SeparatorWall.md) | Wall-based separating element. |  no  |
| [SeparatorSlab](SeparatorSlab.md) | Slab-based separating element (for example floor/roof/base slab separators). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SeparatorRequirementDriver](SeparatorRequirementDriver.md) |
| Domain Of | [Separator](Separator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:separator_requirement_drivers |
| native | pbs:separator_requirement_drivers |




## LinkML Source

<details>
```yaml
name: separator_requirement_drivers
description: 'Performance requirement drivers for this separator. Multiple values
  are allowed because one separator may need to satisfy several requirements.

  '
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Separator
range: SeparatorRequirementDriver
multivalued: true

```
</details></div>
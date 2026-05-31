---
search:
  boost: 5.0
---

# Slot: property_delta 


_Field-level differences detected between the two revision states._



<div data-search-exclude markdown="1">



URI: [pbs:property_delta](https://schema.pragmaticbim.ch/property_delta)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PropertyChange](PropertyChange.md) | Attribute, PropertySet, schema slot, or document field change. |  no  |
| [RequirementChange](RequirementChange.md) | Change to a requirement record or its fields. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PropertyDelta](PropertyDelta.md) |
| Domain Of | [PropertyChange](PropertyChange.md), [RequirementChange](RequirementChange.md) |

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
| self | pbs:property_delta |
| native | pbs:property_delta |




## LinkML Source

<details>
```yaml
name: property_delta
description: Field-level differences detected between the two revision states.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- PropertyChange
- RequirementChange
range: PropertyDelta
multivalued: true
inlined: true

```
</details></div>
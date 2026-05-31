---
search:
  boost: 2.0
---


# Enum: ConnectionVirtualType 




_Classification of virtual connection semantics using schema-internal meanings because no stable 1:1 IFC mapping exists for these concepts._



<div data-search-exclude markdown="1">

URI: [pbs:ConnectionVirtualType](https://schema.pragmaticbim.ch/ConnectionVirtualType)

**Enum URI:** [pbs:ConnectionVirtualType](https://schema.pragmaticbim.ch/ConnectionVirtualType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| structural_joint | pbs:connection_virtual_type_structural_joint | Logical structural continuity or structural joint relation. |
| adjacency | pbs:connection_virtual_type_adjacency | Topological adjacency relation without implying a physical opening. |
| access | pbs:connection_virtual_type_access | Access relation indicating passability or navigational linkage. |
| other | pbs:connection_virtual_type_other | Other virtual connection semantics not covered by the controlled values. |




## Slots

| Name | Description |
| ---  | --- |
| [connection_virtual_type](connection_virtual_type.md) | Classification of virtual connection semantics (for example structural_joint, adjacency, access). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ConnectionVirtualType
description: Classification of virtual connection semantics using schema-internal
  meanings because no stable 1:1 IFC mapping exists for these concepts.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ConnectionVirtualType
permissible_values:
  structural_joint:
    text: structural_joint
    description: Logical structural continuity or structural joint relation.
    meaning: pbs:connection_virtual_type_structural_joint
  adjacency:
    text: adjacency
    description: Topological adjacency relation without implying a physical opening.
    meaning: pbs:connection_virtual_type_adjacency
  access:
    text: access
    description: Access relation indicating passability or navigational linkage.
    meaning: pbs:connection_virtual_type_access
  other:
    text: other
    description: Other virtual connection semantics not covered by the controlled
      values.
    meaning: pbs:connection_virtual_type_other

```
</details>

</div>
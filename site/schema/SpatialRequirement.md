---
search:
  boost: 10.0
---

# Class: SpatialRequirement 


_Spatial constraint requirement (min area, min height, adjacency, etc.)._



<div data-search-exclude markdown="1">



URI: [pbs:SpatialRequirement](https://schema.pragmaticbim.ch/SpatialRequirement)





```mermaid
 classDiagram
    class SpatialRequirement
    click SpatialRequirement href "./SpatialRequirement.html"
      Requirement <|-- SpatialRequirement
        click Requirement href "./Requirement.html"
      SpatialRequirement : adjacency_kind
        SpatialRequirement --> "0..1" SpatialAdjacencyKind : adjacency_kind
        click SpatialAdjacencyKind href "./SpatialAdjacencyKind.html"
      SpatialRequirement : applies_to_entities
        SpatialRequirement --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      SpatialRequirement : description
      SpatialRequirement : id
      SpatialRequirement : min_area
      SpatialRequirement : min_clear_distance
      SpatialRequirement : min_height
      SpatialRequirement : name
      SpatialRequirement : related_entity
        SpatialRequirement --> "0..1" Entity : related_entity
        click Entity href "./Entity.html"
      SpatialRequirement : source_document
      SpatialRequirement : status
        SpatialRequirement --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
```





## Inheritance
* [Requirement](Requirement.md)
    * **SpatialRequirement**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:SpatialRequirement](https://schema.pragmaticbim.ch/SpatialRequirement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [min_area](min_area.md) | 0..1 <br/> [Double](Double.md) | Minimum required area in square metres. | direct |
| [min_height](min_height.md) | 0..1 <br/> [Double](Double.md) | Minimum required height or clear height in metres. | direct |
| [adjacency_kind](adjacency_kind.md) | 0..1 <br/> [SpatialAdjacencyKind](SpatialAdjacencyKind.md) | Adjacency semantics when this spatial requirement involves another subject. | direct |
| [related_entity](related_entity.md) | 0..1 <br/> [Entity](Entity.md) | Entity or space subject for adjacency or distance constraints. | direct |
| [min_clear_distance](min_clear_distance.md) | 0..1 <br/> [Double](Double.md) | Minimum clear distance in metres when adjacency_kind is min_clear_distance. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Requirement](Requirement.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | [Requirement](Requirement.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | [Requirement](Requirement.md) |
| [applies_to_entities](applies_to_entities.md) | * <br/> [Entity](Entity.md) | Model entities this record applies to (requirements, cost items, schedule items, etc.). | [Requirement](Requirement.md) |
| [source_document](source_document.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional URI to norm, brief, or source document backing this requirement. | [Requirement](Requirement.md) |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status. | [Requirement](Requirement.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:SpatialRequirement |
| native | pbs:SpatialRequirement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SpatialRequirement
description: Spatial constraint requirement (min area, min height, adjacency, etc.).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
slots:
- min_area
- min_height
- adjacency_kind
- related_entity
- min_clear_distance
class_uri: pbs:SpatialRequirement

```
</details>

### Induced

<details>
```yaml
name: SpatialRequirement
description: Spatial constraint requirement (min area, min height, adjacency, etc.).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
attributes:
  min_area:
    name: min_area
    description: Minimum required area in square metres.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - SpatialRequirement
    range: double
    minimum_value: 0
  min_height:
    name: min_height
    description: Minimum required height or clear height in metres.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - SpatialRequirement
    range: double
    minimum_value: 0
  adjacency_kind:
    name: adjacency_kind
    description: Adjacency semantics when this spatial requirement involves another
      subject.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - SpatialRequirement
    range: SpatialAdjacencyKind
  related_entity:
    name: related_entity
    description: Entity or space subject for adjacency or distance constraints.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - SpatialRequirement
    range: Entity
    inlined: false
  min_clear_distance:
    name: min_clear_distance
    description: Minimum clear distance in metres when adjacency_kind is min_clear_distance.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - SpatialRequirement
    range: double
    minimum_value: 0
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: SpatialRequirement
    domain_of:
    - Entity
    - Task
    - Document
    - Requirement
    - Change
    - ChangeSet
    range: string
    required: true
  name:
    name: name
    description: Default display name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - Entity
    - Requirement
    range: string
    required: true
  description:
    name: description
    description: Default description text.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - Entity
    - Requirement
    range: string
  applies_to_entities:
    name: applies_to_entities
    description: Model entities this record applies to (requirements, cost items,
      schedule items, etc.).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - Requirement
    - TimeRecord
    - CostRecord
    range: Entity
    multivalued: true
    inlined: false
  source_document:
    name: source_document
    description: Optional URI to norm, brief, or source document backing this requirement.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - Requirement
    range: uriorcurie
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: SpatialRequirement
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:SpatialRequirement

```
</details></div>
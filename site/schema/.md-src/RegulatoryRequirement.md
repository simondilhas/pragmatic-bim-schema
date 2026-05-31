---
search:
  boost: 10.0
---

# Class: RegulatoryRequirement 


_Regulatory reference requirement (building code, norm, standard)._



<div data-search-exclude markdown="1">



URI: [pbs:RegulatoryRequirement](https://schema.pragmaticbim.ch/RegulatoryRequirement)





```mermaid
 classDiagram
    class RegulatoryRequirement
    click RegulatoryRequirement href "./RegulatoryRequirement.html"
      Requirement <|-- RegulatoryRequirement
        click Requirement href "./Requirement.html"
      RegulatoryRequirement : applies_to_entities
        RegulatoryRequirement --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      RegulatoryRequirement : clause_ref
      RegulatoryRequirement : description
      RegulatoryRequirement : id
      RegulatoryRequirement : jurisdiction
      RegulatoryRequirement : name
      RegulatoryRequirement : norm_uri
      RegulatoryRequirement : requirement_domain
      RegulatoryRequirement : source_document
      RegulatoryRequirement : status
        RegulatoryRequirement --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
```





## Inheritance
* [Requirement](Requirement.md)
    * **RegulatoryRequirement**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:RegulatoryRequirement](https://schema.pragmaticbim.ch/RegulatoryRequirement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [norm_uri](norm_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI identifying the norm, standard, or building code. | direct |
| [clause_ref](clause_ref.md) | 0..1 <br/> [String](String.md) | Clause, article, or section reference within the norm. | direct |
| [jurisdiction](jurisdiction.md) | 0..1 <br/> [String](String.md) | Jurisdiction or authority scope for the regulatory requirement. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Requirement](Requirement.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | [Requirement](Requirement.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | [Requirement](Requirement.md) |
| [requirement_domain](requirement_domain.md) | 1 <br/> [String](String.md) | Domain of this requirement record (performance, spatial, regulatory, brief). | [Requirement](Requirement.md) |
| [applies_to_entities](applies_to_entities.md) | * <br/> [Entity](Entity.md) | Model entities this record applies to (requirements, cost items, schedule items, etc.). | [Requirement](Requirement.md) |
| [source_document](source_document.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional URI to norm, brief, or source document backing this requirement. | [Requirement](Requirement.md) |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status. | [Requirement](Requirement.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:RegulatoryRequirement |
| native | pbs:RegulatoryRequirement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RegulatoryRequirement
description: Regulatory reference requirement (building code, norm, standard).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
slots:
- norm_uri
- clause_ref
- jurisdiction
slot_usage:
  requirement_domain:
    name: requirement_domain
    range: string
    equals_string: regulatory
class_uri: pbs:RegulatoryRequirement

```
</details>

### Induced

<details>
```yaml
name: RegulatoryRequirement
description: Regulatory reference requirement (building code, norm, standard).
from_schema: https://schema.pragmaticbim.ch
is_a: Requirement
slot_usage:
  requirement_domain:
    name: requirement_domain
    range: string
    equals_string: regulatory
attributes:
  norm_uri:
    name: norm_uri
    description: URI identifying the norm, standard, or building code.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - RegulatoryRequirement
    range: uriorcurie
  clause_ref:
    name: clause_ref
    description: Clause, article, or section reference within the norm.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - RegulatoryRequirement
    range: string
  jurisdiction:
    name: jurisdiction
    description: Jurisdiction or authority scope for the regulatory requirement.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - RegulatoryRequirement
    range: string
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: RegulatoryRequirement
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
    owner: RegulatoryRequirement
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
    owner: RegulatoryRequirement
    domain_of:
    - Entity
    - Requirement
    range: string
  requirement_domain:
    name: requirement_domain
    description: Domain of this requirement record (performance, spatial, regulatory,
      brief).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - Requirement
    range: string
    required: true
    equals_string: regulatory
  applies_to_entities:
    name: applies_to_entities
    description: Model entities this record applies to (requirements, cost items,
      schedule items, etc.).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - Requirement
    - AbstractTimeRecord
    - AbstractCostRecord
    range: Entity
    multivalued: true
    inlined: false
  source_document:
    name: source_document
    description: Optional URI to norm, brief, or source document backing this requirement.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - Requirement
    range: uriorcurie
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: RegulatoryRequirement
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:RegulatoryRequirement

```
</details></div>
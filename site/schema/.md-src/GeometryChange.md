---
search:
  boost: 10.0
---

# Class: GeometryChange 


_Geometry or representation change for a subject._



<div data-search-exclude markdown="1">



URI: [pbs:GeometryChange](https://schema.pragmaticbim.ch/GeometryChange)





```mermaid
 classDiagram
    class GeometryChange
    click GeometryChange href "./GeometryChange.html"
      Change <|-- GeometryChange
        click Change href "./Change.html"
      GeometryChange : affected_geometry_role
        GeometryChange --> "0..1" GeometryRepresentationType : affected_geometry_role
        click GeometryRepresentationType href "./GeometryRepresentationType.html"
      GeometryChange : affected_subject_id
      GeometryChange : affected_subject_path
      GeometryChange : affected_subject_type
      GeometryChange : change_severity
        GeometryChange --> "0..1" ChangeSeverity : change_severity
        click ChangeSeverity href "./ChangeSeverity.html"
      GeometryChange : change_source
      GeometryChange : change_type
      GeometryChange : detected_at
      GeometryChange : document_storage_link
      GeometryChange : from_revision
      GeometryChange : from_state_ref
        GeometryChange --> "0..1" StateRef : from_state_ref
        click StateRef href "./StateRef.html"
      GeometryChange : id
      GeometryChange : ifc_global_id
      GeometryChange : intent_verdict
        GeometryChange --> "0..1" ChangeIntentVerdict : intent_verdict
        click ChangeIntentVerdict href "./ChangeIntentVerdict.html"
      GeometryChange : to_revision
      GeometryChange : to_state_ref
        GeometryChange --> "0..1" StateRef : to_state_ref
        click StateRef href "./StateRef.html"
      GeometryChange : triggered_process
      GeometryChange : triggered_task
```





## Inheritance
* [Change](Change.md)
    * **GeometryChange**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:GeometryChange](https://schema.pragmaticbim.ch/GeometryChange) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [affected_geometry_role](affected_geometry_role.md) | 0..1 <br/> [GeometryRepresentationType](GeometryRepresentationType.md) | Geometry role affected when change_type is geometry_change. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Change](Change.md) |
| [change_type](change_type.md) | 1 <br/> [String](String.md) | Category of change detected between two revisions. | [Change](Change.md) |
| [change_severity](change_severity.md) | 0..1 <br/> [ChangeSeverity](ChangeSeverity.md) | Optional severity independent of change type. | [Change](Change.md) |
| [intent_verdict](intent_verdict.md) | 0..1 <br/> [ChangeIntentVerdict](ChangeIntentVerdict.md) | Intent stability verdict from an automated judge (for example iterthink STABLE/NEW). | [Change](Change.md) |
| [affected_subject_id](affected_subject_id.md) | 1 <br/> [String](String.md) | Identifier of the changed subject (entity id, document id, or external key). | [Change](Change.md) |
| [affected_subject_type](affected_subject_type.md) | 1 <br/> [String](String.md) | LinkML class name of the changed subject (for example Space, SeparatorWall, Document). | [Change](Change.md) |
| [affected_subject_path](affected_subject_path.md) | 0..1 <br/> [String](String.md) | Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1). | [Change](Change.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | [Change](Change.md) |
| [document_storage_link](document_storage_link.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Document location when the subject is or embeds a Document. | [Change](Change.md) |
| [from_revision](from_revision.md) | 1 <br/> [Integer](Integer.md) | Source revision number for this change. | [Change](Change.md) |
| [to_revision](to_revision.md) | 1 <br/> [Integer](Integer.md) | Target revision number for this change. | [Change](Change.md) |
| [from_state_ref](from_state_ref.md) | 0..1 <br/> [StateRef](StateRef.md) | Content state pointer at the source revision. | [Change](Change.md) |
| [to_state_ref](to_state_ref.md) | 0..1 <br/> [StateRef](StateRef.md) | Content state pointer at the target revision. | [Change](Change.md) |
| [triggered_task](triggered_task.md) | 0..1 <br/> [String](String.md) | Id of a Task record that this change triggered or should trigger. | [Change](Change.md) |
| [triggered_process](triggered_process.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | External workflow process URI (for example yourcompanyos process instance). | [Change](Change.md) |
| [detected_at](detected_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Timestamp when this change was detected. | [Change](Change.md) |
| [change_source](change_source.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | URI identifying the tool or pipeline that produced this change record. | [Change](Change.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:GeometryChange |
| native | pbs:GeometryChange |
| exact | prov:Activity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeometryChange
description: Geometry or representation change for a subject.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
slots:
- affected_geometry_role
slot_usage:
  change_type:
    name: change_type
    range: string
    equals_string: geometry_change
class_uri: pbs:GeometryChange

```
</details>

### Induced

<details>
```yaml
name: GeometryChange
description: Geometry or representation change for a subject.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
slot_usage:
  change_type:
    name: change_type
    range: string
    equals_string: geometry_change
attributes:
  affected_geometry_role:
    name: affected_geometry_role
    description: Geometry role affected when change_type is geometry_change.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - GeometryChange
    range: GeometryRepresentationType
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: GeometryChange
    domain_of:
    - Entity
    - Task
    - Document
    - Requirement
    - Change
    - ChangeSet
    range: string
    required: true
  change_type:
    name: change_type
    description: Category of change detected between two revisions.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: string
    required: true
    equals_string: geometry_change
  change_severity:
    name: change_severity
    description: Optional severity independent of change type.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: ChangeSeverity
  intent_verdict:
    name: intent_verdict
    description: Intent stability verdict from an automated judge (for example iterthink
      STABLE/NEW).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: ChangeIntentVerdict
  affected_subject_id:
    name: affected_subject_id
    description: Identifier of the changed subject (entity id, document id, or external
      key).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: string
    required: true
  affected_subject_type:
    name: affected_subject_type
    description: 'LinkML class name of the changed subject (for example Space, SeparatorWall,
      Document).

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: string
    required: true
  affected_subject_path:
    name: affected_subject_path
    description: 'Optional JSON-pointer-style path for nested targets (for example
      documents[2], localized_descriptions[de], section.4.2.paragraph_1).

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: string
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Entity
    - Change
    range: string
    pattern: ^[0-3][0-9A-Za-z_$]{21}$
  document_storage_link:
    name: document_storage_link
    description: Document location when the subject is or embeds a Document.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: uriorcurie
  from_revision:
    name: from_revision
    description: Source revision number for this change.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    - ChangeSet
    range: integer
    required: true
    minimum_value: 0
  to_revision:
    name: to_revision
    description: Target revision number for this change.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    - ChangeSet
    range: integer
    required: true
    minimum_value: 0
  from_state_ref:
    name: from_state_ref
    description: Content state pointer at the source revision.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: StateRef
    inlined: true
  to_state_ref:
    name: to_state_ref
    description: Content state pointer at the target revision.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: StateRef
    inlined: true
  triggered_task:
    name: triggered_task
    description: Id of a Task record that this change triggered or should trigger.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: string
  triggered_process:
    name: triggered_process
    description: External workflow process URI (for example yourcompanyos process
      instance).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: uriorcurie
  detected_at:
    name: detected_at
    description: Timestamp when this change was detected.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: dcterms:created
    owner: GeometryChange
    domain_of:
    - Change
    range: datetime
  change_source:
    name: change_source
    description: URI identifying the tool or pipeline that produced this change record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: GeometryChange
    domain_of:
    - Change
    range: uriorcurie
class_uri: pbs:GeometryChange

```
</details></div>
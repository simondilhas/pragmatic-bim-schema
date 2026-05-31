---
search:
  boost: 10.0
---

# Class: MatchChange 


_Entity match status against a requirement changed (previously met / no longer meets)._

__



<div data-search-exclude markdown="1">



URI: [pbs:MatchChange](https://schema.pragmaticbim.ch/MatchChange)





```mermaid
 classDiagram
    class MatchChange
    click MatchChange href "./MatchChange.html"
      Change <|-- MatchChange
        click Change href "./Change.html"
      MatchChange : affected_subject_id
      MatchChange : affected_subject_path
      MatchChange : affected_subject_type
      MatchChange : change_severity
        MatchChange --> "0..1" ChangeSeverity : change_severity
        click ChangeSeverity href "./ChangeSeverity.html"
      MatchChange : change_source
      MatchChange : change_type
        MatchChange --> "1" ChangeType : change_type
        click ChangeType href "./ChangeType.html"
      MatchChange : detected_at
      MatchChange : document_storage_link
      MatchChange : from_revision
      MatchChange : id
      MatchChange : ifc_global_id
      MatchChange : intent_verdict
        MatchChange --> "0..1" ChangeIntentVerdict : intent_verdict
        click ChangeIntentVerdict href "./ChangeIntentVerdict.html"
      MatchChange : match_status
        MatchChange --> "1" MatchStatus : match_status
        click MatchStatus href "./MatchStatus.html"
      MatchChange : related_requirement_id
      MatchChange : to_revision
      MatchChange : triggered_process
      MatchChange : triggered_task
```





## Inheritance
* [Change](Change.md)
    * **MatchChange**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:MatchChange](https://schema.pragmaticbim.ch/MatchChange) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [related_requirement_id](related_requirement_id.md) | 1 <br/> [String](String.md) | Requirement identifier for match_change records. | direct |
| [match_status](match_status.md) | 1 <br/> [MatchStatus](MatchStatus.md) | Whether the subject met the requirement at the target revision. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Change](Change.md) |
| [change_type](change_type.md) | 1 <br/> [ChangeType](ChangeType.md) | Category of change detected between two revisions. | [Change](Change.md) |
| [change_severity](change_severity.md) | 0..1 <br/> [ChangeSeverity](ChangeSeverity.md) | Optional severity independent of change type. | [Change](Change.md) |
| [intent_verdict](intent_verdict.md) | 0..1 <br/> [ChangeIntentVerdict](ChangeIntentVerdict.md) | Intent stability verdict from an automated judge (for example iterthink STABLE/NEW). | [Change](Change.md) |
| [affected_subject_id](affected_subject_id.md) | 1 <br/> [String](String.md) | Identifier of the changed subject (entity id, document id, or external key). | [Change](Change.md) |
| [affected_subject_type](affected_subject_type.md) | 1 <br/> [String](String.md) | LinkML class name of the changed subject (for example Space, SeparatorWall, Document). | [Change](Change.md) |
| [affected_subject_path](affected_subject_path.md) | 0..1 <br/> [String](String.md) | Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1). | [Change](Change.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | [Change](Change.md) |
| [document_storage_link](document_storage_link.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Document location when the subject is or embeds a Document. | [Change](Change.md) |
| [from_revision](from_revision.md) | 1 <br/> [Integer](Integer.md) | Source revision number for this change. | [Change](Change.md) |
| [to_revision](to_revision.md) | 1 <br/> [Integer](Integer.md) | Target revision number for this change. | [Change](Change.md) |
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
| self | pbs:MatchChange |
| native | pbs:MatchChange |
| exact | prov:Activity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MatchChange
description: 'Entity match status against a requirement changed (previously met /
  no longer meets).

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
slots:
- related_requirement_id
- match_status
class_uri: pbs:MatchChange

```
</details>

### Induced

<details>
```yaml
name: MatchChange
description: 'Entity match status against a requirement changed (previously met /
  no longer meets).

  '
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
attributes:
  related_requirement_id:
    name: related_requirement_id
    description: Requirement identifier for match_change records.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - MatchChange
    range: string
    required: true
  match_status:
    name: match_status
    description: Whether the subject met the requirement at the target revision.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - MatchChange
    range: MatchStatus
    required: true
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: MatchChange
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
    owner: MatchChange
    domain_of:
    - Change
    range: ChangeType
    required: true
  change_severity:
    name: change_severity
    description: Optional severity independent of change type.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - Change
    range: ChangeSeverity
  intent_verdict:
    name: intent_verdict
    description: Intent stability verdict from an automated judge (for example iterthink
      STABLE/NEW).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - Change
    range: ChangeIntentVerdict
  affected_subject_id:
    name: affected_subject_id
    description: Identifier of the changed subject (entity id, document id, or external
      key).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
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
    owner: MatchChange
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
    owner: MatchChange
    domain_of:
    - Change
    range: string
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
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
    owner: MatchChange
    domain_of:
    - Change
    range: uriorcurie
  from_revision:
    name: from_revision
    description: Source revision number for this change.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
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
    owner: MatchChange
    domain_of:
    - Change
    - ChangeSet
    range: integer
    required: true
    minimum_value: 0
  triggered_task:
    name: triggered_task
    description: Id of a Task record that this change triggered or should trigger.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - Change
    range: string
  triggered_process:
    name: triggered_process
    description: External workflow process URI (for example yourcompanyos process
      instance).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - Change
    range: uriorcurie
  detected_at:
    name: detected_at
    description: Timestamp when this change was detected.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: dcterms:created
    owner: MatchChange
    domain_of:
    - Change
    range: datetime
  change_source:
    name: change_source
    description: URI identifying the tool or pipeline that produced this change record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: MatchChange
    domain_of:
    - Change
    range: uriorcurie
class_uri: pbs:MatchChange

```
</details></div>
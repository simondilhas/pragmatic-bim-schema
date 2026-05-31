---
search:
  boost: 10.0
---

# Class: PropertyChange 


_Attribute, PropertySet, schema slot, or document field change._



<div data-search-exclude markdown="1">



URI: [pbs:PropertyChange](https://schema.pragmaticbim.ch/PropertyChange)





```mermaid
 classDiagram
    class PropertyChange
    click PropertyChange href "./PropertyChange.html"
      Change <|-- PropertyChange
        click Change href "./Change.html"
      PropertyChange : affected_subject_id
      PropertyChange : affected_subject_path
      PropertyChange : affected_subject_type
      PropertyChange : change_severity
        PropertyChange --> "0..1" ChangeSeverity : change_severity
        click ChangeSeverity href "./ChangeSeverity.html"
      PropertyChange : change_source
      PropertyChange : change_type
        PropertyChange --> "1" ChangeType : change_type
        click ChangeType href "./ChangeType.html"
      PropertyChange : detected_at
      PropertyChange : document_storage_link
      PropertyChange : from_revision
      PropertyChange : from_value
      PropertyChange : id
      PropertyChange : ifc_attribute_name
      PropertyChange : ifc_global_id
      PropertyChange : intent_verdict
        PropertyChange --> "0..1" ChangeIntentVerdict : intent_verdict
        click ChangeIntentVerdict href "./ChangeIntentVerdict.html"
      PropertyChange : property_path
      PropertyChange : property_path_kind
        PropertyChange --> "1" PropertyPathKind : property_path_kind
        click PropertyPathKind href "./PropertyPathKind.html"
      PropertyChange : source_property
      PropertyChange : source_pset
      PropertyChange : to_revision
      PropertyChange : to_value
      PropertyChange : triggered_process
      PropertyChange : triggered_task
```





## Inheritance
* [Change](Change.md)
    * **PropertyChange**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:PropertyChange](https://schema.pragmaticbim.ch/PropertyChange) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [property_path](property_path.md) | 1 <br/> [String](String.md) | Canonical path to the changed field. Examples: Pset_WallCommon.FireRating, IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389. | direct |
| [property_path_kind](property_path_kind.md) | 1 <br/> [PropertyPathKind](PropertyPathKind.md) | Classification of the property path for downstream diff interpretation. | direct |
| [from_value](from_value.md) | 0..1 <br/> [String](String.md) | Prior value serialized as text. Absent or null for new subjects or fields. | direct |
| [to_value](to_value.md) | 0..1 <br/> [String](String.md) | New value serialized as text. Absent or null for deleted subjects or fields. | direct |
| [source_pset](source_pset.md) | 0..1 <br/> [String](String.md) | IFC PropertySet name when property_path_kind is ifc_pset. | direct |
| [source_property](source_property.md) | 0..1 <br/> [String](String.md) | IFC property name within the PropertySet when property_path_kind is ifc_pset. | direct |
| [ifc_attribute_name](ifc_attribute_name.md) | 0..1 <br/> [String](String.md) | IFC attribute name when property_path_kind is ifc_attribute (for example Name, GlobalId). | direct |
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
| self | pbs:PropertyChange |
| native | pbs:PropertyChange |
| exact | prov:Activity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PropertyChange
description: Attribute, PropertySet, schema slot, or document field change.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
slots:
- property_path
- property_path_kind
- from_value
- to_value
- source_pset
- source_property
- ifc_attribute_name
slot_usage:
  property_path:
    name: property_path
    required: true
  property_path_kind:
    name: property_path_kind
    required: true
  source_pset:
    name: source_pset
    description: IFC PropertySet name when property_path_kind is ifc_pset.
  source_property:
    name: source_property
    description: IFC property name within the PropertySet when property_path_kind
      is ifc_pset.
class_uri: pbs:PropertyChange

```
</details>

### Induced

<details>
```yaml
name: PropertyChange
description: Attribute, PropertySet, schema slot, or document field change.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- prov:Activity
is_a: Change
slot_usage:
  property_path:
    name: property_path
    required: true
  property_path_kind:
    name: property_path_kind
    required: true
  source_pset:
    name: source_pset
    description: IFC PropertySet name when property_path_kind is ifc_pset.
  source_property:
    name: source_property
    description: IFC property name within the PropertySet when property_path_kind
      is ifc_pset.
attributes:
  property_path:
    name: property_path
    description: 'Canonical path to the changed field. Examples: Pset_WallCommon.FireRating,
      IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PropertyChange
    - RequirementChange
    range: string
    required: true
  property_path_kind:
    name: property_path_kind
    description: Classification of the property path for downstream diff interpretation.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PropertyChange
    - RequirementChange
    range: PropertyPathKind
    required: true
  from_value:
    name: from_value
    description: Prior value serialized as text. Absent or null for new subjects or
      fields.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PropertyChange
    - RequirementChange
    range: string
  to_value:
    name: to_value
    description: New value serialized as text. Absent or null for deleted subjects
      or fields.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PropertyChange
    - RequirementChange
    range: string
  source_pset:
    name: source_pset
    description: IFC PropertySet name when property_path_kind is ifc_pset.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PerformanceProperty
    - PropertyChange
    range: string
  source_property:
    name: source_property
    description: IFC property name within the PropertySet when property_path_kind
      is ifc_pset.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PerformanceProperty
    - PropertyChange
    range: string
  ifc_attribute_name:
    name: ifc_attribute_name
    description: IFC attribute name when property_path_kind is ifc_attribute (for
      example Name, GlobalId).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - PropertyChange
    range: string
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: PropertyChange
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
    owner: PropertyChange
    domain_of:
    - Change
    range: ChangeType
    required: true
  change_severity:
    name: change_severity
    description: Optional severity independent of change type.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - Change
    range: ChangeSeverity
  intent_verdict:
    name: intent_verdict
    description: Intent stability verdict from an automated judge (for example iterthink
      STABLE/NEW).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - Change
    range: ChangeIntentVerdict
  affected_subject_id:
    name: affected_subject_id
    description: Identifier of the changed subject (entity id, document id, or external
      key).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
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
    owner: PropertyChange
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
    owner: PropertyChange
    domain_of:
    - Change
    range: string
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
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
    owner: PropertyChange
    domain_of:
    - Change
    range: uriorcurie
  from_revision:
    name: from_revision
    description: Source revision number for this change.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
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
    owner: PropertyChange
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
    owner: PropertyChange
    domain_of:
    - Change
    range: string
  triggered_process:
    name: triggered_process
    description: External workflow process URI (for example yourcompanyos process
      instance).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - Change
    range: uriorcurie
  detected_at:
    name: detected_at
    description: Timestamp when this change was detected.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    slot_uri: dcterms:created
    owner: PropertyChange
    domain_of:
    - Change
    range: datetime
  change_source:
    name: change_source
    description: URI identifying the tool or pipeline that produced this change record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PropertyChange
    domain_of:
    - Change
    range: uriorcurie
class_uri: pbs:PropertyChange

```
</details></div>
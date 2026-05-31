---
search:
  boost: 10.0
---

# Class: Entity 


_Common base class for all schema entities._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [pbs:Entity](https://schema.pragmaticbim.ch/Entity)





```mermaid
 classDiagram
    class Entity
    click Entity href "./Entity.html"
      Entity <|-- Agent
        click Agent href "./Agent.html"
      Entity <|-- Message
        click Message href "./Message.html"
      Entity <|-- PhysicalElement
        click PhysicalElement href "./PhysicalElement.html"
      Entity <|-- VirtualEntity
        click VirtualEntity href "./VirtualEntity.html"
      Entity : classifications
        Entity --> "*" Classification : classifications
        click Classification href "./Classification.html"
      Entity : created_at
      Entity : decisions
        Entity --> "*" Decision : decisions
        click Decision href "./Decision.html"
      Entity : description
      Entity : documents
        Entity --> "*" Document : documents
        click Document href "./Document.html"
      Entity : geometry_representations
        Entity --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      Entity : id
      Entity : ifc_global_id
      Entity : localized_descriptions
        Entity --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      Entity : localized_names
        Entity --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      Entity : meaning_uri
      Entity : messages
        Entity --> "*" Message : messages
        click Message href "./Message.html"
      Entity : metadata
        Entity --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      Entity : modified_at
      Entity : name
      Entity : performance_properties
        Entity --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      Entity : quantity_values
        Entity --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      Entity : revision
      Entity : status
        Entity --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      Entity : tasks
        Entity --> "*" Task : tasks
        click Task href "./Task.html"
```





## Inheritance
* **Entity**
    * [Agent](Agent.md)
    * [Message](Message.md)
    * [PhysicalElement](PhysicalElement.md)
    * [VirtualEntity](VirtualEntity.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Entity](https://schema.pragmaticbim.ch/Entity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | direct |
| [localized_names](localized_names.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of name. | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | direct |
| [meaning_uri](meaning_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional semantic URI for linking the entity instance to an external ontology concept. | direct |
| [localized_descriptions](localized_descriptions.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of description. | direct |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | direct |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes. | direct |
| [geometry_representations](geometry_representations.md) | * <br/> [GeometryRepresentation](GeometryRepresentation.md) | Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself. | direct |
| [quantity_values](quantity_values.md) | * <br/> [QuantityValue](QuantityValue.md) | Quantities associated with the entity. | direct |
| [documents](documents.md) | * <br/> [Document](Document.md) | Linked documents associated with this entity. | direct |
| [metadata](metadata.md) | * <br/> [MetadataEntry](MetadataEntry.md) | Generic metadata container for IFC attributes/properties and project-specific extensions. | direct |
| [performance_properties](performance_properties.md) | * <br/> [PerformanceProperty](PerformanceProperty.md) | Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values. | direct |
| [decisions](decisions.md) | * <br/> [Decision](Decision.md) | Decision records associated with this entity. | direct |
| [tasks](tasks.md) | * <br/> [Task](Task.md) | Tasks associated with this entity. | direct |
| [messages](messages.md) | * <br/> [Message](Message.md) | Messages associated with this entity. | direct |
| [created_at](created_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Creation timestamp for this entity record. | direct |
| [modified_at](modified_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Last modification timestamp for this entity record. | direct |
| [revision](revision.md) | 0..1 <br/> [Integer](Integer.md) | Integer revision counter for change tracking. | direct |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Requirement](Requirement.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [PerformanceRequirement](PerformanceRequirement.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [SpatialRequirement](SpatialRequirement.md) | [related_entity](related_entity.md) | range | [Entity](Entity.md) |
| [SpatialRequirement](SpatialRequirement.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [RegulatoryRequirement](RegulatoryRequirement.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [BriefRequirement](BriefRequirement.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [SpatialContext](SpatialContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [ProjectContext](ProjectContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [PerimeterContext](PerimeterContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [LegalSiteContext](LegalSiteContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [BuildingContext](BuildingContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [CivilStructureContext](CivilStructureContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [LevelContext](LevelContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [ZoneContext](ZoneContext.md) | [group_members](group_members.md) | range | [Entity](Entity.md) |
| [Space](Space.md) | [contained_entities](contained_entities.md) | range | [Entity](Entity.md) |
| [System](System.md) | [contained_entities](contained_entities.md) | range | [Entity](Entity.md) |
| [TimeRecord](TimeRecord.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |
| [CostRecord](CostRecord.md) | [applies_to_entities](applies_to_entities.md) | range | [Entity](Entity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Entity |
| native | pbs:Entity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Entity
description: Common base class for all schema entities.
from_schema: https://schema.pragmaticbim.ch
abstract: true
slots:
- id
- name
- localized_names
- description
- meaning_uri
- localized_descriptions
- ifc_global_id
- classifications
- geometry_representations
- quantity_values
- documents
- metadata
- performance_properties
- decisions
- tasks
- messages
- created_at
- modified_at
- revision
- status
class_uri: pbs:Entity

```
</details>

### Induced

<details>
```yaml
name: Entity
description: Common base class for all schema entities.
from_schema: https://schema.pragmaticbim.ch
abstract: true
attributes:
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: Entity
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
    owner: Entity
    domain_of:
    - Entity
    - Requirement
    range: string
    required: true
  localized_names:
    name: localized_names
    description: Localized variants of name.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  description:
    name: description
    description: Default description text.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    - Requirement
    range: string
  meaning_uri:
    name: meaning_uri
    description: Optional semantic URI for linking the entity instance to an external
      ontology concept.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: LocalizedText
    multivalued: true
    inlined: true
  ifc_global_id:
    name: ifc_global_id
    description: IFC GlobalId of the mapped entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    - Change
    range: string
    pattern: ^[0-3][0-9A-Za-z_$]{21}$
  classifications:
    name: classifications
    description: Classification entries from IFC and other schemes.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    - Document
    range: Classification
    multivalued: true
    inlined: true
  geometry_representations:
    name: geometry_representations
    description: 'Geometry references associated with the entity. A single element
      may link to multiple geometry representations to serve different intents (authoring,
      coordination, analysis, visualization) without duplicating the element itself.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: GeometryRepresentation
    multivalued: true
    inlined: true
  quantity_values:
    name: quantity_values
    description: Quantities associated with the entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: QuantityValue
    multivalued: true
    inlined: true
  documents:
    name: documents
    description: Linked documents associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: Document
    multivalued: true
    inlined: true
  metadata:
    name: metadata
    description: Generic metadata container for IFC attributes/properties and project-specific
      extensions.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: MetadataEntry
    multivalued: true
    inlined: true
  performance_properties:
    name: performance_properties
    description: 'Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/
      security/material) extracted from raw IFC PropertySet values.

      '
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: PerformanceProperty
    multivalued: true
    inlined: true
  decisions:
    name: decisions
    description: Decision records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: Decision
    multivalued: true
    inlined: true
  tasks:
    name: tasks
    description: Tasks associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: Task
    multivalued: true
    inlined: true
  messages:
    name: messages
    description: Messages associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: Message
    multivalued: true
    inlined: true
  created_at:
    name: created_at
    description: Creation timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Entity
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:Entity

```
</details></div>
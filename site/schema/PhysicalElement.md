---
search:
  boost: 10.0
---

# Class: PhysicalElement 


_Base class for physical elements that can be placed in built asset/level context._



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [pbs:PhysicalElement](https://schema.pragmaticbim.ch/PhysicalElement)





```mermaid
 classDiagram
    class PhysicalElement
    click PhysicalElement href "./PhysicalElement.html"
      Entity <|-- PhysicalElement
        click Entity href "./Entity.html"
      PhysicalElement <|-- Separator
        click Separator href "./Separator.html"
      PhysicalElement <|-- ConnectionPhysical
        click ConnectionPhysical href "./ConnectionPhysical.html"
      PhysicalElement <|-- Boundary
        click Boundary href "./Boundary.html"
      PhysicalElement <|-- Equipment
        click Equipment href "./Equipment.html"
      PhysicalElement : classifications
        PhysicalElement --> "*" Classification : classifications
        click Classification href "./Classification.html"
      PhysicalElement : created_at
      PhysicalElement : decisions
        PhysicalElement --> "*" Decision : decisions
        click Decision href "./Decision.html"
      PhysicalElement : description
      PhysicalElement : documents
        PhysicalElement --> "*" Document : documents
        click Document href "./Document.html"
      PhysicalElement : geometry_representations
        PhysicalElement --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      PhysicalElement : id
      PhysicalElement : ifc_global_id
      PhysicalElement : localized_descriptions
        PhysicalElement --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      PhysicalElement : localized_names
        PhysicalElement --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      PhysicalElement : meaning_uri
      PhysicalElement : messages
        PhysicalElement --> "*" Message : messages
        click Message href "./Message.html"
      PhysicalElement : metadata
        PhysicalElement --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      PhysicalElement : modified_at
      PhysicalElement : name
      PhysicalElement : parent_building
        PhysicalElement --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "./BuiltAssetContext.html"
      PhysicalElement : parent_level
        PhysicalElement --> "0..1" LevelContext : parent_level
        click LevelContext href "./LevelContext.html"
      PhysicalElement : performance_properties
        PhysicalElement --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      PhysicalElement : quantity_values
        PhysicalElement --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      PhysicalElement : revision
      PhysicalElement : status
        PhysicalElement --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      PhysicalElement : tasks
        PhysicalElement --> "*" Task : tasks
        click Task href "./Task.html"
```





## Inheritance
* [Entity](Entity.md)
    * **PhysicalElement**
        * [Separator](Separator.md)
        * [ConnectionPhysical](ConnectionPhysical.md)
        * [Boundary](Boundary.md)
        * [Equipment](Equipment.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:PhysicalElement](https://schema.pragmaticbim.ch/PhysicalElement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | direct |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | Unique local identifier. | [Entity](Entity.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Default display name. | [Entity](Entity.md) |
| [localized_names](localized_names.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of name. | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | Default description text. | [Entity](Entity.md) |
| [meaning_uri](meaning_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional semantic URI for linking the entity instance to an external ontology concept. | [Entity](Entity.md) |
| [localized_descriptions](localized_descriptions.md) | * <br/> [LocalizedText](LocalizedText.md) | Localized variants of description. | [Entity](Entity.md) |
| [ifc_global_id](ifc_global_id.md) | 0..1 <br/> [String](String.md) | IFC GlobalId of the mapped entity. | [Entity](Entity.md) |
| [classifications](classifications.md) | * <br/> [Classification](Classification.md) | Classification entries from IFC and other schemes. | [Entity](Entity.md) |
| [geometry_representations](geometry_representations.md) | * <br/> [GeometryRepresentation](GeometryRepresentation.md) | Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself. | [Entity](Entity.md) |
| [quantity_values](quantity_values.md) | * <br/> [QuantityValue](QuantityValue.md) | Quantities associated with the entity. | [Entity](Entity.md) |
| [documents](documents.md) | * <br/> [Document](Document.md) | Linked documents associated with this entity. | [Entity](Entity.md) |
| [metadata](metadata.md) | * <br/> [MetadataEntry](MetadataEntry.md) | Generic metadata container for IFC attributes/properties and project-specific extensions. | [Entity](Entity.md) |
| [performance_properties](performance_properties.md) | * <br/> [PerformanceProperty](PerformanceProperty.md) | Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values. | [Entity](Entity.md) |
| [decisions](decisions.md) | * <br/> [Decision](Decision.md) | Decision records associated with this entity. | [Entity](Entity.md) |
| [tasks](tasks.md) | * <br/> [Task](Task.md) | Tasks associated with this entity. | [Entity](Entity.md) |
| [messages](messages.md) | * <br/> [Message](Message.md) | Messages associated with this entity. | [Entity](Entity.md) |
| [created_at](created_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Creation timestamp for this entity record. | [Entity](Entity.md) |
| [modified_at](modified_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Last modification timestamp for this entity record. | [Entity](Entity.md) |
| [revision](revision.md) | 0..1 <br/> [Integer](Integer.md) | Integer revision counter for change tracking. | [Entity](Entity.md) |
| [status](status.md) | 0..1 <br/> [StatusType](StatusType.md) | Lifecycle or QA status. | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Space](Space.md) | [bounded_by](bounded_by.md) | range | [PhysicalElement](PhysicalElement.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [connects_physical_elements](connects_physical_elements.md) | range | [PhysicalElement](PhysicalElement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:PhysicalElement |
| native | pbs:PhysicalElement |
| exact | bot:Element, ifcowl:IfcElement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalElement
description: Base class for physical elements that can be placed in built asset/level
  context.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Element
- ifcowl:IfcElement
is_a: Entity
abstract: true
slots:
- parent_building
- parent_level
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
class_uri: pbs:PhysicalElement

```
</details>

### Induced

<details>
```yaml
name: PhysicalElement
description: Base class for physical elements that can be placed in built asset/level
  context.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Element
- ifcowl:IfcElement
is_a: Entity
abstract: true
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
attributes:
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    - System
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    description: Parent level/storey context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
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
    owner: PhysicalElement
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PhysicalElement
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:PhysicalElement

```
</details></div>
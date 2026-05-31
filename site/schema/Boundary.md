---
search:
  boost: 10.0
---

# Class: Boundary 


_Physical element acting as a boundary treatment (for example covering)._



<div data-search-exclude markdown="1">



URI: [pbs:Boundary](https://schema.pragmaticbim.ch/Boundary)





```mermaid
 classDiagram
    class Boundary
    click Boundary href "./Boundary.html"
      PhysicalElement <|-- Boundary
        click PhysicalElement href "./PhysicalElement.html"
      Boundary : boundary_type
        Boundary --> "1" BoundaryType : boundary_type
        click BoundaryType href "./BoundaryType.html"
      Boundary : bounded_space
        Boundary --> "0..1" Space : bounded_space
        click Space href "./Space.html"
      Boundary : classifications
        Boundary --> "*" Classification : classifications
        click Classification href "./Classification.html"
      Boundary : created_at
      Boundary : decisions
        Boundary --> "*" Decision : decisions
        click Decision href "./Decision.html"
      Boundary : description
      Boundary : documents
        Boundary --> "*" Document : documents
        click Document href "./Document.html"
      Boundary : geometry_representations
        Boundary --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      Boundary : id
      Boundary : ifc_global_id
      Boundary : localized_descriptions
        Boundary --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      Boundary : localized_names
        Boundary --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      Boundary : meaning_uri
      Boundary : messages
        Boundary --> "*" Message : messages
        click Message href "./Message.html"
      Boundary : metadata
        Boundary --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      Boundary : modified_at
      Boundary : name
      Boundary : parent_building
        Boundary --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "./BuiltAssetContext.html"
      Boundary : parent_level
        Boundary --> "0..1" LevelContext : parent_level
        click LevelContext href "./LevelContext.html"
      Boundary : performance_properties
        Boundary --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      Boundary : quantity_values
        Boundary --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      Boundary : revision
      Boundary : status
        Boundary --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      Boundary : tasks
        Boundary --> "*" Task : tasks
        click Task href "./Task.html"
```





## Inheritance
* [Entity](Entity.md)
    * [PhysicalElement](PhysicalElement.md)
        * **Boundary**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Boundary](https://schema.pragmaticbim.ch/Boundary) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [boundary_type](boundary_type.md) | 1 <br/> [BoundaryType](BoundaryType.md) | Classification of boundary element (e.g., covering). | direct |
| [bounded_space](bounded_space.md) | 0..1 <br/> [Space](Space.md) | Space bounded by this boundary element. | direct |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | [PhysicalElement](PhysicalElement.md) |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | [PhysicalElement](PhysicalElement.md) |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Boundary |
| native | pbs:Boundary |
| exact | ifcowl:IfcCovering |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Boundary
description: Physical element acting as a boundary treatment (for example covering).
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcCovering
is_a: PhysicalElement
slots:
- boundary_type
- bounded_space
class_uri: pbs:Boundary

```
</details>

### Induced

<details>
```yaml
name: Boundary
description: Physical element acting as a boundary treatment (for example covering).
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- ifcowl:IfcCovering
is_a: PhysicalElement
attributes:
  boundary_type:
    name: boundary_type
    description: Classification of boundary element (e.g., covering).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
    domain_of:
    - Boundary
    range: BoundaryType
    required: true
  bounded_space:
    name: bounded_space
    description: Space bounded by this boundary element.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
    domain_of:
    - Boundary
    inverse: bounded_by
    range: Space
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
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
    owner: Boundary
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Boundary
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:Boundary

```
</details></div>
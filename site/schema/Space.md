---
search:
  boost: 10.0
---

# Class: Space 


_Spatial container used for occupancy, circulation, service, or analysis._



<div data-search-exclude markdown="1">



URI: [pbs:Space](https://schema.pragmaticbim.ch/Space)





```mermaid
 classDiagram
    class Space
    click Space href "./Space.html"
      VirtualEntity <|-- Space
        click VirtualEntity href "./VirtualEntity.html"
      Space : bounded_by
        Space --> "*" PhysicalElement : bounded_by
        click PhysicalElement href "./PhysicalElement.html"
      Space : classifications
        Space --> "*" Classification : classifications
        click Classification href "./Classification.html"
      Space : contained_entities
        Space --> "*" Entity : contained_entities
        click Entity href "./Entity.html"
      Space : cost_assemblies
        Space --> "*" CostAssembly : cost_assemblies
        click CostAssembly href "./CostAssembly.html"
      Space : cost_items
        Space --> "*" CostItem : cost_items
        click CostItem href "./CostItem.html"
      Space : created_at
      Space : decisions
        Space --> "*" Decision : decisions
        click Decision href "./Decision.html"
      Space : description
      Space : documents
        Space --> "*" Document : documents
        click Document href "./Document.html"
      Space : geometry_representations
        Space --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      Space : id
      Space : ifc_global_id
      Space : localized_descriptions
        Space --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      Space : localized_names
        Space --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      Space : materials
        Space --> "*" Material : materials
        click Material href "./Material.html"
      Space : meaning_uri
      Space : messages
        Space --> "*" Message : messages
        click Message href "./Message.html"
      Space : metadata
        Space --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      Space : modified_at
      Space : name
      Space : parent_building
        Space --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "./BuiltAssetContext.html"
      Space : parent_level
        Space --> "0..1" LevelContext : parent_level
        click LevelContext href "./LevelContext.html"
      Space : parent_zone
        Space --> "0..1" ZoneContext : parent_zone
        click ZoneContext href "./ZoneContext.html"
      Space : performance_properties
        Space --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      Space : quantity_values
        Space --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      Space : revision
      Space : space_type
        Space --> "1" SpaceType : space_type
        click SpaceType href "./SpaceType.html"
      Space : status
        Space --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      Space : tasks
        Space --> "*" Task : tasks
        click Task href "./Task.html"
      Space : time_items
        Space --> "*" TimeItem : time_items
        click TimeItem href "./TimeItem.html"
      Space : time_plans
        Space --> "*" TimePlan : time_plans
        click TimePlan href "./TimePlan.html"
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * **Space**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:Space](https://schema.pragmaticbim.ch/Space) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [space_type](space_type.md) | 1 <br/> [SpaceType](SpaceType.md) | Classification of space (void, circulation, usable, service). | direct |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | direct |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | direct |
| [parent_zone](parent_zone.md) | 0..1 <br/> [ZoneContext](ZoneContext.md) | Parent zone context reference. | direct |
| [bounded_by](bounded_by.md) | * <br/> [PhysicalElement](PhysicalElement.md) | Physical elements that bound a space. | direct |
| [contained_entities](contained_entities.md) | * <br/> [Entity](Entity.md) | Generic containment for associated entities. | direct |
| [cost_items](cost_items.md) | * <br/> [CostItem](CostItem.md) | Cost items associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [cost_assemblies](cost_assemblies.md) | * <br/> [CostAssembly](CostAssembly.md) | Aggregated unit prices associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [time_items](time_items.md) | * <br/> [TimeItem](TimeItem.md) | Time items associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [time_plans](time_plans.md) | * <br/> [TimePlan](TimePlan.md) | Grouped time plans associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [materials](materials.md) | * <br/> [Material](Material.md) | Material definitions associated with this entity. | [VirtualEntity](VirtualEntity.md) |
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
| [SeparatorWall](SeparatorWall.md) | [separates_spaces](separates_spaces.md) | range | [Space](Space.md) |
| [Boundary](Boundary.md) | [bounded_space](bounded_space.md) | range | [Space](Space.md) |
| [Equipment](Equipment.md) | [parent_space](parent_space.md) | range | [Space](Space.md) |
| [System](System.md) | [serves_spaces](serves_spaces.md) | range | [Space](Space.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [connects_spaces](connects_spaces.md) | range | [Space](Space.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:Space |
| native | pbs:Space |
| exact | bot:Space, ifcowl:IfcSpace |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Space
description: Spatial container used for occupancy, circulation, service, or analysis.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Space
- ifcowl:IfcSpace
is_a: VirtualEntity
slots:
- space_type
- parent_building
- parent_level
- parent_zone
- bounded_by
- contained_entities
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
class_uri: pbs:Space

```
</details>

### Induced

<details>
```yaml
name: Space
description: Spatial container used for occupancy, circulation, service, or analysis.
from_schema: https://schema.pragmaticbim.ch
exact_mappings:
- bot:Space
- ifcowl:IfcSpace
is_a: VirtualEntity
slot_usage:
  parent_building:
    name: parent_building
    range: BuiltAssetContext
  parent_level:
    name: parent_level
    range: LevelContext
attributes:
  space_type:
    name: space_type
    description: Classification of space (void, circulation, usable, service).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    range: SpaceType
    required: true
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
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
    owner: Space
    domain_of:
    - PhysicalElement
    - SpatialContext
    - Space
    range: LevelContext
  parent_zone:
    name: parent_zone
    description: Parent zone context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - SpatialContext
    - Space
    range: ZoneContext
  bounded_by:
    name: bounded_by
    description: Physical elements that bound a space.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    inverse: bounded_space
    range: PhysicalElement
    multivalued: true
  contained_entities:
    name: contained_entities
    description: Generic containment for associated entities.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Space
    - System
    range: Entity
    multivalued: true
  cost_items:
    name: cost_items
    description: Cost items associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - VirtualEntity
    range: CostItem
    multivalued: true
    inlined: false
  cost_assemblies:
    name: cost_assemblies
    description: Aggregated unit prices associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - VirtualEntity
    range: CostAssembly
    multivalued: true
    inlined: false
  time_items:
    name: time_items
    description: Time items associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - VirtualEntity
    range: TimeItem
    multivalued: true
    inlined: false
  time_plans:
    name: time_plans
    description: Grouped time plans associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - VirtualEntity
    range: TimePlan
    multivalued: true
    inlined: false
  materials:
    name: materials
    description: Material definitions associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - VirtualEntity
    range: Material
    multivalued: true
    inlined: false
  id:
    name: id
    description: Unique local identifier.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    identifier: true
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
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
    owner: Space
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: Space
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:Space

```
</details></div>
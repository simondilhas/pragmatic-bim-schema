---
search:
  boost: 10.0
---

# Class: LevelContext 


_Spatial context node constrained to level/storey semantics._



<div data-search-exclude markdown="1">



URI: [pbs:LevelContext](https://schema.pragmaticbim.ch/LevelContext)





```mermaid
 classDiagram
    class LevelContext
    click LevelContext href "./LevelContext.html"
      SpatialContext <|-- LevelContext
        click SpatialContext href "./SpatialContext.html"
      LevelContext : classifications
        LevelContext --> "*" Classification : classifications
        click Classification href "./Classification.html"
      LevelContext : context_type
        LevelContext --> "1" ContextType : context_type
        click ContextType href "./ContextType.html"
      LevelContext : cost_records
        LevelContext --> "*" CostRecord : cost_records
        click CostRecord href "./CostRecord.html"
      LevelContext : created_at
      LevelContext : decisions
        LevelContext --> "*" Decision : decisions
        click Decision href "./Decision.html"
      LevelContext : description
      LevelContext : documents
        LevelContext --> "*" Document : documents
        click Document href "./Document.html"
      LevelContext : geometry_representations
        LevelContext --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      LevelContext : group_members
        LevelContext --> "*" Entity : group_members
        click Entity href "./Entity.html"
      LevelContext : id
      LevelContext : ifc_global_id
      LevelContext : localized_descriptions
        LevelContext --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      LevelContext : localized_names
        LevelContext --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      LevelContext : materials
        LevelContext --> "*" Material : materials
        click Material href "./Material.html"
      LevelContext : meaning_uri
      LevelContext : messages
        LevelContext --> "*" Message : messages
        click Message href "./Message.html"
      LevelContext : metadata
        LevelContext --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      LevelContext : modified_at
      LevelContext : name
      LevelContext : parent_building
        LevelContext --> "0..1" BuiltAssetContext : parent_building
        click BuiltAssetContext href "./BuiltAssetContext.html"
      LevelContext : parent_legal_site
        LevelContext --> "0..1" LegalSiteContext : parent_legal_site
        click LegalSiteContext href "./LegalSiteContext.html"
      LevelContext : parent_level
        LevelContext --> "0..1" LevelContext : parent_level
        click LevelContext href "./LevelContext.html"
      LevelContext : parent_perimeter
        LevelContext --> "0..1" PerimeterContext : parent_perimeter
        click PerimeterContext href "./PerimeterContext.html"
      LevelContext : parent_project
        LevelContext --> "0..1" ProjectContext : parent_project
        click ProjectContext href "./ProjectContext.html"
      LevelContext : parent_zone
        LevelContext --> "0..1" ZoneContext : parent_zone
        click ZoneContext href "./ZoneContext.html"
      LevelContext : performance_properties
        LevelContext --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      LevelContext : quantity_values
        LevelContext --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      LevelContext : revision
      LevelContext : status
        LevelContext --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      LevelContext : tasks
        LevelContext --> "*" Task : tasks
        click Task href "./Task.html"
      LevelContext : time_records
        LevelContext --> "*" TimeRecord : time_records
        click TimeRecord href "./TimeRecord.html"
      LevelContext : zone_type
        LevelContext --> "0..1" ZoneType : zone_type
        click ZoneType href "./ZoneType.html"
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * [SpatialContext](SpatialContext.md)
            * **LevelContext**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:LevelContext](https://schema.pragmaticbim.ch/LevelContext) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [context_type](context_type.md) | 1 <br/> [ContextType](ContextType.md) | Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone). | [SpatialContext](SpatialContext.md) |
| [zone_type](zone_type.md) | 0..1 <br/> [ZoneType](ZoneType.md) | Optional zone classification; intended for SpatialContext nodes where context_type is zone. | [SpatialContext](SpatialContext.md) |
| [parent_project](parent_project.md) | 0..1 <br/> [ProjectContext](ProjectContext.md) | Parent project context reference. | [SpatialContext](SpatialContext.md) |
| [parent_perimeter](parent_perimeter.md) | 0..1 <br/> [PerimeterContext](PerimeterContext.md) | Parent perimeter context reference. | [SpatialContext](SpatialContext.md) |
| [parent_legal_site](parent_legal_site.md) | 0..1 <br/> [LegalSiteContext](LegalSiteContext.md) | Parent legal site context reference. | [SpatialContext](SpatialContext.md) |
| [parent_building](parent_building.md) | 0..1 <br/> [BuiltAssetContext](BuiltAssetContext.md) | Parent building context reference. | [SpatialContext](SpatialContext.md) |
| [parent_level](parent_level.md) | 0..1 <br/> [LevelContext](LevelContext.md) | Parent level/storey context reference. | [SpatialContext](SpatialContext.md) |
| [parent_zone](parent_zone.md) | 0..1 <br/> [ZoneContext](ZoneContext.md) | Parent zone context reference. | [SpatialContext](SpatialContext.md) |
| [group_members](group_members.md) | * <br/> [Entity](Entity.md) | Zone members; may include spaces, separations, systems, etc. | [SpatialContext](SpatialContext.md) |
| [cost_records](cost_records.md) | * <br/> [CostRecord](CostRecord.md) | Cost records associated with this entity. | [VirtualEntity](VirtualEntity.md) |
| [time_records](time_records.md) | * <br/> [TimeRecord](TimeRecord.md) | Time records associated with this entity. | [VirtualEntity](VirtualEntity.md) |
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
| [PhysicalElement](PhysicalElement.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [Separator](Separator.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [SeparatorWall](SeparatorWall.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [SeparatorSlab](SeparatorSlab.md) | [separates_levels](separates_levels.md) | range | [LevelContext](LevelContext.md) |
| [SeparatorSlab](SeparatorSlab.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [ConnectionPhysical](ConnectionPhysical.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [Boundary](Boundary.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [Equipment](Equipment.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [SpatialContext](SpatialContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [ProjectContext](ProjectContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [PerimeterContext](PerimeterContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [LegalSiteContext](LegalSiteContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [BuildingContext](BuildingContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [CivilStructureContext](CivilStructureContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [LevelContext](LevelContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [ZoneContext](ZoneContext.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |
| [Space](Space.md) | [parent_level](parent_level.md) | range | [LevelContext](LevelContext.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:LevelContext |
| native | pbs:LevelContext |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LevelContext
description: Spatial context node constrained to level/storey semantics.
from_schema: https://schema.pragmaticbim.ch
is_a: SpatialContext
class_uri: pbs:LevelContext

```
</details>

### Induced

<details>
```yaml
name: LevelContext
description: Spatial context node constrained to level/storey semantics.
from_schema: https://schema.pragmaticbim.ch
is_a: SpatialContext
attributes:
  context_type:
    name: context_type
    description: Classification of context entity (project, perimeter, legal_site,
      building, civil_structure, level, zone).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    range: ContextType
    required: true
  zone_type:
    name: zone_type
    description: Optional zone classification; intended for SpatialContext nodes where
      context_type is zone.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    range: ZoneType
  parent_project:
    name: parent_project
    description: Parent project context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    - System
    range: ProjectContext
  parent_perimeter:
    name: parent_perimeter
    description: Parent perimeter context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    range: PerimeterContext
  parent_legal_site:
    name: parent_legal_site
    description: Parent legal site context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    range: LegalSiteContext
  parent_building:
    name: parent_building
    description: Parent building context reference.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
    domain_of:
    - SpatialContext
    - Space
    range: ZoneContext
  group_members:
    name: group_members
    description: Zone members; may include spaces, separations, systems, etc.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - SpatialContext
    range: Entity
    multivalued: true
  cost_records:
    name: cost_records
    description: Cost records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - VirtualEntity
    range: CostRecord
    multivalued: true
    inlined: false
  time_records:
    name: time_records
    description: Time records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - VirtualEntity
    range: TimeRecord
    multivalued: true
    inlined: false
  materials:
    name: materials
    description: Material definitions associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
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
    owner: LevelContext
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LevelContext
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:LevelContext

```
</details></div>
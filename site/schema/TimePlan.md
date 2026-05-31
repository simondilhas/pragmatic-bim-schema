---
search:
  boost: 10.0
---

# Class: TimePlan 


_Grouped schedule container defining component items, milestones, and dependencies for a scoped plan._



<div data-search-exclude markdown="1">



URI: [pbs:TimePlan](https://schema.pragmaticbim.ch/TimePlan)





```mermaid
 classDiagram
    class TimePlan
    click TimePlan href "./TimePlan.html"
      AbstractTimeRecord <|-- TimePlan
        click AbstractTimeRecord href "./AbstractTimeRecord.html"
      TimePlan : applies_to_entities
        TimePlan --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      TimePlan : classifications
        TimePlan --> "*" Classification : classifications
        click Classification href "./Classification.html"
      TimePlan : component_time_items
        TimePlan --> "*" TimeItem : component_time_items
        click TimeItem href "./TimeItem.html"
      TimePlan : cost_assemblies
        TimePlan --> "*" CostAssembly : cost_assemblies
        click CostAssembly href "./CostAssembly.html"
      TimePlan : cost_items
        TimePlan --> "*" CostItem : cost_items
        click CostItem href "./CostItem.html"
      TimePlan : created_at
      TimePlan : decisions
        TimePlan --> "*" Decision : decisions
        click Decision href "./Decision.html"
      TimePlan : description
      TimePlan : documents
        TimePlan --> "*" Document : documents
        click Document href "./Document.html"
      TimePlan : geometry_representations
        TimePlan --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      TimePlan : id
      TimePlan : ifc_global_id
      TimePlan : localized_descriptions
        TimePlan --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      TimePlan : localized_names
        TimePlan --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      TimePlan : materials
        TimePlan --> "*" Material : materials
        click Material href "./Material.html"
      TimePlan : meaning_uri
      TimePlan : messages
        TimePlan --> "*" Message : messages
        click Message href "./Message.html"
      TimePlan : metadata
        TimePlan --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      TimePlan : modified_at
      TimePlan : name
      TimePlan : performance_properties
        TimePlan --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      TimePlan : quantity_values
        TimePlan --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      TimePlan : revision
      TimePlan : status
        TimePlan --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      TimePlan : tasks
        TimePlan --> "*" Task : tasks
        click Task href "./Task.html"
      TimePlan : time_dependencies
        TimePlan --> "*" TimeDependency : time_dependencies
        click TimeDependency href "./TimeDependency.html"
      TimePlan : time_items
        TimePlan --> "*" TimeItem : time_items
        click TimeItem href "./TimeItem.html"
      TimePlan : time_plans
        TimePlan --> "*" TimePlan : time_plans
        click TimePlan href "./TimePlan.html"
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * [AbstractTimeRecord](AbstractTimeRecord.md)
            * **TimePlan**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:TimePlan](https://schema.pragmaticbim.ch/TimePlan) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [component_time_items](component_time_items.md) | * <br/> [TimeItem](TimeItem.md) | Time items contained in this plan; milestone instances may also appear through the TimeItem subtype. | direct |
| [time_dependencies](time_dependencies.md) | * <br/> [TimeDependency](TimeDependency.md) | Dependency relationships used within this time plan. | direct |
| [applies_to_entities](applies_to_entities.md) | * <br/> [Entity](Entity.md) | Model entities this record applies to (requirements, cost items, schedule items, etc.). | [AbstractTimeRecord](AbstractTimeRecord.md) |
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
| [VirtualEntity](VirtualEntity.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [SpatialContext](SpatialContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [ProjectContext](ProjectContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [PerimeterContext](PerimeterContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [LegalSiteContext](LegalSiteContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [BuildingContext](BuildingContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [CivilStructureContext](CivilStructureContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [LevelContext](LevelContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [ZoneContext](ZoneContext.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [Space](Space.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [System](System.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [AbstractTimeRecord](AbstractTimeRecord.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [TimeItem](TimeItem.md) | [time_plan](time_plan.md) | range | [TimePlan](TimePlan.md) |
| [TimeItem](TimeItem.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [Milestone](Milestone.md) | [time_plan](time_plan.md) | range | [TimePlan](TimePlan.md) |
| [Milestone](Milestone.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [TimePlan](TimePlan.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [TimeDependency](TimeDependency.md) | [time_plan](time_plan.md) | range | [TimePlan](TimePlan.md) |
| [TimeDependency](TimeDependency.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [CostItem](CostItem.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [CostAssembly](CostAssembly.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |
| [Material](Material.md) | [time_plans](time_plans.md) | range | [TimePlan](TimePlan.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:TimePlan |
| native | pbs:TimePlan |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TimePlan
description: Grouped schedule container defining component items, milestones, and
  dependencies for a scoped plan.
from_schema: https://schema.pragmaticbim.ch
is_a: AbstractTimeRecord
slots:
- component_time_items
- time_dependencies
class_uri: pbs:TimePlan

```
</details>

### Induced

<details>
```yaml
name: TimePlan
description: Grouped schedule container defining component items, milestones, and
  dependencies for a scoped plan.
from_schema: https://schema.pragmaticbim.ch
is_a: AbstractTimeRecord
attributes:
  component_time_items:
    name: component_time_items
    description: Time items contained in this plan; milestone instances may also appear
      through the TimeItem subtype.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - TimePlan
    range: TimeItem
    multivalued: true
    inlined: false
  time_dependencies:
    name: time_dependencies
    description: Dependency relationships used within this time plan.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - TimePlan
    range: TimeDependency
    multivalued: true
    inlined: false
  applies_to_entities:
    name: applies_to_entities
    description: Model entities this record applies to (requirements, cost items,
      schedule items, etc.).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - Requirement
    - AbstractTimeRecord
    - AbstractCostRecord
    range: Entity
    multivalued: true
    inlined: false
  cost_items:
    name: cost_items
    description: Cost items associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
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
    owner: TimePlan
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimePlan
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:TimePlan

```
</details></div>
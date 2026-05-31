---
search:
  boost: 10.0
---

# Class: TimeItem 


_Planned work item with baseline and actual dates, optionally linked to model entities and a time plan._



<div data-search-exclude markdown="1">



URI: [pbs:TimeItem](https://schema.pragmaticbim.ch/TimeItem)





```mermaid
 classDiagram
    class TimeItem
    click TimeItem href "./TimeItem.html"
      AbstractTimeRecord <|-- TimeItem
        click AbstractTimeRecord href "./AbstractTimeRecord.html"
      TimeItem <|-- Milestone
        click Milestone href "./Milestone.html"
      TimeItem : actual_finish_at
      TimeItem : actual_start_at
      TimeItem : applies_to_entities
        TimeItem --> "*" Entity : applies_to_entities
        click Entity href "./Entity.html"
      TimeItem : classifications
        TimeItem --> "*" Classification : classifications
        click Classification href "./Classification.html"
      TimeItem : cost_assemblies
        TimeItem --> "*" CostAssembly : cost_assemblies
        click CostAssembly href "./CostAssembly.html"
      TimeItem : cost_items
        TimeItem --> "*" CostItem : cost_items
        click CostItem href "./CostItem.html"
      TimeItem : created_at
      TimeItem : decisions
        TimeItem --> "*" Decision : decisions
        click Decision href "./Decision.html"
      TimeItem : description
      TimeItem : documents
        TimeItem --> "*" Document : documents
        click Document href "./Document.html"
      TimeItem : geometry_representations
        TimeItem --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      TimeItem : id
      TimeItem : ifc_global_id
      TimeItem : localized_descriptions
        TimeItem --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      TimeItem : localized_names
        TimeItem --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      TimeItem : materials
        TimeItem --> "*" Material : materials
        click Material href "./Material.html"
      TimeItem : meaning_uri
      TimeItem : messages
        TimeItem --> "*" Message : messages
        click Message href "./Message.html"
      TimeItem : metadata
        TimeItem --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      TimeItem : modified_at
      TimeItem : name
      TimeItem : performance_properties
        TimeItem --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      TimeItem : planned_finish_at
      TimeItem : planned_start_at
      TimeItem : quantity_values
        TimeItem --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      TimeItem : revision
      TimeItem : status
        TimeItem --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      TimeItem : tasks
        TimeItem --> "*" Task : tasks
        click Task href "./Task.html"
      TimeItem : time_items
        TimeItem --> "*" TimeItem : time_items
        click TimeItem href "./TimeItem.html"
      TimeItem : time_plan
        TimeItem --> "0..1" TimePlan : time_plan
        click TimePlan href "./TimePlan.html"
      TimeItem : time_plans
        TimeItem --> "*" TimePlan : time_plans
        click TimePlan href "./TimePlan.html"
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * [AbstractTimeRecord](AbstractTimeRecord.md)
            * **TimeItem**
                * [Milestone](Milestone.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:TimeItem](https://schema.pragmaticbim.ch/TimeItem) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [time_plan](time_plan.md) | 0..1 <br/> [TimePlan](TimePlan.md) | Parent time plan this item or dependency belongs to. | direct |
| [planned_start_at](planned_start_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Planned start timestamp for the time item. | direct |
| [planned_finish_at](planned_finish_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Planned finish timestamp for the time item. | direct |
| [actual_start_at](actual_start_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Actual start timestamp for the time item where known. | direct |
| [actual_finish_at](actual_finish_at.md) | 0..1 <br/> [Datetime](Datetime.md) | Actual finish timestamp for the time item where known. | direct |
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
| [VirtualEntity](VirtualEntity.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [SpatialContext](SpatialContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [ProjectContext](ProjectContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [PerimeterContext](PerimeterContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [LegalSiteContext](LegalSiteContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [BuildingContext](BuildingContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [CivilStructureContext](CivilStructureContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [LevelContext](LevelContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [ZoneContext](ZoneContext.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [Space](Space.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [System](System.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [AbstractTimeRecord](AbstractTimeRecord.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [TimeItem](TimeItem.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [Milestone](Milestone.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [TimePlan](TimePlan.md) | [component_time_items](component_time_items.md) | range | [TimeItem](TimeItem.md) |
| [TimePlan](TimePlan.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [TimeDependency](TimeDependency.md) | [predecessor_item](predecessor_item.md) | range | [TimeItem](TimeItem.md) |
| [TimeDependency](TimeDependency.md) | [successor_item](successor_item.md) | range | [TimeItem](TimeItem.md) |
| [TimeDependency](TimeDependency.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [CostItem](CostItem.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [CostAssembly](CostAssembly.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |
| [Material](Material.md) | [time_items](time_items.md) | range | [TimeItem](TimeItem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:TimeItem |
| native | pbs:TimeItem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TimeItem
description: Planned work item with baseline and actual dates, optionally linked to
  model entities and a time plan.
from_schema: https://schema.pragmaticbim.ch
is_a: AbstractTimeRecord
slots:
- time_plan
- planned_start_at
- planned_finish_at
- actual_start_at
- actual_finish_at
class_uri: pbs:TimeItem

```
</details>

### Induced

<details>
```yaml
name: TimeItem
description: Planned work item with baseline and actual dates, optionally linked to
  model entities and a time plan.
from_schema: https://schema.pragmaticbim.ch
is_a: AbstractTimeRecord
attributes:
  time_plan:
    name: time_plan
    description: Parent time plan this item or dependency belongs to.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - TimeItem
    - TimeDependency
    range: TimePlan
    inlined: false
  planned_start_at:
    name: planned_start_at
    description: Planned start timestamp for the time item.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - TimeItem
    range: datetime
  planned_finish_at:
    name: planned_finish_at
    description: Planned finish timestamp for the time item.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - TimeItem
    range: datetime
  actual_start_at:
    name: actual_start_at
    description: Actual start timestamp for the time item where known.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - TimeItem
    range: datetime
  actual_finish_at:
    name: actual_finish_at
    description: Actual finish timestamp for the time item where known.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - TimeItem
    range: datetime
  applies_to_entities:
    name: applies_to_entities
    description: Model entities this record applies to (requirements, cost items,
      schedule items, etc.).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
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
    owner: TimeItem
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: TimeItem
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:TimeItem

```
</details></div>
---
search:
  boost: 10.0
---

# Class: ConnectionVirtual 


_Logical or topological connection between spaces and/or physical elements._



<div data-search-exclude markdown="1">



URI: [pbs:ConnectionVirtual](https://schema.pragmaticbim.ch/ConnectionVirtual)





```mermaid
 classDiagram
    class ConnectionVirtual
    click ConnectionVirtual href "./ConnectionVirtual.html"
      VirtualEntity <|-- ConnectionVirtual
        click VirtualEntity href "./VirtualEntity.html"
      ConnectionVirtual : classifications
        ConnectionVirtual --> "*" Classification : classifications
        click Classification href "./Classification.html"
      ConnectionVirtual : connection_virtual_requirement_drivers
        ConnectionVirtual --> "*" ConnectionRequirementDriver : connection_virtual_requirement_drivers
        click ConnectionRequirementDriver href "./ConnectionRequirementDriver.html"
      ConnectionVirtual : connection_virtual_type
        ConnectionVirtual --> "1" ConnectionVirtualType : connection_virtual_type
        click ConnectionVirtualType href "./ConnectionVirtualType.html"
      ConnectionVirtual : connects_physical_elements
        ConnectionVirtual --> "*" PhysicalElement : connects_physical_elements
        click PhysicalElement href "./PhysicalElement.html"
      ConnectionVirtual : connects_spaces
        ConnectionVirtual --> "*" Space : connects_spaces
        click Space href "./Space.html"
      ConnectionVirtual : cost_records
        ConnectionVirtual --> "*" CostRecord : cost_records
        click CostRecord href "./CostRecord.html"
      ConnectionVirtual : created_at
      ConnectionVirtual : decisions
        ConnectionVirtual --> "*" Decision : decisions
        click Decision href "./Decision.html"
      ConnectionVirtual : description
      ConnectionVirtual : documents
        ConnectionVirtual --> "*" Document : documents
        click Document href "./Document.html"
      ConnectionVirtual : geometry_representations
        ConnectionVirtual --> "*" GeometryRepresentation : geometry_representations
        click GeometryRepresentation href "./GeometryRepresentation.html"
      ConnectionVirtual : id
      ConnectionVirtual : ifc_global_id
      ConnectionVirtual : localized_descriptions
        ConnectionVirtual --> "*" LocalizedText : localized_descriptions
        click LocalizedText href "./LocalizedText.html"
      ConnectionVirtual : localized_names
        ConnectionVirtual --> "*" LocalizedText : localized_names
        click LocalizedText href "./LocalizedText.html"
      ConnectionVirtual : materials
        ConnectionVirtual --> "*" Material : materials
        click Material href "./Material.html"
      ConnectionVirtual : meaning_uri
      ConnectionVirtual : messages
        ConnectionVirtual --> "*" Message : messages
        click Message href "./Message.html"
      ConnectionVirtual : metadata
        ConnectionVirtual --> "*" MetadataEntry : metadata
        click MetadataEntry href "./MetadataEntry.html"
      ConnectionVirtual : modified_at
      ConnectionVirtual : name
      ConnectionVirtual : performance_properties
        ConnectionVirtual --> "*" PerformanceProperty : performance_properties
        click PerformanceProperty href "./PerformanceProperty.html"
      ConnectionVirtual : quantity_values
        ConnectionVirtual --> "*" QuantityValue : quantity_values
        click QuantityValue href "./QuantityValue.html"
      ConnectionVirtual : revision
      ConnectionVirtual : status
        ConnectionVirtual --> "0..1" StatusType : status
        click StatusType href "./StatusType.html"
      ConnectionVirtual : tasks
        ConnectionVirtual --> "*" Task : tasks
        click Task href "./Task.html"
      ConnectionVirtual : time_records
        ConnectionVirtual --> "*" TimeRecord : time_records
        click TimeRecord href "./TimeRecord.html"
```





## Inheritance
* [Entity](Entity.md)
    * [VirtualEntity](VirtualEntity.md)
        * **ConnectionVirtual**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:ConnectionVirtual](https://schema.pragmaticbim.ch/ConnectionVirtual) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [connection_virtual_type](connection_virtual_type.md) | 1 <br/> [ConnectionVirtualType](ConnectionVirtualType.md) | Classification of virtual connection semantics (for example structural_joint, adjacency, access). | direct |
| [connects_physical_elements](connects_physical_elements.md) | * <br/> [PhysicalElement](PhysicalElement.md) | Physical elements connected by this virtual connection (for example wall-wall, wall-slab). | direct |
| [connects_spaces](connects_spaces.md) | * <br/> [Space](Space.md) | Spaces connected by this virtual connection. | direct |
| [connection_virtual_requirement_drivers](connection_virtual_requirement_drivers.md) | * <br/> [ConnectionRequirementDriver](ConnectionRequirementDriver.md) | Main requirement drivers for this virtual connection. | direct |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:ConnectionVirtual |
| native | pbs:ConnectionVirtual |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConnectionVirtual
description: Logical or topological connection between spaces and/or physical elements.
from_schema: https://schema.pragmaticbim.ch
is_a: VirtualEntity
slots:
- connection_virtual_type
- connects_physical_elements
- connects_spaces
- connection_virtual_requirement_drivers
class_uri: pbs:ConnectionVirtual

```
</details>

### Induced

<details>
```yaml
name: ConnectionVirtual
description: Logical or topological connection between spaces and/or physical elements.
from_schema: https://schema.pragmaticbim.ch
is_a: VirtualEntity
attributes:
  connection_virtual_type:
    name: connection_virtual_type
    description: Classification of virtual connection semantics (for example structural_joint,
      adjacency, access).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - ConnectionVirtual
    range: ConnectionVirtualType
    required: true
  connects_physical_elements:
    name: connects_physical_elements
    description: Physical elements connected by this virtual connection (for example
      wall-wall, wall-slab).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - ConnectionVirtual
    range: PhysicalElement
    multivalued: true
  connects_spaces:
    name: connects_spaces
    description: Spaces connected by this virtual connection.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - ConnectionVirtual
    range: Space
    multivalued: true
  connection_virtual_requirement_drivers:
    name: connection_virtual_requirement_drivers
    description: Main requirement drivers for this virtual connection.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - ConnectionVirtual
    range: ConnectionRequirementDriver
    multivalued: true
  cost_records:
    name: cost_records
    description: Cost records associated with this entity.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
    domain_of:
    - Entity
    range: uriorcurie
  localized_descriptions:
    name: localized_descriptions
    description: Localized variants of description.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
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
    owner: ConnectionVirtual
    domain_of:
    - Entity
    range: datetime
  modified_at:
    name: modified_at
    description: Last modification timestamp for this entity record.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - Entity
    range: datetime
  revision:
    name: revision
    description: Integer revision counter for change tracking.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - Entity
    range: integer
    minimum_value: 0
  status:
    name: status
    description: Lifecycle or QA status.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: ConnectionVirtual
    domain_of:
    - Entity
    - Requirement
    range: StatusType
class_uri: pbs:ConnectionVirtual

```
</details></div>
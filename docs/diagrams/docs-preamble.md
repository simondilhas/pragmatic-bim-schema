<!-- schema-diagrams-preamble -->

## Schema diagrams

Generated from `schema/*.yaml`. See the [schema documentation](https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html) for interactive class pages.

### Module map

```mermaid
flowchart TB
  Root["Pragmatic BIM Data Contract"]
  Root --> core["Core"]
  Root --> performance_enums["Performance Enums"]
  Root --> requirements_enums["Requirements Enums"]
  Root --> performance["Entity Performance Properties"]
  Root --> requirements["Requirements"]
  Root --> elements_physical["Elements Physical"]
  Root --> elements_virtual["Elements Virtual"]
  Root --> enums["Enums"]
  Root --> changes["Changes"]
```

### Three pillars (overview)

```mermaid
flowchart TB
  Root["Pragmatic BIM Data Contract"]
  Root --> Entity["Entities"]
  Root --> Requirement["Requirements"]
  Root --> Change["Changes"]
```

### Entities (detail)

```mermaid
classDiagram
  direction TB
  Entity <|-- Agent
  Agent <|-- Company
  Agent <|-- Person
  Entity <|-- Message
  Entity <|-- PhysicalElement
  PhysicalElement <|-- Boundary
  PhysicalElement <|-- ConnectionPhysical
  PhysicalElement <|-- Equipment
  PhysicalElement <|-- Separator
  Separator <|-- SeparatorSlab
  Separator <|-- SeparatorWall
  Entity <|-- VirtualEntity
  VirtualEntity <|-- AbstractCostRecord
  AbstractCostRecord <|-- CostAssembly
  AbstractCostRecord <|-- CostItem
  VirtualEntity <|-- AbstractTimeRecord
  AbstractTimeRecord <|-- TimeItem
  TimeItem <|-- Milestone
  AbstractTimeRecord <|-- TimePlan
  VirtualEntity <|-- ConnectionVirtual
  VirtualEntity <|-- Material
  VirtualEntity <|-- Space
  VirtualEntity <|-- SpatialContext
  SpatialContext <|-- BuiltAssetContext
  BuiltAssetContext <|-- BuildingContext
  BuiltAssetContext <|-- CivilStructureContext
  SpatialContext <|-- LegalSiteContext
  SpatialContext <|-- LevelContext
  SpatialContext <|-- PerimeterContext
  SpatialContext <|-- ProjectContext
  SpatialContext <|-- ZoneContext
  VirtualEntity <|-- System
  VirtualEntity <|-- TimeDependency
  PerformanceProperty <|-- AcousticProperty
  PerformanceProperty <|-- FireProperty
  PerformanceProperty <|-- MaterialProperty
  PerformanceProperty <|-- SecurityProperty
  PerformanceProperty <|-- StructuralProperty
  PerformanceProperty <|-- ThermalProperty
  Entity *-- PerformanceProperty
```

### Requirements (detail)

```mermaid
classDiagram
  direction TB
  Requirement <|-- BriefRequirement
  Requirement <|-- PerformanceRequirement
  Requirement <|-- RegulatoryRequirement
  Requirement <|-- SpatialRequirement
```

### Changes (detail)

```mermaid
classDiagram
  direction TB
  Change <|-- AdditionChange
  Change <|-- DeletionChange
  Change <|-- GeometryChange
  Change <|-- MatchChange
  Change <|-- PropertyChange
  Change <|-- RequirementChange
  ChangeSet *-- Change
  PropertyChange *-- PropertyDelta
  RequirementChange *-- PropertyDelta
  Change *-- StateRef
  ChangeSet *-- StateRef
```


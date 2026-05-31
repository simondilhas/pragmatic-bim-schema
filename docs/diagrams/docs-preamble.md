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
  Root --> performance["Performance"]
  Root --> requirements["Requirements"]
  Root --> elements_physical["Elements Physical"]
  Root --> elements_virtual["Elements Virtual"]
  Root --> enums["Enums"]
  Root --> changes["Changes"]
```

### Entity hierarchy

```mermaid
classDiagram
  VirtualEntity <|-- AbstractCostRecord
  PerformanceProperty <|-- AcousticProperty
  Entity <|-- Agent
  PhysicalElement <|-- Boundary
  BuiltAssetContext <|-- BuildingContext
  SpatialContext <|-- BuiltAssetContext
  BuiltAssetContext <|-- CivilStructureContext
  Agent <|-- Company
  PhysicalElement <|-- ConnectionPhysical
  VirtualEntity <|-- ConnectionVirtual
  AbstractCostRecord <|-- CostAssembly
  AbstractCostRecord <|-- CostItem
  PhysicalElement <|-- Equipment
  PerformanceProperty <|-- FireProperty
  SpatialContext <|-- LegalSiteContext
  SpatialContext <|-- LevelContext
  VirtualEntity <|-- Material
  PerformanceProperty <|-- MaterialProperty
  Entity <|-- Message
  ScheduleItem <|-- Milestone
  SpatialContext <|-- PerimeterContext
  Agent <|-- Person
  Entity <|-- PhysicalElement
  SpatialContext <|-- ProjectContext
  Entity <|-- ScheduleDependency
  Entity <|-- ScheduleItem
  Entity <|-- ScheduleTemplate
  PerformanceProperty <|-- SecurityProperty
  PhysicalElement <|-- Separator
  Separator <|-- SeparatorSlab
  Separator <|-- SeparatorWall
  VirtualEntity <|-- Space
  VirtualEntity <|-- SpatialContext
  PerformanceProperty <|-- StructuralProperty
  VirtualEntity <|-- System
  PerformanceProperty <|-- ThermalProperty
  Entity <|-- VirtualEntity
  SpatialContext <|-- ZoneContext
```


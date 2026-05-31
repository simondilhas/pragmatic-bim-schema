<!-- schema-diagrams-preamble -->

## Schema diagrams

Generated from `schema/*.yaml`. Click a pillar in the overview or use the buttons below to explore each branch.

<div id="pillars-acc" class="pillars-acc">

<div class="pillars-overview">
<pre class="mermaid">
flowchart TB
  Root["Pragmatic BIM Data Contract"]
  Root --> Entity["Entities"]
  Root --> Requirement["Requirements"]
  Root --> Change["Changes"]
</pre>
</div>

<div class="pillar-controls">
  <button type="button" class="pillar-btn" data-pillar="entity">Entities</button>
  <button type="button" class="pillar-btn" data-pillar="requirement">Requirements</button>
  <button type="button" class="pillar-btn" data-pillar="change">Changes</button>
</div>

<div class="pillar-panels">
  <div id="pillar-entity" class="pillar-panel" hidden>
<pre class="mermaid">
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
  VirtualEntity <|-- ConnectionVirtual
  VirtualEntity <|-- CostRecord
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
  VirtualEntity <|-- TimeRecord
  PerformanceProperty <|-- AcousticProperty
  PerformanceProperty <|-- FireProperty
  PerformanceProperty <|-- MaterialProperty
  PerformanceProperty <|-- SecurityProperty
  PerformanceProperty <|-- StructuralProperty
  PerformanceProperty <|-- ThermalProperty
  Entity *-- PerformanceProperty
</pre>
  </div>
  <div id="pillar-requirement" class="pillar-panel" hidden>
<pre class="mermaid">
classDiagram
  direction TB
  Requirement <|-- BriefRequirement
  Requirement <|-- PerformanceRequirement
  Requirement <|-- RegulatoryRequirement
  Requirement <|-- SpatialRequirement
</pre>
  </div>
  <div id="pillar-change" class="pillar-panel" hidden>
<pre class="mermaid">
classDiagram
  direction TB
  Change <|-- AdditionChange
  Change <|-- DeletionChange
  Change <|-- GeometryChange
  Change <|-- MatchChange
  Change <|-- PropertyChange
  Change <|-- RequirementChange
  ChangeSet *-- Change
</pre>
  </div>
</div>

</div>

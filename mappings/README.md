# IFC Mapping Specification

Declarative mapping from IFC entity classes to the [Pragmatic BIM Data Contract](https://schema.pragmaticbim.ch/) schema and the ingestion adapter database projection.

**Files**

| File | Role |
|------|------|
| [`ifc_mapping.yaml`](ifc_mapping.yaml) | Entrypoint: version, schema URI, `imports` list |
| [`ifc_mapping.merged.yaml`](ifc_mapping.merged.yaml) | **Generated** single-file artifact for adapters (regenerate after edits) |
| [`_conventions.yaml`](_conventions.yaml) | Global rules, metadata capture, field anchors |
| [`_pset_fallbacks.yaml`](_pset_fallbacks.yaml) | PropertySet lookup lists (default + Revit / ArchiCAD / Vectorworks) |
| [`_relationships.yaml`](_relationships.yaml) | IFC rel class → `relation_type` |
| [`_fragments.yaml`](_fragments.yaml) | Shared field, geometry, and attribute fragments |
| [`_templates.yaml`](_templates.yaml) | Shared entity templates (`inherits`) |
| [`entities/architectural.yaml`](entities/architectural.yaml) | Walls, slabs, doors, spatial context, structure |
| [`entities/hvac.yaml`](entities/hvac.yaml) | Ducts, pipes, equipment, systems |
| [`../scripts/merge_ifc_mapping.py`](../scripts/merge_ifc_mapping.py) | Merge split sources → `ifc_mapping.merged.yaml` |

Split sources are the **source of truth**. Edit those, then regenerate the merged file.

This directory contains **no adapter logic** — only declarative YAML plus the merge helper script.

---

## File layout and merge workflow

YAML anchors (`&name` / `*name`) do not work across files. Split sources are concatenated in `imports` order by the merge script so anchors resolve correctly.

```text
ifc_mapping.yaml          ← entrypoint (imports list)
_conventions.yaml         ← conventions + metadata anchors
_pset_fallbacks.yaml      ← tool-specific pset lists
_relationships.yaml
_fragments.yaml           ← geometry / field fragments (uses pset anchors)
entities/architectural.yaml
entities/hvac.yaml        ← entity blocks (indented under entities:)
_templates.yaml
        │
        ▼  python scripts/merge_ifc_mapping.py
ifc_mapping.merged.yaml   ← single file for adapters
```

**After editing any split file:**

```bash
python scripts/merge_ifc_mapping.py
```

**CI check (merged file up to date):**

```bash
python scripts/merge_ifc_mapping.py --check
```

Adapters can either load `ifc_mapping.merged.yaml` directly, or implement the same `imports` merge at runtime.

### Where to edit what

| Change | File |
|--------|------|
| New Revit / ArchiCAD / Vectorworks pset | `_pset_fallbacks.yaml` |
| New IFC class (architectural) | `entities/architectural.yaml` |
| New IFC class (HVAC) | `entities/hvac.yaml` |
| New relationship rule | `_relationships.yaml` |
| Metadata / GlobalId conventions | `_conventions.yaml` |
| Shared field or geometry pattern | `_fragments.yaml` or `_templates.yaml` |

---

## Purpose

IFC exports vary by authoring tool and project. This mapping:

1. Normalizes IFC instances to PBS entity types (`canonical_type`) and module categories (`content_kind`).
2. Projects schema slots onto adapter columns (`name`, `code_or_number`, `storey`, `attributes`).
3. Declares IFC relationship → `content_relations.relation_type` mappings aligned with PBS schema slot names.
4. Assigns geometry roles for the `content_geometries` table.

Schema slots are defined in [`schema/`](../schema/). This mapping must not introduce fields absent from those YAML modules.

---

## Database projection

The adapter writes three tables:

### `content`

| Column | Source |
|--------|--------|
| `content_kind` | `physical`, `virtual`, or `context` (see below) |
| `canonical_type` | PBS LinkML class name, optionally with variant suffix (e.g. `SeparatorSlab.floor`) |
| `canonical_type_version` | Pinned schema release (currently `v0.0.7` in `ifc_mapping.yaml`) |
| `name` | `Entity.name` |
| `code_or_number` | Primary identifier from classifications or PropertySet fallbacks |
| `storey` | `parent_level` resolution via spatial containment (GlobalId of `IfcBuildingStorey`) |
| `source_id` | IFC `GlobalId` — **primary IFC ↔ contract link** (see below) |
| `source_system` | Export origin (`revit`, `archicad`, `vectorworks`, or default `ifc`) |
| `attributes` | JSONB of PBS schema slots for the entity class, including `ifc_global_id` and `metadata[]` |

### IFC ↔ contract identity (`GlobalId`)

IFC `GlobalId` is the stable crosswalk between the source model and PBS contract records:

| Location | Role |
|----------|------|
| `content.source_id` | Primary lookup key on ingest and re-import |
| `attributes.ifc_global_id` | PBS `Entity.ifc_global_id` slot (same value) |
| `content_relations.source_content_id` / `target_content_id` | Relationship endpoints |

Re-imports, updates, and change detection match on `GlobalId`. The adapter should not generate a new contract `id` when `GlobalId` already exists for the same model scope.

Defined in `ifc_mapping.yaml` under `conventions.ifc_contract_link`.

### `content_relations`

| Column | Source |
|--------|--------|
| `source_content_id` | Source element GlobalId |
| `target_content_id` | Target element GlobalId |
| `relation_type` | PBS relationship slot name (e.g. `parent_level`, `separates_spaces`) |

### `content_geometries`

| Column | Source |
|--------|--------|
| `geometry_role` | `body_3d`, `footprint_2d`, `axis`, or `point` ([`GeometryRepresentationType`](../schema/entity_schema_enums.yaml)) |
| `geometry_space` | IFC representation context or storey GlobalId |
| `geom` | Geometry payload (adapter-specific) |

---

## `content_kind` and `canonical_type`

| `content_kind` | PBS module | Examples |
|----------------|------------|----------|
| `physical` | [`entity_physical_schema.yaml`](../schema/entity_physical_schema.yaml) | `SeparatorWall`, `ConnectionPhysical`, `Equipment`, `PhysicalElement` |
| `virtual` | [`entity_virtual_schema.yaml`](../schema/entity_virtual_schema.yaml) | `Space`, `System`, `ConnectionVirtual`, `TimeRecord`, `CostRecord`, `Material` |
| `context` | Spatial context subclasses | `BuildingContext`, `LevelContext`, `ZoneContext`, `PerimeterContext` |
| `requirement` | [`requirements_schema.yaml`](../schema/requirements_schema.yaml) | `PerformanceRequirement`, `SpatialRequirement`, `RegulatoryRequirement`, `BriefRequirement` |
| `change` | [`changes_schema.yaml`](../schema/changes_schema.yaml) | `PropertyChange`, `GeometryChange`, `MatchChange`, `AdditionChange`, `DeletionChange` |

`requirement` and `change` rows are **not** produced from IFC entity mapping blocks today. Adapters or validation pipelines create them directly. Use the concrete requirement or change class (for example `PerformanceRequirement`, `PropertyChange`) together with `change_type` where applicable, alongside `canonical_type`.

**Variant suffixes** disambiguate IFC `PredefinedType` or transport role without inventing new PBS classes:

- `SeparatorSlab.floor`, `.roof`, `.baseslab`
- `ConnectionPhysical.duct`, `.pipe`, `.network_other`
- `Boundary.ceiling`, `.flooring`, `.cladding`

---

## YAML file structure

The entrypoint [`ifc_mapping.yaml`](ifc_mapping.yaml) declares version metadata and an `imports` list. Split modules compose the full mapping (see **File layout and merge workflow** above). Adapters typically load [`ifc_mapping.merged.yaml`](ifc_mapping.merged.yaml).

Merged structure:

```yaml
mapping_version: "1.2.0"
schema_uri: https://schema.pragmaticbim.ch/
canonical_type_version: "v0.0.7"

conventions: ...
pset_fallbacks: ...
relationships: ...
fragments: ...
entities: ...
templates: ...
```

### Entity block

Each `entities.Ifc*` entry defines:

| Key | Description |
|-----|-------------|
| `content_kind` | Module category for the DB |
| `canonical_type` | PBS class (fixed or via `predefined_type_map`) |
| `inherits` | Merge fields from another entity or `templates.*` entry |
| `fields` | Top-level DB column lookups |
| `attributes` | PBS schema slots stored in JSONB |
| `geometry` | Primary and secondary `geometry_role` values |
| `relations` | IFC relationship classes that apply to this entity |

---

## Field source types

| Source type | Adapter behavior |
|-------------|------------------|
| `ifc_attribute` | Read a direct IFC attribute |
| `ifc_attribute_fallback` | Try attributes in order; first non-empty wins |
| `ifc_pset_fallback` | Try PropertySet/property pairs in order; first match wins |
| `ifc_attribute_all` | All IFC entity attributes on the instance, minus excluded/promoted ones |
| `ifc_pset_all` | All PropertySet properties on the instance, minus those used elsewhere |
| `metadata_merge` | Combine multiple metadata capture rules into one `metadata[]` array |
| `ifc_classification` | Map `IfcClassificationReference` via `IfcRelAssociatesClassification` |
| `ifc_relation` | Resolve value through an IFC relationship |
| `ifc_attribute_heuristic` | Map attribute value through keyword rules with a default |
| `ifc_relation_heuristic` | Infer value from related entities (e.g. system discipline) |
| `constant` | Fixed PBS enum or string value |
| `predefined_type_map` | Branch on IFC `PredefinedType` |

---

## Fallback convention

Property lookups use **ordered fallback lists**. The adapter applies `conventions.fallback_policy: first_match_wins`.

### Resolution order for `code_or_number`

1. If `source_system_overrides[source_system]` exists, try those PropertySet pairs first.
2. Then try the shared `fallbacks` list (tool-agnostic IFC standard psets).
3. If still empty, use the first `classifications[].classification_code` from `IfcRelAssociatesClassification`.

### Source system overrides

| `source_system` | Typical extra psets |
|-----------------|---------------------|
| `revit` | `Pset_Revit_IdentityData.Mark`, `Pset_Revit_TypeIdentity.Type Mark` |
| `archicad` | `ARCHICAD_General.ID`, `ARCHICAD_General.Element ID` |
| `vectorworks` | `Vectorworks_General.Tag`, `Vectorworks_Data.RecordName` |

Shared defaults (`Pset_BuildingElementCommon.Reference`, etc.) are always appended after tool-specific entries in the entity `fallbacks` list.

**When extending:** add new entries at the **top** of the relevant override list for a source system. Do not reorder existing entries — downstream projects may depend on current precedence.

---

## Classifications

All mapped entities include a `classifications` field mapping. The adapter populates the PBS `classifications[]` slot (inlined `Classification` objects) from `IfcRelAssociatesClassification`:

| Classification slot | IFC source |
|---------------------|------------|
| `classification_scheme` | `ReferencedSource.Name`, fallback `"ifc"` |
| `classification_code` | `Identification` or `ItemReference` |
| `classification_label` | `Name` |
| `classification_uri` | `Location` |
| `classification_source` | `ReferencedSource.SourceRoles` |

This is especially important for entities with weak PBS typing (`IfcBeam`, `IfcColumn`, `IfcStair`, `IfcRamp`) where `classification_code` may also serve as `code_or_number`.

---

## Metadata capture (IFC attributes and PropertySets)

All mapped entities populate `attributes.metadata[]` (PBS `MetadataEntry`). Two capture rules are merged (`metadata_merge`):

### 1. IFC entity attributes

Every **IFC entity attribute** on the instance is stored unless already promoted elsewhere:

| Excluded (promoted) | Destination |
|---------------------|-------------|
| `GlobalId` | `source_id`, `attributes.ifc_global_id` |
| `Name`, `LongName`, `ObjectType` | `content.name` |
| `Description` | `attributes.description` |
| Attributes mapped to typed PBS slots | e.g. `PredefinedType` → `separator_slab_type` |

**Key format:** `{IfcClass}.{AttributeName}` — e.g. `IfcWall.OverallHeight`, `IfcDoor.OverallHeight`.

### 2. PropertySets

Every **PropertySet property** not used for `code_or_number` or typed attribute slots:

**Key format:** `{Pset}.{Property}` — e.g. `Pset_WallCommon.FireRating`.

### Value serialization

`metadata_value` is stored as text (`MetadataEntry.metadata_value`). The adapter serializes IFC values (numbers, booleans, enums, object references) to strings. Object references may use GlobalId where resolvable.

Example `attributes` JSONB fragment:

```json
{
  "ifc_global_id": "3l$8vj$nL1Pu4$G9QjXjC",
  "separator_wall_type": "unit_boundary",
  "metadata": [
    { "metadata_key": "IfcWall.OverallHeight", "metadata_value": "3.0" },
    { "metadata_key": "Pset_WallCommon.FireRating", "metadata_value": "EI60" }
  ]
}
```

---

## Relationship mappings

Global rules live under `relationships` in `ifc_mapping.yaml`. Each entity lists which IFC rel classes apply.

| IFC relationship | `relation_type` | When |
|------------------|-----------------|------|
| `IfcRelContainedInSpatialStructure` | `parent_level` | RelatingStructure is `IfcBuildingStorey` |
| same | `parent_space` | RelatingStructure is `IfcSpace` |
| same | `parent_building` | RelatingStructure is `IfcBuilding` |
| `IfcRelAggregates` | `parent_*` | Spatial hierarchy (site → building → storey) |
| `IfcRelAssignsToGroup` | `group_members` | Assigned to `IfcZone` / `IfcGroup` |
| `IfcRelAssignsToSystem` | `parent_system` | Element → system |
| same | `contained_entities` | System → member elements |
| `IfcRelSpaceBoundary` | `separates_spaces` | Wall/slab → space |
| same | `bounded_by` | Covering → space |
| `IfcRelConnectsElements` | `connects_physical_elements` | Structural joints, host connections |
| `IfcRelConnectsPathElements` | `connects_physical_elements` | Duct/pipe run connectivity |
| `IfcRelFillsElement` | `connects_physical_elements` | Door/window ↔ opening |
| `IfcRelServicesBuildings` | `serves_spaces` / `serves_zones` | System service area |
| `IfcRelAssociatesClassification` | `classifications` | Populates classifications slot |

---

## Geometry roles

Uses [`GeometryRepresentationType`](../schema/entity_schema_enums.yaml) values:

| Entity group | Primary | Secondary |
|--------------|---------|-----------|
| Walls, slabs, roofs, curtain walls, stairs, ramps, equipment, doors, windows, fittings | `body_3d` | `footprint_2d` |
| Duct/pipe segments | `axis` | `body_3d` |
| Spaces | `footprint_2d` | `body_3d` |
| Spatial contexts (site, building, storey, zone) | `footprint_2d` | `point` |
| Beams/columns (`ConnectionVirtual`) | `axis` | — |

---

## Worked examples

### IfcWall → SeparatorWall

```yaml
# entities.IfcWall (abbreviated)
content_kind: physical
canonical_type: SeparatorWall
fields:
  name: Name → LongName → ObjectType
  code_or_number: Pset_WallCommon.Reference → … → Revit Mark
  storey: IfcRelContainedInSpatialStructure → walk up to IfcBuildingStorey
attributes:
  separator_wall_type: unit_boundary
  ifc_global_id: GlobalId
geometry:
  primary: body_3d
  secondary: footprint_2d
metadata_examples:
  - IfcWall.OverallHeight
  - Pset_WallCommon.FireRating
relations:
  - IfcRelContainedInSpatialStructure
  - IfcRelSpaceBoundary
```

### IfcDuctSegment → ConnectionPhysical

```yaml
content_kind: physical
canonical_type: ConnectionPhysical.duct
attributes:
  connection_physical_type: duct
  transport_medium: air
geometry:
  primary: axis        # centerline
  secondary: body_3d
relations:
  - IfcRelConnectsPathElements
  - IfcRelAssignsToSystem
```

### IfcSlab PredefinedType split

Per **IfcSlabTypeEnum** (IFC 4.3). `CEILING` is **not** a slab type — ceilings are `IfcCovering` with `PredefinedType=CEILING`.

| IFC `PredefinedType` | `canonical_type` | `attributes.separator_slab_type` |
|----------------------|------------------|----------------------------------|
| `FLOOR`, `LANDING`, `PAVING`, … | `SeparatorSlab.floor` | `floor` |
| `ROOF` | `SeparatorSlab.roof` | `roof` |
| `BASESLAB`, `TRACKSLAB` | `SeparatorSlab.baseslab` | `baseslab` |
| `USERDEFINED`, `NOTDEFINED` | `SeparatorSlab.floor` (default) | `floor` |

### IfcCovering PredefinedType split

Per **IfcCoveringTypeEnum**. Maps to PBS `Boundary` (`schema` exact mapping: `ifcowl:IfcCovering`).

| IFC `PredefinedType` | `canonical_type` | `attributes.boundary_type` |
|----------------------|------------------|----------------------------|
| `CEILING` | `Boundary.ceiling` | `ceiling` |
| `FLOORING`, `SKIRTINGBOARD`, `TOPPING` | `Boundary.flooring` | `flooring` |
| `CLADDING`, `ROOFING`, `INSULATION`, … | `Boundary.cladding` | `cladding` |

---

## IFC schema cross-check notes

Mappings are validated against IFC 4.3 entity and enumeration definitions ([buildingSMART IFC 4.3 docs](https://ifc43-docs.standards.buildingsmart.org/)). Key corrections:

| Topic | IFC fact | Mapping rule |
|-------|----------|--------------|
| Ceiling | `IfcCoveringTypeEnum.CEILING` on **IfcCovering**; slabs are structural only | `IfcCovering` → `Boundary`; not on `IfcSlab` |
| IfcRoof | Assembly container aggregating slabs/beams | `PhysicalElement`, not `SeparatorSlab.roof` |
| IfcSlab types | `FLOOR`, `ROOF`, `BASESLAB`, `LANDING`, + civil types — no `CEILING` | Full enum in `entities/architectural.yaml` |
| Pipe segment type | `IfcPipeSegmentTypeEnum`: `RIGIDSEGMENT`, `FLEXIBLESEGMENT`, … — not `GAS`/`STEAM` | `transport_medium` inferred from `IfcDistributionSystem` |
| System PredefinedType | `IfcDistributionSystemEnum`: `DOMESTICHOTWATER`, `DOMESTICCOLDWATER`, … | Fixed invalid `_` spellings; no `SANITARY` — use `SEWAGE`/`WASTEWATER` |

---

## Known schema gaps

Documented limitations where IFC semantics exceed current PBS schema coverage:

| Gap | Mapping approach |
|-----|------------------|
| `BoundaryType` has only `flooring`, `ceiling`, `cladding` | Other `IfcCoveringTypeEnum` values (e.g. `ROOFING`, `INSULATION`) map to nearest boundary type |
| No fitting enum on `ConnectionPhysicalType` | `IfcDuctFitting`, `IfcPipeFitting` → `network_other` |
| No structural member class | `IfcBeam`, `IfcColumn` → `ConnectionVirtual` with `connection_virtual_type: structural_joint` |
| No stair/ramp class | `IfcStair`, `IfcRamp` → abstract `PhysicalElement`; enrich via `classifications[]` |
| `IfcCurtainWall` | Mapped to `SeparatorWall` (closest wall-based separator) |
| `IfcRoof` | Mapped to `PhysicalElement` (assembly container; roof faces are `IfcSlab`/`IfcCovering` parts) |

These are intentional pragmatic mappings pending schema extension.

---

## Extending for a new source system

1. Add a key under each relevant `source_system_overrides` block in `pset_fallbacks` (or per-entity `fields.code_or_number`).
2. Place tool-specific psets **before** shared IFC standard psets.
3. Set `source_system` on ingest to match the override key (lowercase, e.g. `solibri` if adding QA tool exports).
4. Document the new overrides in this README.

Example:

```yaml
source_system_overrides:
  mytool:
    - pset: MyTool_Identity
      property: ElementCode
```

---

## Adding a new IFC class

1. Identify the nearest PBS class in [`entity_physical_schema.yaml`](../schema/entity_physical_schema.yaml) or [`entity_virtual_schema.yaml`](../schema/entity_virtual_schema.yaml).
2. Add an `entities.IfcNewClass` block with `content_kind`, `canonical_type`, required type slots, and geometry.
3. Copy `fields` and `attributes` patterns from a similar entity; only use slot names that exist on the target PBS class (plus `Entity` base slots).
4. List applicable IFC relationships under `relations`.
5. Add entity-specific pset fallbacks to `pset_fallbacks` if standard lists are insufficient.
6. If the entity shares a template with others, add a `templates.*` entry and reference it with `inherits`.

---

## `inherits` and templates

Some entities declare `inherits: IfcHvacEquipmentBase` or `inherits: IfcWall`. The adapter merges the referenced `templates.*` or `entities.*` block before applying entity-specific overrides. Keys on the entity take precedence.

HVAC equipment sharing `IfcHvacEquipmentBase`: `IfcPump`, `IfcFan`, `IfcCompressor`, `IfcBoiler`, `IfcChiller`, `IfcCoolingTower`, `IfcHeatExchanger`.

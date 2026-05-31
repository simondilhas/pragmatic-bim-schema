from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'pbs',
     'default_range': 'string',
     'description': 'To provide a simple, implementation-ready BIM data model for '
                    'integration, querying, costing, and analysis workflows, this '
                    'schema defines a pragmatic, graph-first LinkML structure that '
                    'is IFC-aware and extensible across classification schemes.\n',
     'id': 'https://schema.pragmaticbim.ch',
     'imports': ['linkml:types',
                 'shared_enums_schema',
                 'entity_core_schema',
                 'entity_enums_schema',
                 'entity_performance_enums_schema',
                 'entity_performance_schema',
                 'entity_physical_schema',
                 'entity_virtual_schema',
                 'requirements_enums_schema',
                 'requirements_schema',
                 'changes_enums_schema',
                 'changes_schema'],
     'license': 'MIT',
     'name': 'pragmatic_bim_data_contract',
     'prefixes': {'bot': {'prefix_prefix': 'bot',
                          'prefix_reference': 'https://w3id.org/bot#'},
                  'ifc': {'prefix_prefix': 'ifc',
                          'prefix_reference': 'https://standards.buildingsmart.org/IFC/DEV/IFC4_3/FINAL/HTML/'},
                  'ifcowl': {'prefix_prefix': 'ifcowl',
                             'prefix_reference': 'https://w3id.org/ifc/IFC4_ADD2#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'pbs': {'prefix_prefix': 'pbs',
                          'prefix_reference': 'https://schema.pragmaticbim.ch/'}},
     'see_also': ['https://schema.pragmaticbim.ch',
                  'https://schema.pragmaticbim.ch/schema/pragmatic-bim.docs.html'],
     'source_file': 'schema/00_pragmatic_bim_data_contract.yaml',
     'title': 'Pragmatic BIM Data Contract'} )

class ContentKind(str, Enum):
    """
    Top-level content category for adapter projection and schema routing.
    """
    physical = "physical"
    """
    Tangible BIM element from the physical elements module.
    """
    virtual = "virtual"
    """
    Non-physical conceptual entity (space, system, time/cost record, etc.).
    """
    context = "context"
    """
    Spatial context node (project, site, building, level, zone).
    """
    requirement = "requirement"
    """
    Prescriptive requirement record.
    """
    change = "change"
    """
    Revision diff or audit record.
    """


class QuantityType(str, Enum):
    area_net_horizontal = "area_net_horizontal"
    """
    Net horizontal area, typically usable floor area excluding non-net parts.
    """
    area_gross_horizontal = "area_gross_horizontal"
    """
    Gross horizontal area, typically measured to outer boundaries.
    """
    area_net_vertical = "area_net_vertical"
    """
    Net vertical area, typically wall or facade area excluding deductions.
    """
    area_gross_vertical = "area_gross_vertical"
    """
    Gross vertical area, typically full wall or facade area including non-net portions.
    """
    volume_net = "volume_net"
    """
    Net enclosed volume after subtracting non-counted voids or deductions.
    """
    volume_gross = "volume_gross"
    """
    Gross enclosed volume measured to external or gross boundaries.
    """
    length = "length"
    """
    Linear extent of an element or feature.
    """
    width = "width"
    """
    Width dimension of an element, opening, or space proxy.
    """
    height = "height"
    """
    Height dimension of an element, opening, or space proxy.
    """
    perimeter = "perimeter"
    """
    Boundary length around a 2D shape or footprint.
    """


class StatusType(str, Enum):
    """
    Lifecycle or QA gate status used for model progression and approvals.
    """
    draft = "draft"
    """
    Work-in-progress state before formal review.
    """
    submitted = "submitted"
    """
    Submitted state for review or approval.
    """
    reviewed = "reviewed"
    """
    Reviewed state pending final approval decision.
    """
    approved = "approved"
    """
    Approved state accepted for downstream use.
    """
    rejected = "rejected"
    """
    Rejected state not accepted for downstream use.
    """
    archived = "archived"
    """
    Archived state no longer in use.
    """


class BoundaryType(str, Enum):
    flooring = "flooring"
    ceiling = "ceiling"
    cladding = "cladding"


class ConnectionPhysicalType(str, Enum):
    """
    Classification of physical connector elements that connect spaces.
    """
    door = "door"
    """
    Human access connector via a door element.
    """
    window = "window"
    """
    Visual/daylight connector via a window element.
    """
    duct = "duct"
    """
    Air distribution connector segment.
    """
    pipe = "pipe"
    """
    Fluid/gas distribution connector segment.
    """
    cable = "cable"
    """
    Electrical/data cable connector segment.
    """
    conduit = "conduit"
    """
    Electrical/data conduit connector segment.
    """
    opening_other = "opening_other"
    """
    Other opening-style connector not covered by door/window.
    """
    network_other = "network_other"
    """
    Other network connector segment not covered by controlled values.
    """


class ConnectionVirtualType(str, Enum):
    """
    Classification of virtual connection semantics using schema-internal meanings because no stable 1:1 IFC mapping exists for these concepts.
    """
    structural_joint = "structural_joint"
    """
    Logical structural continuity or structural joint relation.
    """
    adjacency = "adjacency"
    """
    Topological adjacency relation without implying a physical opening.
    """
    access = "access"
    """
    Access relation indicating passability or navigational linkage.
    """
    other = "other"
    """
    Other virtual connection semantics not covered by the controlled values.
    """


class ContextType(str, Enum):
    project = "project"
    perimeter = "perimeter"
    legal_site = "legal_site"
    building = "building"
    civil_structure = "civil_structure"
    level = "level"
    zone = "zone"


class EquipmentType(str, Enum):
    hvac = "hvac"
    """
    HVAC endpoint/device such as terminal units or packaged devices.
    """
    electrical = "electrical"
    """
    Electrical endpoint/device such as appliances, outlets, or fixtures.
    """
    plumbing = "plumbing"
    """
    Plumbing endpoint/device such as sanitary terminals and fixtures.
    """
    fire_safety = "fire_safety"
    """
    Fire safety endpoint/device such as suppression terminals and alarms.
    """
    controls = "controls"
    """
    Monitoring/control device such as sensors, actuators, and controllers.
    """
    furniture = "furniture"
    """
    Furniture/device objects treated as endpoint assets.
    """
    other = "other"
    """
    Other endpoint/device element not covered by controlled values.
    """


class GeometryRepresentationType(str, Enum):
    """
    Classification of geometric representation dimension/style.
    """
    axis = "axis"
    """
    Linear axis/centerline representation.
    """
    body_3d = "body_3d"
    """
    3D volumetric/body representation.
    """
    footprint_2d = "footprint_2d"
    """
    2D surface/footprint representation.
    """
    point = "point"
    """
    Point/dot representation.
    """


class SeparatorSlabType(str, Enum):
    """
    Classification of slab-based separator elements.
    """
    floor = "floor"
    roof = "roof"
    baseslab = "baseslab"
    balcony = "balcony"
    """
    Balcony slab; mapped to FLOOR as the closest IFC slab type.
    """


class SeparatorWallType(str, Enum):
    """
    Classification of wall-based separator elements.
    """
    unit_boundary = "unit_boundary"
    """
    Wall separator that defines boundaries between occupancy units.
    """
    vertical_circulation_boundary = "vertical_circulation_boundary"
    """
    Wall separator that bounds or encloses vertical circulation areas.
    """
    horizontal_circulation_boundary = "horizontal_circulation_boundary"
    """
    Wall separator that bounds or structures horizontal circulation areas.
    """


class SpaceType(str, Enum):
    """
    Classification of space semantics used by modeling and downstream conversion.
    """
    void = "void"
    """
    Non-occupiable or intentionally empty space in the model.
    """
    circulation = "circulation"
    """
    Space primarily intended for movement and access.
    """
    usable = "usable"
    """
    Space intended for regular occupancy or primary use.
    """
    service = "service"
    """
    Space primarily intended for technical/service functions.
    """
    modeled_gross_floor_area = "modeled_gross_floor_area"
    """
    Space classification used when representing gross floor area as modeled space.
    """
    modeled_gross_volume = "modeled_gross_volume"
    """
    Space classification used when representing gross volume as modeled space.
    """


class SystemDiscipline(str, Enum):
    """
    Discipline of a building service system.
    """
    electrical = "electrical"
    """
    Electrical power, lighting, and related electrical services.
    """
    sanitary = "sanitary"
    """
    Water supply, drainage, and sanitary plumbing services.
    """
    ventilation = "ventilation"
    """
    Air movement and ventilation services.
    """
    heating = "heating"
    """
    Heat generation and heat distribution services.
    """


class SystemType(str, Enum):
    """
    Role of an MEP-related element or grouping in the service chain.
    """
    unit = "unit"
    """
    Generating or converting unit (for example AHU, chiller, heat pump).
    """
    network = "network"
    """
    Distribution network element carrying flow (for example ducts, pipes, cable carriers).
    """
    terminal = "terminal"
    """
    End/terminal element located in served spaces.
    """


class TimeDependencyType(str, Enum):
    """
    Precedence logic between two time items.
    """
    finish_to_start = "finish_to_start"
    """
    Successor starts when the predecessor finishes.
    """
    start_to_start = "start_to_start"
    """
    Successor starts when the predecessor starts.
    """
    finish_to_finish = "finish_to_finish"
    """
    Successor finishes when the predecessor finishes.
    """
    start_to_finish = "start_to_finish"
    """
    Successor finishes when the predecessor starts.
    """


class TransportMedium(str, Enum):
    """
    Primary medium transported through or enabled by a physical connector.
    """
    human_access = "human_access"
    """
    Human movement/access medium.
    """
    daylight_view = "daylight_view"
    """
    Daylight/view medium.
    """
    air = "air"
    """
    Air medium.
    """
    liquid = "liquid"
    """
    Liquid medium.
    """
    gas = "gas"
    """
    Gas medium.
    """
    electricity = "electricity"
    """
    Electrical energy medium.
    """
    data = "data"
    """
    Data/signal medium.
    """


class ZoneType(str, Enum):
    """
    Classification of zone purpose and organizational intent.
    """
    occupancy_unit = "occupancy_unit"
    """
    Occupancy unit zone (for example apartment, office suite, or retail unit).
    """
    tenant = "tenant"
    """
    Tenant area zone used for leasing and occupancy boundaries.
    """
    functional = "functional"
    """
    Functional grouping zone (for example clinical, retail, office support).
    """
    cost = "cost"
    """
    Cost grouping zone for estimation and controlling.
    """
    fire = "fire"
    """
    Fire compartment or fire strategy grouping zone.
    """
    security = "security"
    """
    Security management zone for access control and surveillance planning.
    """


class PerformancePropertyValueType(str, Enum):
    """
    Type discriminator for normalized performance property values.
    """
    string = "string"
    number = "number"
    boolean = "boolean"


class FirePropertyKey(str, Enum):
    """
    Canonical fire-related keys derived from IFC PropertySets.
    """
    resistance_rating = "resistance_rating"
    smoke_rating = "smoke_rating"
    reaction_to_fire = "reaction_to_fire"


class AcousticPropertyKey(str, Enum):
    """
    Canonical acoustic-related keys derived from IFC PropertySets.
    """
    rating_db = "rating_db"
    impact_sound_rating_db = "impact_sound_rating_db"
    airborne_sound_rating_db = "airborne_sound_rating_db"


class ThermalPropertyKey(str, Enum):
    """
    Canonical thermal-related keys derived from IFC PropertySets.
    """
    u_value = "u_value"
    r_value = "r_value"
    thermal_transmittance = "thermal_transmittance"


class StructuralPropertyKey(str, Enum):
    """
    Canonical structural-related keys derived from IFC PropertySets.
    """
    load_bearing = "load_bearing"
    stiffness_class = "stiffness_class"
    strength_class = "strength_class"


class SecurityPropertyKey(str, Enum):
    """
    Canonical security-related keys derived from IFC PropertySets.
    """
    access_control_class = "access_control_class"
    intrusion_resistance_class = "intrusion_resistance_class"
    surveillance_coverage = "surveillance_coverage"


class MaterialPropertyKey(str, Enum):
    """
    Canonical material-related keys derived from IFC PropertySets and material metadata.
    """
    material_name = "material_name"
    material_class = "material_class"
    density = "density"
    thermal_conductivity = "thermal_conductivity"


class ConnectionRequirementDriver(str, Enum):
    """
    Main requirement drivers for connection element performance.
    """
    fire = "fire"
    security = "security"
    accessibility = "accessibility"
    acoustic = "acoustic"
    thermal = "thermal"
    visual = "visual"
    structural = "structural"


class SeparatorRequirementDriver(str, Enum):
    """
    Main requirement drivers for separator performance.
    """
    acoustic = "acoustic"
    fire = "fire"
    thermal = "thermal"
    privacy = "privacy"
    hygiene = "hygiene"
    structural = "structural"


class SpatialAdjacencyKind(str, Enum):
    """
    Spatial adjacency semantics for spatial requirements.
    """
    adjacent_to = "adjacent_to"
    """
    Subject must be adjacent to the related entity or space.
    """
    not_adjacent_to = "not_adjacent_to"
    """
    Subject must not be adjacent to the related entity or space.
    """
    min_clear_distance = "min_clear_distance"
    """
    Minimum clear distance to the related entity or space.
    """


class RequirementTargetOperator(str, Enum):
    """
    Comparison operator for numeric or textual requirement targets.
    """
    equals = "equals"
    minimum = "minimum"
    maximum = "maximum"
    range = "range"


class RequirementDomain(str, Enum):
    """
    Domain of a prescriptive requirement record.
    """
    performance = "performance"
    """
    Performance targets (U-value, fire rating, airflow, acoustic, etc.).
    """
    spatial = "spatial"
    """
    Spatial constraints (min area, min height, adjacency, etc.).
    """
    regulatory = "regulatory"
    """
    Regulatory references (building code, norm, standard).
    """
    brief = "brief"
    """
    Client or programme requirement, including free-standing brief items.
    """


class ChangeIntentVerdict(str, Enum):
    """
    Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).
    """
    stable = "stable"
    """
    Change preserves design intent; downstream rules may treat as cosmetic.
    """
    new_intent = "new_intent"
    """
    Change alters design intent; may require re-evaluation or new tasks.
    """


class ChangeSeverity(str, Enum):
    """
    Optional severity of a change independent of change type.
    """
    unchanged = "unchanged"
    """
    No material difference (typically omitted from persisted Change records).
    """
    minor = "minor"
    """
    Small attribute, metadata, or wording adjustment.
    """
    major = "major"
    """
    Significant attribute, geometry, relationship, or structural content change.
    """
    rewritten = "rewritten"
    """
    Subject substantially replaced while retaining the same identity.
    """


class ChangeType(str, Enum):
    """
    Category of change detected between two revisions.
    """
    geometry_change = "geometry_change"
    """
    Geometry or representation changed.
    """
    property_change = "property_change"
    """
    Attribute, PropertySet, or schema slot changed.
    """
    requirement_change = "requirement_change"
    """
    Requirement record or field changed.
    """
    match_change = "match_change"
    """
    Entity match status against a requirement changed (met / unmet).
    """
    addition = "addition"
    """
    New entity or requirement introduced.
    """
    deletion = "deletion"
    """
    Entity or requirement removed.
    """


class MatchStatus(str, Enum):
    """
    Whether an entity satisfies a related requirement at the target revision.
    """
    met = "met"
    """
    Subject satisfies the requirement.
    """
    unmet = "unmet"
    """
    Subject no longer satisfies the requirement.
    """
    unknown = "unknown"
    """
    Match could not be determined.
    """


class PropertyPathKind(str, Enum):
    """
    Classification of a property path for diff interpretation across IFC and text sources.
    """
    ifc_attribute = "ifc_attribute"
    """
    Direct IFC entity attribute (for example IfcWall.Name).
    """
    ifc_pset = "ifc_pset"
    """
    IFC PropertySet property (for example Pset_WallCommon.FireRating).
    """
    schema_slot = "schema_slot"
    """
    Field on a schema entity (for example description, space_type).
    """
    document_field = "document_field"
    """
    Structured field in an extracted document (for example section.4.2.title).
    """
    text_span = "text_span"
    """
    Free-text span anchor (for example body:char_offset:1204-1389).
    """


class StateRefKind(str, Enum):
    """
    Kind of content referenced by a StateRef pointer.
    """
    ifc_model = "ifc_model"
    """
    Whole IFC file or subset export.
    """
    geometry = "geometry"
    """
    Geometry payload or representation blob.
    """
    document = "document"
    """
    Original file in DMS or object storage.
    """
    text_extract = "text_extract"
    """
    Normalized or extracted text used for diffing.
    """
    entity_record = "entity_record"
    """
    Serialized entity record at a specific revision.
    """
    other = "other"
    """
    Other content kind not covered by controlled values.
    """



class Entity(ConfiguredBaseModel):
    """
    Common base class for all schema entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:Entity',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Agent(Entity):
    """
    Abstract base class for people or organizations acting in workflow and communication roles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:Agent',
         'exact_mappings': ['prov:Agent'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    postal_addresses: Optional[list[PostalAddress]] = Field(default=None, description="""Structured postal or physical addresses associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    contact_points: Optional[list[ContactPoint]] = Field(default=None, description="""Structured communication channels and profiles associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Person(Agent):
    """
    Individual stakeholder, contributor, assignee, or responsible party represented in the schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Person',
         'exact_mappings': ['schema:Person', 'prov:Agent'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    belongs_to_company: Optional[str] = Field(default=None, description="""Optional company that the person belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    postal_addresses: Optional[list[PostalAddress]] = Field(default=None, description="""Structured postal or physical addresses associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    contact_points: Optional[list[ContactPoint]] = Field(default=None, description="""Structured communication channels and profiles associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Company(Agent):
    """
    Organization, company, or legal entity participating in the project or asset lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Company',
         'exact_mappings': ['schema:Organization', 'prov:Agent'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    postal_addresses: Optional[list[PostalAddress]] = Field(default=None, description="""Structured postal or physical addresses associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    contact_points: Optional[list[ContactPoint]] = Field(default=None, description="""Structured communication channels and profiles associated with this agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Classification(ConfiguredBaseModel):
    """
    Generic classification entry from any scheme (for example IFC, Uniclass, OmniClass, custom).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Classification',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    classification_scheme: str = Field(default=..., description="""Name of the classification scheme (for example ifc, uniclass, omniclass, custom).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })
    classification_code: str = Field(default=..., description="""Classification code inside the scheme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })
    classification_label: Optional[str] = Field(default=None, description="""Optional human-readable classification label.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })
    classification_uri: Optional[str] = Field(default=None, description="""Optional URI/CURIE that identifies the classification concept in an external registry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })
    classification_version: Optional[str] = Field(default=None, description="""Optional scheme/version identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })
    classification_source: Optional[str] = Field(default=None, description="""Source authority or dataset for this classification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Classification']} })


class GeometryRepresentation(ConfiguredBaseModel):
    """
    Minimal geometry reference for an entity, separating representation from encoding format.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:GeometryRepresentation',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    geometry_reference: str = Field(default=..., description="""URI/path/hash/pointer to geometry payload.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeometryRepresentation']} })
    geometry_representation: GeometryRepresentationType = Field(default=..., description="""Representation kind/dimension (for example body_3d, footprint_2d, point), independent of file format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeometryRepresentation']} })
    geometry_format: Optional[str] = Field(default=None, description="""Optional serialization/encoding format (for example ifc, gltf, wkt, geojson), independent of representation kind.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeometryRepresentation']} })


class QuantityValue(ConfiguredBaseModel):
    """
    Minimal quantity record for costing and analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:QuantityValue',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    quantity_type: QuantityType = Field(default=..., description="""Controlled quantity type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    quantity_value: float = Field(default=..., description="""Numeric quantity value.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    quantity_unit: str = Field(default=..., description="""Unit of the quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })
    quantity_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the quantity unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue']} })


class MetadataEntry(ConfiguredBaseModel):
    """
    Generic metadata entry for storing IFC attributes, PropertySet fields, or project-specific key-value data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:MetadataEntry',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    metadata_key: str = Field(default=..., description="""Metadata key, for example IfcWall.FireRating or Pset_WallCommon.Reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetadataEntry']} })
    metadata_value: Optional[str] = Field(default=None, description="""Metadata value serialized as text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetadataEntry']} })


class PerformanceProperty(ConfiguredBaseModel):
    """
    Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:PerformanceProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    property_key: str = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class Decision(ConfiguredBaseModel):
    """
    Decision record linked to an entity for workflow traceability and governance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Decision',
         'exact_mappings': ['prov:Entity'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    decision_type: Optional[str] = Field(default=None, description="""Decision type expressed as a URI/CURIE from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision'], 'slot_uri': 'dcterms:type'} })
    decision_status: Optional[str] = Field(default=None, description="""Decision status expressed as a URI/CURIE (for example proposed, accepted, rejected, superseded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision'], 'slot_uri': 'adms:status'} })
    decided_by: Optional[str] = Field(default=None, description="""Agent responsible for the decision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision'], 'slot_uri': 'prov:wasAttributedTo'} })
    decided_at: Optional[datetime ] = Field(default=None, description="""Timestamp when the decision was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision'], 'slot_uri': 'dcterms:created'} })
    rationale: Optional[str] = Field(default=None, description="""Human-readable rationale that explains why the decision was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decision'], 'slot_uri': 'dcterms:description'} })


class Task(ConfiguredBaseModel):
    """
    Action/task record linked to an entity for implementation and follow-up workflows.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Task',
         'exact_mappings': ['schema:Action', 'prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core',
         'slot_usage': {'id': {'description': 'Optional stable identifier when '
                                              'referenced externally (for example from '
                                              'Change.triggered_task).',
                               'identifier': False,
                               'name': 'id',
                               'required': False}}})

    id: Optional[str] = Field(default=None, description="""Optional stable identifier when referenced externally (for example from Change.triggered_task).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    task_type: Optional[str] = Field(default=None, description="""Task type expressed as a URI/CURIE from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'dcterms:type'} })
    task_status: Optional[str] = Field(default=None, description="""Task status URI/CURIE aligned with action status vocabularies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'schema:actionStatus'} })
    assignee: Optional[str] = Field(default=None, description="""Responsible agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'schema:agent'} })
    due_at: Optional[datetime ] = Field(default=None, description="""Due timestamp for task completion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'schema:deadline'} })
    related_decision: Optional[Decision] = Field(default=None, description="""Optional reference to a decision that informs or drives this task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'prov:used'} })
    task_notes: Optional[str] = Field(default=None, description="""Additional notes or implementation details for the task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task'], 'slot_uri': 'rdfs:comment'} })


class Message(Entity):
    """
    Message or communication record linked to an entity for coordination and traceability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Message',
         'exact_mappings': ['schema:Message', 'prov:Entity'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    message_type: Optional[str] = Field(default=None, description="""Message type expressed as a URI/CURIE from a controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'dcterms:type'} })
    sender: Optional[str] = Field(default=None, description="""Agent that sent the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'schema:sender'} })
    recipients: Optional[list[str]] = Field(default=None, description="""Agents that received the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'schema:recipient'} })
    sent_at: Optional[datetime ] = Field(default=None, description="""Timestamp when the message was sent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'schema:dateSent'} })
    message_subject: Optional[str] = Field(default=None, description="""Optional subject or headline for the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'schema:headline'} })
    message_body: Optional[str] = Field(default=None, description="""Human-readable message content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message'], 'slot_uri': 'schema:text'} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Document(ConfiguredBaseModel):
    """
    Reference to an external document stored in a file system, DMS, object storage, or URL.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Document',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core',
         'slot_usage': {'id': {'description': 'Optional stable identifier when '
                                              'referenced externally (for example from '
                                              'Change records).',
                               'identifier': False,
                               'name': 'id',
                               'required': False}}})

    id: Optional[str] = Field(default=None, description="""Optional stable identifier when referenced externally (for example from Change records).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    storage_link: str = Field(default=..., description="""URI/URL/path to the stored document location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Document']} })


class PostalAddress(ConfiguredBaseModel):
    """
    Structured postal or physical address for an agent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:PostalAddress',
         'exact_mappings': ['schema:PostalAddress'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    street_address: Optional[str] = Field(default=None, description="""Street name and house number or equivalent address line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:streetAddress'} })
    post_office_box_number: Optional[str] = Field(default=None, description="""Post office box number where applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:postOfficeBoxNumber'} })
    postal_code: Optional[str] = Field(default=None, description="""Postal or ZIP code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:postalCode'} })
    address_locality: Optional[str] = Field(default=None, description="""Locality, city, or town.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:addressLocality'} })
    address_region: Optional[str] = Field(default=None, description="""Region, state, canton, or province.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:addressRegion'} })
    address_country: Optional[str] = Field(default=None, description="""Country name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress'], 'slot_uri': 'schema:addressCountry'} })
    address_country_code: Optional[str] = Field(default=None, description="""Optional ISO 3166-1 alpha-2 or alpha-3 country code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostalAddress']} })


class ContactPoint(ConfiguredBaseModel):
    """
    Structured communication endpoint or profile for an agent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ContactPoint',
         'exact_mappings': ['schema:ContactPoint'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    contact_channel_type: Optional[str] = Field(default=None, description="""Communication channel type such as email, phone, website, linkedin, whatsapp, signal, slack, teams, or telegram.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })
    contact_value: Optional[str] = Field(default=None, description="""Human-readable contact value such as an email address, phone number, handle, or username.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })
    contact_uri: Optional[str] = Field(default=None, description="""URI for the contact endpoint or profile where applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })
    usage_context: Optional[str] = Field(default=None, description="""Optional usage context such as work, personal, support, billing, or emergency.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })
    is_preferred: Optional[bool] = Field(default=None, description="""Indicates whether this is the preferred contact point.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })
    availability_notes: Optional[str] = Field(default=None, description="""Optional notes about availability, office hours, or response expectations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContactPoint']} })


class LocalizedText(ConfiguredBaseModel):
    """
    Localized text value for a specific language tag.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:LocalizedText',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/core'})

    language_tag: str = Field(default=..., description="""IETF BCP 47 language tag (for example en, de, pt-BR).""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizedText']} })
    text_value: str = Field(default=..., description="""Localized text value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalizedText']} })


class FireProperty(PerformanceProperty):
    """
    Normalized fire-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:FireProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'FirePropertyKey'}}})

    property_key: FirePropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class AcousticProperty(PerformanceProperty):
    """
    Normalized acoustic-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:AcousticProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'AcousticPropertyKey'}}})

    property_key: AcousticPropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class ThermalProperty(PerformanceProperty):
    """
    Normalized thermal-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ThermalProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'ThermalPropertyKey'}}})

    property_key: ThermalPropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class StructuralProperty(PerformanceProperty):
    """
    Normalized structural-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:StructuralProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'StructuralPropertyKey'}}})

    property_key: StructuralPropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class SecurityProperty(PerformanceProperty):
    """
    Normalized security-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:SecurityProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'SecurityPropertyKey'}}})

    property_key: SecurityPropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class MaterialProperty(PerformanceProperty):
    """
    Normalized material-related property.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:MaterialProperty',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/performance',
         'slot_usage': {'property_key': {'name': 'property_key',
                                         'range': 'MaterialPropertyKey'}}})

    property_key: MaterialPropertyKey = Field(default=..., description="""Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_type: PerformancePropertyValueType = Field(default=..., description="""Value type discriminator for normalized storage (for example string, number, boolean).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_string: Optional[str] = Field(default=None, description="""String value when property_value_type is string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_number: Optional[float] = Field(default=None, description="""Numeric value when property_value_type is number.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_value_boolean: Optional[bool] = Field(default=None, description="""Boolean value when property_value_type is boolean.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit: Optional[str] = Field(default=None, description="""Normalized unit where applicable (for example min, dB, W/m2K).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    property_unit_uri: Optional[str] = Field(default=None, description="""Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_value_raw: Optional[str] = Field(default=None, description="""Raw source value before normalization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })
    mapping_version: Optional[str] = Field(default=None, description="""Mapping specification version used to derive the normalized property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty']} })


class Requirement(ConfiguredBaseModel):
    """
    Prescriptive requirement record (content_kind requirement). Not an Entity; may apply to one or more model entities.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:Requirement',
         'from_schema': 'https://schema.pragmaticbim.ch/requirements',
         'slot_usage': {'id': {'identifier': True, 'name': 'id', 'required': True}}})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    requirement_domain: RequirementDomain = Field(default=..., description="""Domain of this requirement record (performance, spatial, regulatory, brief).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    source_document: Optional[str] = Field(default=None, description="""Optional URI to norm, brief, or source document backing this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })


class PerformanceRequirement(Requirement):
    """
    Performance target requirement (U-value, fire rating, airflow, acoustic, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:PerformanceRequirement',
         'from_schema': 'https://schema.pragmaticbim.ch/requirements',
         'slot_usage': {'requirement_domain': {'equals_string': 'performance',
                                               'name': 'requirement_domain',
                                               'range': 'string'}}})

    requirement_property_key: str = Field(default=..., description="""Canonical performance key for the target (for example u_value, resistance_rating). Aligns with performance property keys where applicable.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_operator: Optional[RequirementTargetOperator] = Field(default=None, description="""Comparison operator for the requirement target.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_value_string: Optional[str] = Field(default=None, description="""Textual target value when applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_value_number: Optional[float] = Field(default=None, description="""Numeric target value when applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_value_boolean: Optional[bool] = Field(default=None, description="""Boolean target value when applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_unit: Optional[str] = Field(default=None, description="""Unit for numeric targets (for example W/m2K, min, dB).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    target_unit_uri: Optional[str] = Field(default=None, description="""Optional URI identifying the target unit (for example QUDT).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceRequirement']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    requirement_domain: Literal["performance"] = Field(default=..., description="""Domain of this requirement record (performance, spatial, regulatory, brief).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement'], 'equals_string': 'performance'} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    source_document: Optional[str] = Field(default=None, description="""Optional URI to norm, brief, or source document backing this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })


class SpatialRequirement(Requirement):
    """
    Spatial constraint requirement (min area, min height, adjacency, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:SpatialRequirement',
         'from_schema': 'https://schema.pragmaticbim.ch/requirements',
         'slot_usage': {'requirement_domain': {'equals_string': 'spatial',
                                               'name': 'requirement_domain',
                                               'range': 'string'}}})

    min_area: Optional[float] = Field(default=None, description="""Minimum required area in square metres.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialRequirement']} })
    min_height: Optional[float] = Field(default=None, description="""Minimum required height or clear height in metres.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialRequirement']} })
    adjacency_kind: Optional[SpatialAdjacencyKind] = Field(default=None, description="""Adjacency semantics when this spatial requirement involves another subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialRequirement']} })
    related_entity: Optional[str] = Field(default=None, description="""Entity or space subject for adjacency or distance constraints.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialRequirement']} })
    min_clear_distance: Optional[float] = Field(default=None, description="""Minimum clear distance in metres when adjacency_kind is min_clear_distance.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialRequirement']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    requirement_domain: Literal["spatial"] = Field(default=..., description="""Domain of this requirement record (performance, spatial, regulatory, brief).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement'], 'equals_string': 'spatial'} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    source_document: Optional[str] = Field(default=None, description="""Optional URI to norm, brief, or source document backing this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })


class RegulatoryRequirement(Requirement):
    """
    Regulatory reference requirement (building code, norm, standard).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:RegulatoryRequirement',
         'from_schema': 'https://schema.pragmaticbim.ch/requirements',
         'slot_usage': {'requirement_domain': {'equals_string': 'regulatory',
                                               'name': 'requirement_domain',
                                               'range': 'string'}}})

    norm_uri: Optional[str] = Field(default=None, description="""URI identifying the norm, standard, or building code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegulatoryRequirement']} })
    clause_ref: Optional[str] = Field(default=None, description="""Clause, article, or section reference within the norm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegulatoryRequirement']} })
    jurisdiction: Optional[str] = Field(default=None, description="""Jurisdiction or authority scope for the regulatory requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegulatoryRequirement']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    requirement_domain: Literal["regulatory"] = Field(default=..., description="""Domain of this requirement record (performance, spatial, regulatory, brief).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement'], 'equals_string': 'regulatory'} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    source_document: Optional[str] = Field(default=None, description="""Optional URI to norm, brief, or source document backing this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })


class BriefRequirement(Requirement):
    """
    Client or programme requirement, including free-standing brief items.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:BriefRequirement',
         'from_schema': 'https://schema.pragmaticbim.ch/requirements',
         'slot_usage': {'requirement_domain': {'equals_string': 'brief',
                                               'name': 'requirement_domain',
                                               'range': 'string'}}})

    programme_ref: Optional[str] = Field(default=None, description="""URI or identifier for a programme or brief document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BriefRequirement']} })
    statement: Optional[str] = Field(default=None, description="""Free-text requirement statement from client or programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BriefRequirement']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    requirement_domain: Literal["brief"] = Field(default=..., description="""Domain of this requirement record (performance, spatial, regulatory, brief).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement'], 'equals_string': 'brief'} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    source_document: Optional[str] = Field(default=None, description="""Optional URI to norm, brief, or source document backing this requirement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })


class PhysicalElement(Entity):
    """
    Base class for physical elements that can be placed in built asset/level context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:PhysicalElement',
         'exact_mappings': ['bot:Element', 'ifcowl:IfcElement'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical',
         'slot_usage': {'parent_building': {'name': 'parent_building',
                                            'range': 'BuiltAssetContext'},
                        'parent_level': {'name': 'parent_level',
                                         'range': 'LevelContext'}}})

    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Separator(PhysicalElement):
    """
    Abstract base class for elements that separate spaces or zones.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:Separator',
         'exact_mappings': ['ifcowl:IfcBuildingElement'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    separator_requirement_drivers: Optional[list[SeparatorRequirementDriver]] = Field(default=None, description="""Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Separator']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class SeparatorWall(Separator):
    """
    Wall-based separating element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:SeparatorWall',
         'exact_mappings': ['ifcowl:IfcWall'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    separator_wall_type: SeparatorWallType = Field(default=..., description="""Classification of wall-based separator element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeparatorWall']} })
    separates_spaces: Optional[list[str]] = Field(default=None, description="""Spaces separated by this separator element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeparatorWall']} })
    separator_requirement_drivers: Optional[list[SeparatorRequirementDriver]] = Field(default=None, description="""Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Separator']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class SeparatorSlab(Separator):
    """
    Slab-based separating element (for example floor/roof/base slab separators).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:SeparatorSlab',
         'exact_mappings': ['ifcowl:IfcSlab'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    separator_slab_type: SeparatorSlabType = Field(default=..., description="""Classification of slab-based separator element (for example floor/roof/base slab).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeparatorSlab']} })
    separates_levels: Optional[list[str]] = Field(default=None, description="""Level context nodes separated by this slab separator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SeparatorSlab']} })
    separator_requirement_drivers: Optional[list[SeparatorRequirementDriver]] = Field(default=None, description="""Performance requirement drivers for this separator. Multiple values are allowed because one separator may need to satisfy several requirements.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Separator']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class ConnectionPhysical(PhysicalElement):
    """
    Physical connector providing functional connection between spaces (for example door, window, duct, pipe, cable).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ConnectionPhysical',
         'exact_mappings': ['ifcowl:IfcDoor',
                            'ifcowl:IfcWindow',
                            'ifcowl:IfcFlowSegment',
                            'ifcowl:IfcCableCarrierSegment'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    connection_physical_type: ConnectionPhysicalType = Field(default=..., description="""Classification of physical connector type (for example door, window, duct, pipe, cable).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionPhysical']} })
    transport_medium: TransportMedium = Field(default=..., description="""Primary transport medium carried or enabled by the connector (for example human_access, air, liquid, electricity).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionPhysical']} })
    connection_physical_requirement_drivers: Optional[list[ConnectionRequirementDriver]] = Field(default=None, description="""Performance requirement drivers for this physical connection element. Multiple values are allowed because one connection may need to satisfy several requirements.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionPhysical']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Boundary(PhysicalElement):
    """
    Physical element acting as a boundary treatment (for example covering).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Boundary',
         'exact_mappings': ['ifcowl:IfcCovering'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    boundary_type: BoundaryType = Field(default=..., description="""Classification of boundary element (e.g., covering).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boundary']} })
    bounded_space: Optional[str] = Field(default=None, description="""Space bounded by this boundary element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boundary'], 'inverse': 'bounded_by'} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Equipment(PhysicalElement):
    """
    Endpoint or device element (for example terminal, unit, control device, sensor) located in a space and assigned to a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Equipment',
         'exact_mappings': ['bot:Element', 'ifcowl:IfcDistributionElement'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/physical'})

    equipment_type: EquipmentType = Field(default=..., description="""Classification of equipment (for example HVAC, electrical, plumbing).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Equipment']} })
    parent_space: Optional[str] = Field(default=None, description="""Parent space where the equipment is located.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Equipment'], 'inverse': 'contained_entities'} })
    parent_system: Optional[list[str]] = Field(default=None, description="""Parent systems that the equipment belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Equipment']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class VirtualEntity(Entity):
    """
    Abstract base class for non-physical, conceptual, or informational entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:VirtualEntity',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class SpatialContext(VirtualEntity):
    """
    Context node used to represent project, perimeter, legal site, built asset, level, or zone.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:SpatialContext',
         'exact_mappings': ['ifcowl:IfcSpatialStructureElement'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual',
         'slot_usage': {'parent_building': {'name': 'parent_building',
                                            'range': 'BuiltAssetContext'},
                        'parent_legal_site': {'name': 'parent_legal_site',
                                              'range': 'LegalSiteContext'},
                        'parent_level': {'name': 'parent_level',
                                         'range': 'LevelContext'},
                        'parent_perimeter': {'name': 'parent_perimeter',
                                             'range': 'PerimeterContext'},
                        'parent_project': {'name': 'parent_project',
                                           'range': 'ProjectContext'},
                        'parent_zone': {'name': 'parent_zone', 'range': 'ZoneContext'}},
         'tree_root': True})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class ProjectContext(SpatialContext):
    """
    Spatial context node constrained to project semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ProjectContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class PerimeterContext(SpatialContext):
    """
    Spatial context node constrained to perimeter semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:PerimeterContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class LegalSiteContext(SpatialContext):
    """
    Spatial context node constrained to legal site semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:LegalSiteContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class BuiltAssetContext(SpatialContext):
    """
    Abstract spatial context for built assets such as buildings and civil structures.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:BuiltAssetContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class BuildingContext(BuiltAssetContext):
    """
    Spatial context node constrained to building semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:BuildingContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class CivilStructureContext(BuiltAssetContext):
    """
    Spatial context node constrained to civil structure semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:CivilStructureContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class LevelContext(SpatialContext):
    """
    Spatial context node constrained to level/storey semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:LevelContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class ZoneContext(SpatialContext):
    """
    Spatial context node constrained to zone semantics.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ZoneContext',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    context_type: ContextType = Field(default=..., description="""Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    zone_type: Optional[ZoneType] = Field(default=None, description="""Optional zone classification; intended for SpatialContext nodes where context_type is zone.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_perimeter: Optional[str] = Field(default=None, description="""Parent perimeter context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_legal_site: Optional[str] = Field(default=None, description="""Parent legal site context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    group_members: Optional[list[str]] = Field(default=None, description="""Zone members; may include spaces, separations, systems, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Space(VirtualEntity):
    """
    Spatial container used for occupancy, circulation, service, or analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Space',
         'exact_mappings': ['bot:Space', 'ifcowl:IfcSpace'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual',
         'slot_usage': {'parent_building': {'name': 'parent_building',
                                            'range': 'BuiltAssetContext'},
                        'parent_level': {'name': 'parent_level',
                                         'range': 'LevelContext'}}})

    space_type: SpaceType = Field(default=..., description="""Classification of space (void, circulation, usable, service).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Space']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    parent_level: Optional[str] = Field(default=None, description="""Parent level/storey context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space']} })
    parent_zone: Optional[str] = Field(default=None, description="""Parent zone context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'Space']} })
    bounded_by: Optional[list[str]] = Field(default=None, description="""Physical elements that bound a space.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Space'], 'inverse': 'bounded_space'} })
    contained_entities: Optional[list[str]] = Field(default=None, description="""Generic containment for associated entities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Space', 'System']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class System(VirtualEntity):
    """
    Building service system grouping that serves spaces or zones.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:System',
         'exact_mappings': ['ifcowl:IfcSystem'],
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual',
         'slot_usage': {'parent_building': {'name': 'parent_building',
                                            'range': 'BuiltAssetContext'},
                        'parent_project': {'name': 'parent_project',
                                           'range': 'ProjectContext'}}})

    system_type: SystemType = Field(default=..., description="""Classification of system role (unit, network, terminal).""", json_schema_extra = { "linkml_meta": {'domain_of': ['System']} })
    system_discipline: SystemDiscipline = Field(default=..., description="""Classification of system discipline (electrical, sanitary, ventilation, heating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['System']} })
    parent_project: Optional[str] = Field(default=None, description="""Parent project context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialContext', 'System']} })
    parent_building: Optional[str] = Field(default=None, description="""Parent building context reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhysicalElement', 'SpatialContext', 'Space', 'System']} })
    serves_spaces: Optional[list[str]] = Field(default=None, description="""Spaces served by this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System']} })
    serves_zones: Optional[list[str]] = Field(default=None, description="""Zone context nodes served by this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['System']} })
    contained_entities: Optional[list[str]] = Field(default=None, description="""Generic containment for associated entities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Space', 'System']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class ConnectionVirtual(VirtualEntity):
    """
    Logical or topological connection between spaces and/or physical elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ConnectionVirtual',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    connection_virtual_type: ConnectionVirtualType = Field(default=..., description="""Classification of virtual connection semantics (for example structural_joint, adjacency, access).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionVirtual']} })
    connects_physical_elements: Optional[list[str]] = Field(default=None, description="""Physical elements connected by this virtual connection (for example wall-wall, wall-slab).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionVirtual']} })
    connects_spaces: Optional[list[str]] = Field(default=None, description="""Spaces connected by this virtual connection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionVirtual']} })
    connection_virtual_requirement_drivers: Optional[list[ConnectionRequirementDriver]] = Field(default=None, description="""Main requirement drivers for this virtual connection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectionVirtual']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class AbstractTimeRecord(VirtualEntity):
    """
    Abstract base for reusable time/schedule record fields shared by atomic and grouped time records.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:AbstractTimeRecord',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class TimeItem(AbstractTimeRecord):
    """
    Planned work item with baseline and actual dates, optionally linked to model entities and a time plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:TimeItem',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    time_plan: Optional[str] = Field(default=None, description="""Parent time plan this item or dependency belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem', 'TimeDependency']} })
    planned_start_at: Optional[datetime ] = Field(default=None, description="""Planned start timestamp for the time item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    planned_finish_at: Optional[datetime ] = Field(default=None, description="""Planned finish timestamp for the time item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    actual_start_at: Optional[datetime ] = Field(default=None, description="""Actual start timestamp for the time item where known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    actual_finish_at: Optional[datetime ] = Field(default=None, description="""Actual finish timestamp for the time item where known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Milestone(TimeItem):
    """
    Zero-duration checkpoint or delivery target within a time plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Milestone',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    milestone_at: Optional[datetime ] = Field(default=None, description="""Target timestamp for the milestone checkpoint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Milestone']} })
    time_plan: Optional[str] = Field(default=None, description="""Parent time plan this item or dependency belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem', 'TimeDependency']} })
    planned_start_at: Optional[datetime ] = Field(default=None, description="""Planned start timestamp for the time item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    planned_finish_at: Optional[datetime ] = Field(default=None, description="""Planned finish timestamp for the time item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    actual_start_at: Optional[datetime ] = Field(default=None, description="""Actual start timestamp for the time item where known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    actual_finish_at: Optional[datetime ] = Field(default=None, description="""Actual finish timestamp for the time item where known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class TimePlan(AbstractTimeRecord):
    """
    Grouped schedule container defining component items, milestones, and dependencies for a scoped plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:TimePlan',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    component_time_items: Optional[list[str]] = Field(default=None, description="""Time items contained in this plan; milestone instances may also appear through the TimeItem subtype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimePlan']} })
    time_dependencies: Optional[list[str]] = Field(default=None, description="""Dependency relationships used within this time plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimePlan']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class TimeDependency(VirtualEntity):
    """
    Precedence relationship between two time items within a plan, optionally with lag.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:TimeDependency',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    time_plan: Optional[str] = Field(default=None, description="""Parent time plan this item or dependency belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeItem', 'TimeDependency']} })
    predecessor_item: Optional[str] = Field(default=None, description="""Time item that must occur before the successor item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeDependency']} })
    successor_item: Optional[str] = Field(default=None, description="""Time item whose timing is constrained by the predecessor item.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeDependency']} })
    dependency_type: TimeDependencyType = Field(default=..., description="""Precedence logic used between the predecessor and successor items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeDependency']} })
    lag_days: Optional[float] = Field(default=None, description="""Optional lag or lead offset in days applied to the dependency relation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeDependency']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class AbstractCostRecord(VirtualEntity):
    """
    Abstract base for reusable cost record fields shared by atomic and aggregated cost records.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:AbstractCostRecord',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    cost_category: Optional[str] = Field(default=None, description="""Cost category label kept intentionally open pending classification-backed modeling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    unit_cost: float = Field(default=..., description="""Unit cost for this cost item.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    currency: str = Field(default=..., description="""ISO 4217 currency code (for example EUR, USD).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_type: Optional[QuantityType] = Field(default=None, description="""Quantity type used as basis for this cost calculation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_value: Optional[float] = Field(default=None, description="""Quantity magnitude used as basis for this cost calculation.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_unit: Optional[str] = Field(default=None, description="""Unit of the cost quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('currency')
    def pattern_currency(cls, v):
        pattern=re.compile(r"^[A-Z]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid currency format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid currency format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class CostItem(AbstractCostRecord):
    """
    Cost record used for estimation and calculation, optionally linked to quantities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:CostItem',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    cost_category: Optional[str] = Field(default=None, description="""Cost category label kept intentionally open pending classification-backed modeling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    unit_cost: float = Field(default=..., description="""Unit cost for this cost item.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    currency: str = Field(default=..., description="""ISO 4217 currency code (for example EUR, USD).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_type: Optional[QuantityType] = Field(default=None, description="""Quantity type used as basis for this cost calculation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_value: Optional[float] = Field(default=None, description="""Quantity magnitude used as basis for this cost calculation.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_unit: Optional[str] = Field(default=None, description="""Unit of the cost quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('currency')
    def pattern_currency(cls, v):
        pattern=re.compile(r"^[A-Z]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid currency format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid currency format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class CostAssembly(AbstractCostRecord):
    """
    Aggregated unit price assembled from multiple cost items.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:CostAssembly',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    component_cost_items: Optional[list[str]] = Field(default=None, description="""Atomic cost items that are aggregated into this cost assembly.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CostAssembly']} })
    cost_category: Optional[str] = Field(default=None, description="""Cost category label kept intentionally open pending classification-backed modeling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    unit_cost: float = Field(default=..., description="""Unit cost for this cost item.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    currency: str = Field(default=..., description="""ISO 4217 currency code (for example EUR, USD).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_type: Optional[QuantityType] = Field(default=None, description="""Quantity type used as basis for this cost calculation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_value: Optional[float] = Field(default=None, description="""Quantity magnitude used as basis for this cost calculation.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    cost_quantity_unit: Optional[str] = Field(default=None, description="""Unit of the cost quantity value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AbstractCostRecord']} })
    applies_to_entities: Optional[list[str]] = Field(default=None, description="""Model entities this record applies to (requirements, cost items, schedule items, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Requirement', 'AbstractTimeRecord', 'AbstractCostRecord']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('currency')
    def pattern_currency(cls, v):
        pattern=re.compile(r"^[A-Z]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid currency format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid currency format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class Material(VirtualEntity):
    """
    Material definition that can be associated with one or more entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:Material',
         'from_schema': 'https://schema.pragmaticbim.ch/entity/virtual'})

    material_category: Optional[str] = Field(default=None, description="""Material category label kept intentionally open pending classification-backed modeling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Material']} })
    material_specification: Optional[str] = Field(default=None, description="""Material grade, specification, or product description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Material']} })
    cost_items: Optional[list[str]] = Field(default=None, description="""Cost items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    cost_assemblies: Optional[list[str]] = Field(default=None, description="""Aggregated unit prices associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_items: Optional[list[str]] = Field(default=None, description="""Time items associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    time_plans: Optional[list[str]] = Field(default=None, description="""Grouped time plans associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    materials: Optional[list[str]] = Field(default=None, description="""Material definitions associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualEntity']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    name: str = Field(default=..., description="""Default display name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    localized_names: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    description: Optional[str] = Field(default=None, description="""Default description text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })
    meaning_uri: Optional[str] = Field(default=None, description="""Optional semantic URI for linking the entity instance to an external ontology concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    localized_descriptions: Optional[list[LocalizedText]] = Field(default=None, description="""Localized variants of description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    classifications: Optional[list[Classification]] = Field(default=None, description="""Classification entries from IFC and other schemes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Document']} })
    geometry_representations: Optional[list[GeometryRepresentation]] = Field(default=None, description="""Geometry references associated with the entity. A single element may link to multiple geometry representations to serve different intents (authoring, coordination, analysis, visualization) without duplicating the element itself.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    quantity_values: Optional[list[QuantityValue]] = Field(default=None, description="""Quantities associated with the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    documents: Optional[list[Document]] = Field(default=None, description="""Linked documents associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    metadata: Optional[list[MetadataEntry]] = Field(default=None, description="""Generic metadata container for IFC attributes/properties and project-specific extensions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    performance_properties: Optional[list[PerformanceProperty]] = Field(default=None, description="""Normalized, strongly typed domain properties (fire/acoustic/thermal/structural/ security/material) extracted from raw IFC PropertySet values.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    decisions: Optional[list[Decision]] = Field(default=None, description="""Decision records associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""Tasks associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    messages: Optional[dict[str, Message]] = Field(default=None, description="""Messages associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    created_at: Optional[datetime ] = Field(default=None, description="""Creation timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    modified_at: Optional[datetime ] = Field(default=None, description="""Last modification timestamp for this entity record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    revision: Optional[int] = Field(default=None, description="""Integer revision counter for change tracking.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Entity']} })
    status: Optional[StatusType] = Field(default=None, description="""Lifecycle or QA status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Requirement']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class StateRef(ConfiguredBaseModel):
    """
    Pointer to a content state at a specific revision. Covers IFC models, geometry payloads, documents, and extracted text.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:StateRef',
         'from_schema': 'https://schema.pragmaticbim.ch/changes'})

    state_ref: str = Field(default=..., description="""URI, path, or content hash identifying the stored content state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StateRef']} })
    state_ref_kind: StateRefKind = Field(default=..., description="""Kind of content referenced (for example ifc_model, document, text_extract).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StateRef']} })
    state_ref_format: Optional[str] = Field(default=None, description="""Optional serialization format (for example ifc, gltf, pdf, docx, markdown, plain_text, json).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['StateRef']} })
    state_ref_label: Optional[str] = Field(default=None, description="""Optional human-readable label (for example LOD300 export, Spec v3 draft).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StateRef']} })


class PropertyDelta(ConfiguredBaseModel):
    """
    Field-level difference between two revision states. Supports IFC attributes, PropertySets, schema slots, document fields, and text spans.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:PropertyDelta',
         'from_schema': 'https://schema.pragmaticbim.ch/changes'})

    property_path: str = Field(default=..., description="""Canonical path to the changed field. Examples: Pset_WallCommon.FireRating, IfcWall.Name, description, section.4.2.requirement_3, body:char_offset:1204-1389.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyDelta']} })
    property_path_kind: PropertyPathKind = Field(default=..., description="""Classification of the property path for downstream diff interpretation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyDelta']} })
    from_value: Optional[str] = Field(default=None, description="""Prior value serialized as text. Absent or null for new subjects or fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyDelta']} })
    to_value: Optional[str] = Field(default=None, description="""New value serialized as text. Absent or null for deleted subjects or fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyDelta']} })
    source_pset: Optional[str] = Field(default=None, description="""Original IFC PropertySet name (for example Pset_WallCommon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    source_property: Optional[str] = Field(default=None, description="""Original property name inside the source PropertySet (for example FireRating).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PerformanceProperty', 'PropertyDelta']} })
    ifc_attribute_name: Optional[str] = Field(default=None, description="""IFC attribute name when property_path_kind is ifc_attribute (for example Name, GlobalId).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyDelta']} })


class Change(ConfiguredBaseModel):
    """
    Detected difference for one subject between two revisions (content_kind change). Supports IFC model diffs, document/text diffs, and schema-entity field changes.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'pbs:Change',
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'name': 'change_type', 'required': True},
                        'id': {'identifier': True, 'name': 'id', 'required': True}}})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: ChangeType = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class PropertyChange(Change):
    """
    Attribute, PropertySet, schema slot, or document field change.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:PropertyChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'property_change',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    property_delta: Optional[list[PropertyDelta]] = Field(default=None, description="""Field-level differences detected between the two revision states.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyChange', 'RequirementChange']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["property_change"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'property_change'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class GeometryChange(Change):
    """
    Geometry or representation change for a subject.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:GeometryChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'geometry_change',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    affected_geometry_role: Optional[GeometryRepresentationType] = Field(default=None, description="""Geometry role affected when change_type is geometry_change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeometryChange']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["geometry_change"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'geometry_change'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class RequirementChange(Change):
    """
    Change to a requirement record or its fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:RequirementChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'requirement_change',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    affected_requirement_id: Optional[str] = Field(default=None, description="""Identifier of the requirement record affected by this change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequirementChange']} })
    property_delta: Optional[list[PropertyDelta]] = Field(default=None, description="""Field-level differences detected between the two revision states.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PropertyChange', 'RequirementChange']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["requirement_change"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'requirement_change'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class MatchChange(Change):
    """
    Entity match status against a requirement changed (previously met / no longer meets).

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:MatchChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'match_change',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    related_requirement_id: str = Field(default=..., description="""Requirement identifier for match_change records.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MatchChange']} })
    match_status: MatchStatus = Field(default=..., description="""Whether the subject met the requirement at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MatchChange']} })
    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["match_change"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'match_change'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class AdditionChange(Change):
    """
    New entity or requirement introduced in to_revision.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:AdditionChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'addition',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["addition"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'addition'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class DeletionChange(Change):
    """
    Entity or requirement removed in to_revision.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:DeletionChange',
         'exact_mappings': ['prov:Activity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'change_type': {'equals_string': 'deletion',
                                        'name': 'change_type',
                                        'range': 'string'}}})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    change_type: Literal["deletion"] = Field(default=..., description="""Category of change detected between two revisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'equals_string': 'deletion'} })
    change_severity: Optional[ChangeSeverity] = Field(default=None, description="""Optional severity independent of change type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    intent_verdict: Optional[ChangeIntentVerdict] = Field(default=None, description="""Intent stability verdict from an automated judge (for example iterthink STABLE/NEW).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_id: str = Field(default=..., description="""Identifier of the changed subject (entity id, document id, or external key).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_type: str = Field(default=..., description="""LinkML class name of the changed subject (for example Space, SeparatorWall, Document).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    affected_subject_path: Optional[str] = Field(default=None, description="""Optional JSON-pointer-style path for nested targets (for example documents[2], localized_descriptions[de], section.4.2.paragraph_1).
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    ifc_global_id: Optional[str] = Field(default=None, description="""IFC GlobalId of the mapped entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Change']} })
    document_storage_link: Optional[str] = Field(default=None, description="""Document location when the subject is or embeds a Document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    from_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the source revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    to_state_ref: Optional[StateRef] = Field(default=None, description="""Content state pointer at the target revision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_task: Optional[str] = Field(default=None, description="""Id of a Task record that this change triggered or should trigger.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    triggered_process: Optional[str] = Field(default=None, description="""External workflow process URI (for example yourcompanyos process instance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })
    detected_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this change was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change'], 'slot_uri': 'dcterms:created'} })
    change_source: Optional[str] = Field(default=None, description="""URI identifying the tool or pipeline that produced this change record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Change']} })

    @field_validator('ifc_global_id')
    def pattern_ifc_global_id(cls, v):
        pattern=re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ifc_global_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ifc_global_id format: {v}"
            raise ValueError(err_msg)
        return v


class ChangeSet(ConfiguredBaseModel):
    """
    Batch of Change records produced by comparing two model or document revisions.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pbs:ChangeSet',
         'exact_mappings': ['prov:Entity'],
         'from_schema': 'https://schema.pragmaticbim.ch/changes',
         'slot_usage': {'id': {'identifier': True, 'name': 'id', 'required': True}}})

    id: str = Field(default=..., description="""Unique local identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity',
                       'Task',
                       'Document',
                       'Requirement',
                       'Change',
                       'ChangeSet']} })
    from_revision: int = Field(default=..., description="""Source revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    to_revision: int = Field(default=..., description="""Target revision number for this change.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Change', 'ChangeSet']} })
    changes: Optional[dict[str, Change]] = Field(default=None, description="""Change records included in this batch.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeSet']} })
    ifc_state_ref: Optional[StateRef] = Field(default=None, description="""Optional baseline IFC model state for the comparison that produced this changeset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeSet']} })
    document_state_refs: Optional[list[StateRef]] = Field(default=None, description="""Optional baseline document states for the comparison that produced this changeset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeSet']} })
    produced_at: Optional[datetime ] = Field(default=None, description="""Timestamp when this changeset was produced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeSet'], 'slot_uri': 'dcterms:created'} })
    produced_by: Optional[str] = Field(default=None, description="""Agent or system that produced this changeset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ChangeSet'], 'slot_uri': 'prov:wasAttributedTo'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
Agent.model_rebuild()
Person.model_rebuild()
Company.model_rebuild()
Classification.model_rebuild()
GeometryRepresentation.model_rebuild()
QuantityValue.model_rebuild()
MetadataEntry.model_rebuild()
PerformanceProperty.model_rebuild()
Decision.model_rebuild()
Task.model_rebuild()
Message.model_rebuild()
Document.model_rebuild()
PostalAddress.model_rebuild()
ContactPoint.model_rebuild()
LocalizedText.model_rebuild()
FireProperty.model_rebuild()
AcousticProperty.model_rebuild()
ThermalProperty.model_rebuild()
StructuralProperty.model_rebuild()
SecurityProperty.model_rebuild()
MaterialProperty.model_rebuild()
Requirement.model_rebuild()
PerformanceRequirement.model_rebuild()
SpatialRequirement.model_rebuild()
RegulatoryRequirement.model_rebuild()
BriefRequirement.model_rebuild()
PhysicalElement.model_rebuild()
Separator.model_rebuild()
SeparatorWall.model_rebuild()
SeparatorSlab.model_rebuild()
ConnectionPhysical.model_rebuild()
Boundary.model_rebuild()
Equipment.model_rebuild()
VirtualEntity.model_rebuild()
SpatialContext.model_rebuild()
ProjectContext.model_rebuild()
PerimeterContext.model_rebuild()
LegalSiteContext.model_rebuild()
BuiltAssetContext.model_rebuild()
BuildingContext.model_rebuild()
CivilStructureContext.model_rebuild()
LevelContext.model_rebuild()
ZoneContext.model_rebuild()
Space.model_rebuild()
System.model_rebuild()
ConnectionVirtual.model_rebuild()
AbstractTimeRecord.model_rebuild()
TimeItem.model_rebuild()
Milestone.model_rebuild()
TimePlan.model_rebuild()
TimeDependency.model_rebuild()
AbstractCostRecord.model_rebuild()
CostItem.model_rebuild()
CostAssembly.model_rebuild()
Material.model_rebuild()
StateRef.model_rebuild()
PropertyDelta.model_rebuild()
Change.model_rebuild()
PropertyChange.model_rebuild()
GeometryChange.model_rebuild()
RequirementChange.model_rebuild()
MatchChange.model_rebuild()
AdditionChange.model_rebuild()
DeletionChange.model_rebuild()
ChangeSet.model_rebuild()

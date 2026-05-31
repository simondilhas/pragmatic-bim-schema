---
search:
  boost: 10.0
---

# Class: PerformanceProperty 


_Normalized performance/property record derived from raw IFC PropertySet values with source traceability and strong typing through domain-specific subclasses._

__



<div data-search-exclude markdown="1">


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [pbs:PerformanceProperty](https://schema.pragmaticbim.ch/PerformanceProperty)





```mermaid
 classDiagram
    class PerformanceProperty
    click PerformanceProperty href "./PerformanceProperty.html"
      PerformanceProperty <|-- FireProperty
        click FireProperty href "./FireProperty.html"
      PerformanceProperty <|-- AcousticProperty
        click AcousticProperty href "./AcousticProperty.html"
      PerformanceProperty <|-- ThermalProperty
        click ThermalProperty href "./ThermalProperty.html"
      PerformanceProperty <|-- StructuralProperty
        click StructuralProperty href "./StructuralProperty.html"
      PerformanceProperty <|-- SecurityProperty
        click SecurityProperty href "./SecurityProperty.html"
      PerformanceProperty <|-- MaterialProperty
        click MaterialProperty href "./MaterialProperty.html"
      PerformanceProperty : mapping_version
      PerformanceProperty : property_key
      PerformanceProperty : property_unit
      PerformanceProperty : property_unit_uri
      PerformanceProperty : property_value_boolean
      PerformanceProperty : property_value_number
      PerformanceProperty : property_value_string
      PerformanceProperty : property_value_type
        PerformanceProperty --> "1" PerformancePropertyValueType : property_value_type
        click PerformancePropertyValueType href "./PerformancePropertyValueType.html"
      PerformanceProperty : source_property
      PerformanceProperty : source_pset
      PerformanceProperty : source_value_raw
```





## Inheritance
* **PerformanceProperty**
    * [FireProperty](FireProperty.md)
    * [AcousticProperty](AcousticProperty.md)
    * [ThermalProperty](ThermalProperty.md)
    * [StructuralProperty](StructuralProperty.md)
    * [SecurityProperty](SecurityProperty.md)
    * [MaterialProperty](MaterialProperty.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:PerformanceProperty](https://schema.pragmaticbim.ch/PerformanceProperty) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [property_key](property_key.md) | 1 <br/> [String](String.md) | Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum. | direct |
| [property_value_type](property_value_type.md) | 1 <br/> [PerformancePropertyValueType](PerformancePropertyValueType.md) | Value type discriminator for normalized storage (for example string, number, boolean). | direct |
| [property_value_string](property_value_string.md) | 0..1 <br/> [String](String.md) | String value when property_value_type is string. | direct |
| [property_value_number](property_value_number.md) | 0..1 <br/> [Double](Double.md) | Numeric value when property_value_type is number. | direct |
| [property_value_boolean](property_value_boolean.md) | 0..1 <br/> [Boolean](Boolean.md) | Boolean value when property_value_type is boolean. | direct |
| [property_unit](property_unit.md) | 0..1 <br/> [String](String.md) | Normalized unit where applicable (for example min, dB, W/m2K). | direct |
| [property_unit_uri](property_unit_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT. | direct |
| [source_pset](source_pset.md) | 0..1 <br/> [String](String.md) | Original IFC PropertySet name (for example Pset_WallCommon). | direct |
| [source_property](source_property.md) | 0..1 <br/> [String](String.md) | Original property name inside the source PropertySet (for example FireRating). | direct |
| [source_value_raw](source_value_raw.md) | 0..1 <br/> [String](String.md) | Raw source value before normalization. | direct |
| [mapping_version](mapping_version.md) | 0..1 <br/> [String](String.md) | Mapping specification version used to derive the normalized property. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Entity](Entity.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Agent](Agent.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Person](Person.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Company](Company.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Message](Message.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [PhysicalElement](PhysicalElement.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Separator](Separator.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [SeparatorWall](SeparatorWall.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [SeparatorSlab](SeparatorSlab.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [ConnectionPhysical](ConnectionPhysical.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Boundary](Boundary.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Equipment](Equipment.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [VirtualEntity](VirtualEntity.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [SpatialContext](SpatialContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [ProjectContext](ProjectContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [PerimeterContext](PerimeterContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [LegalSiteContext](LegalSiteContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [BuildingContext](BuildingContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [CivilStructureContext](CivilStructureContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [LevelContext](LevelContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [ZoneContext](ZoneContext.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Space](Space.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [System](System.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [TimeRecord](TimeRecord.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [CostRecord](CostRecord.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |
| [Material](Material.md) | [performance_properties](performance_properties.md) | range | [PerformanceProperty](PerformanceProperty.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:PerformanceProperty |
| native | pbs:PerformanceProperty |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PerformanceProperty
description: 'Normalized performance/property record derived from raw IFC PropertySet
  values with source traceability and strong typing through domain-specific subclasses.

  '
from_schema: https://schema.pragmaticbim.ch
abstract: true
slots:
- property_key
- property_value_type
- property_value_string
- property_value_number
- property_value_boolean
- property_unit
- property_unit_uri
- source_pset
- source_property
- source_value_raw
- mapping_version
class_uri: pbs:PerformanceProperty

```
</details>

### Induced

<details>
```yaml
name: PerformanceProperty
description: 'Normalized performance/property record derived from raw IFC PropertySet
  values with source traceability and strong typing through domain-specific subclasses.

  '
from_schema: https://schema.pragmaticbim.ch
abstract: true
attributes:
  property_key:
    name: property_key
    description: Canonical key inside the domain; constrained via subclass slot_usage
      to a domain-specific enum.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: string
    required: true
  property_value_type:
    name: property_value_type
    description: Value type discriminator for normalized storage (for example string,
      number, boolean).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: PerformancePropertyValueType
    required: true
  property_value_string:
    name: property_value_string
    description: String value when property_value_type is string.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: string
  property_value_number:
    name: property_value_number
    description: Numeric value when property_value_type is number.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: double
  property_value_boolean:
    name: property_value_boolean
    description: Boolean value when property_value_type is boolean.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: boolean
  property_unit:
    name: property_unit
    description: Normalized unit where applicable (for example min, dB, W/m2K).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: string
  property_unit_uri:
    name: property_unit_uri
    description: Optional URI that identifies the normalized property unit in an external
      vocabulary such as QUDT.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: uriorcurie
  source_pset:
    name: source_pset
    description: Original IFC PropertySet name (for example Pset_WallCommon).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    - PropertyChange
    range: string
  source_property:
    name: source_property
    description: Original property name inside the source PropertySet (for example
      FireRating).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    - PropertyChange
    range: string
  source_value_raw:
    name: source_value_raw
    description: Raw source value before normalization.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: string
  mapping_version:
    name: mapping_version
    description: Mapping specification version used to derive the normalized property.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: PerformanceProperty
    domain_of:
    - PerformanceProperty
    range: string
class_uri: pbs:PerformanceProperty

```
</details></div>
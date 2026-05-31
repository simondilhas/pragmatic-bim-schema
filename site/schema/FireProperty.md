---
search:
  boost: 10.0
---

# Class: FireProperty 


_Normalized fire-related property._



<div data-search-exclude markdown="1">



URI: [pbs:FireProperty](https://schema.pragmaticbim.ch/FireProperty)





```mermaid
 classDiagram
    class FireProperty
    click FireProperty href "./FireProperty.html"
      PerformanceProperty <|-- FireProperty
        click PerformanceProperty href "./PerformanceProperty.html"
      FireProperty : mapping_version
      FireProperty : property_key
        FireProperty --> "1" FirePropertyKey : property_key
        click FirePropertyKey href "./FirePropertyKey.html"
      FireProperty : property_unit
      FireProperty : property_unit_uri
      FireProperty : property_value_boolean
      FireProperty : property_value_number
      FireProperty : property_value_string
      FireProperty : property_value_type
        FireProperty --> "1" PerformancePropertyValueType : property_value_type
        click PerformancePropertyValueType href "./PerformancePropertyValueType.html"
      FireProperty : source_property
      FireProperty : source_pset
      FireProperty : source_value_raw
```





## Inheritance
* [PerformanceProperty](PerformanceProperty.md)
    * **FireProperty**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:FireProperty](https://schema.pragmaticbim.ch/FireProperty) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [property_key](property_key.md) | 1 <br/> [FirePropertyKey](FirePropertyKey.md) | Canonical key inside the domain; constrained via subclass slot_usage to a domain-specific enum. | [PerformanceProperty](PerformanceProperty.md) |
| [property_value_type](property_value_type.md) | 1 <br/> [PerformancePropertyValueType](PerformancePropertyValueType.md) | Value type discriminator for normalized storage (for example string, number, boolean). | [PerformanceProperty](PerformanceProperty.md) |
| [property_value_string](property_value_string.md) | 0..1 <br/> [String](String.md) | String value when property_value_type is string. | [PerformanceProperty](PerformanceProperty.md) |
| [property_value_number](property_value_number.md) | 0..1 <br/> [Double](Double.md) | Numeric value when property_value_type is number. | [PerformanceProperty](PerformanceProperty.md) |
| [property_value_boolean](property_value_boolean.md) | 0..1 <br/> [Boolean](Boolean.md) | Boolean value when property_value_type is boolean. | [PerformanceProperty](PerformanceProperty.md) |
| [property_unit](property_unit.md) | 0..1 <br/> [String](String.md) | Normalized unit where applicable (for example min, dB, W/m2K). | [PerformanceProperty](PerformanceProperty.md) |
| [property_unit_uri](property_unit_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Optional URI that identifies the normalized property unit in an external vocabulary such as QUDT. | [PerformanceProperty](PerformanceProperty.md) |
| [source_pset](source_pset.md) | 0..1 <br/> [String](String.md) | Original IFC PropertySet name (for example Pset_WallCommon). | [PerformanceProperty](PerformanceProperty.md) |
| [source_property](source_property.md) | 0..1 <br/> [String](String.md) | Original property name inside the source PropertySet (for example FireRating). | [PerformanceProperty](PerformanceProperty.md) |
| [source_value_raw](source_value_raw.md) | 0..1 <br/> [String](String.md) | Raw source value before normalization. | [PerformanceProperty](PerformanceProperty.md) |
| [mapping_version](mapping_version.md) | 0..1 <br/> [String](String.md) | Mapping specification version used to derive the normalized property. | [PerformanceProperty](PerformanceProperty.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:FireProperty |
| native | pbs:FireProperty |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FireProperty
description: Normalized fire-related property.
from_schema: https://schema.pragmaticbim.ch
is_a: PerformanceProperty
slot_usage:
  property_key:
    name: property_key
    range: FirePropertyKey
class_uri: pbs:FireProperty

```
</details>

### Induced

<details>
```yaml
name: FireProperty
description: Normalized fire-related property.
from_schema: https://schema.pragmaticbim.ch
is_a: PerformanceProperty
slot_usage:
  property_key:
    name: property_key
    range: FirePropertyKey
attributes:
  property_key:
    name: property_key
    description: Canonical key inside the domain; constrained via subclass slot_usage
      to a domain-specific enum.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: FirePropertyKey
    required: true
  property_value_type:
    name: property_value_type
    description: Value type discriminator for normalized storage (for example string,
      number, boolean).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: PerformancePropertyValueType
    required: true
  property_value_string:
    name: property_value_string
    description: String value when property_value_type is string.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: string
  property_value_number:
    name: property_value_number
    description: Numeric value when property_value_type is number.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: double
  property_value_boolean:
    name: property_value_boolean
    description: Boolean value when property_value_type is boolean.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: boolean
  property_unit:
    name: property_unit
    description: Normalized unit where applicable (for example min, dB, W/m2K).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: string
  property_unit_uri:
    name: property_unit_uri
    description: Optional URI that identifies the normalized property unit in an external
      vocabulary such as QUDT.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: uriorcurie
  source_pset:
    name: source_pset
    description: Original IFC PropertySet name (for example Pset_WallCommon).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
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
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    - PropertyChange
    range: string
  source_value_raw:
    name: source_value_raw
    description: Raw source value before normalization.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: string
  mapping_version:
    name: mapping_version
    description: Mapping specification version used to derive the normalized property.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: FireProperty
    domain_of:
    - PerformanceProperty
    range: string
class_uri: pbs:FireProperty

```
</details></div>
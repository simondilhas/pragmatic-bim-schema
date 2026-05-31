---
search:
  boost: 10.0
---

# Class: LocalizedText 


_Localized text value for a specific language tag._



<div data-search-exclude markdown="1">



URI: [pbs:LocalizedText](https://schema.pragmaticbim.ch/LocalizedText)





```mermaid
 classDiagram
    class LocalizedText
    click LocalizedText href "./LocalizedText.html"
      LocalizedText : language_tag
      LocalizedText : text_value
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pbs:LocalizedText](https://schema.pragmaticbim.ch/LocalizedText) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [language_tag](language_tag.md) | 1 <br/> [String](String.md) | IETF BCP 47 language tag (for example en, de, pt-BR). | direct |
| [text_value](text_value.md) | 1 <br/> [String](String.md) | Localized text value. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Entity](Entity.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Entity](Entity.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Agent](Agent.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Agent](Agent.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Person](Person.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Person](Person.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Company](Company.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Company](Company.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Message](Message.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Message](Message.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [PhysicalElement](PhysicalElement.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [PhysicalElement](PhysicalElement.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Separator](Separator.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Separator](Separator.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [SeparatorWall](SeparatorWall.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [SeparatorWall](SeparatorWall.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [SeparatorSlab](SeparatorSlab.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [SeparatorSlab](SeparatorSlab.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [ConnectionPhysical](ConnectionPhysical.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [ConnectionPhysical](ConnectionPhysical.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Boundary](Boundary.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Boundary](Boundary.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Equipment](Equipment.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Equipment](Equipment.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [VirtualEntity](VirtualEntity.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [VirtualEntity](VirtualEntity.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [SpatialContext](SpatialContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [SpatialContext](SpatialContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [ProjectContext](ProjectContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [ProjectContext](ProjectContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [PerimeterContext](PerimeterContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [PerimeterContext](PerimeterContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [LegalSiteContext](LegalSiteContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [LegalSiteContext](LegalSiteContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [BuiltAssetContext](BuiltAssetContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [BuildingContext](BuildingContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [BuildingContext](BuildingContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [CivilStructureContext](CivilStructureContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [CivilStructureContext](CivilStructureContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [LevelContext](LevelContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [LevelContext](LevelContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [ZoneContext](ZoneContext.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [ZoneContext](ZoneContext.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Space](Space.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Space](Space.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [System](System.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [System](System.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [ConnectionVirtual](ConnectionVirtual.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [AbstractTimeRecord](AbstractTimeRecord.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [AbstractTimeRecord](AbstractTimeRecord.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [TimeItem](TimeItem.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [TimeItem](TimeItem.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Milestone](Milestone.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Milestone](Milestone.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [TimePlan](TimePlan.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [TimePlan](TimePlan.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [TimeDependency](TimeDependency.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [TimeDependency](TimeDependency.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [AbstractCostRecord](AbstractCostRecord.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [CostItem](CostItem.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [CostItem](CostItem.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [CostAssembly](CostAssembly.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [CostAssembly](CostAssembly.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |
| [Material](Material.md) | [localized_names](localized_names.md) | range | [LocalizedText](LocalizedText.md) |
| [Material](Material.md) | [localized_descriptions](localized_descriptions.md) | range | [LocalizedText](LocalizedText.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:LocalizedText |
| native | pbs:LocalizedText |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocalizedText
description: Localized text value for a specific language tag.
from_schema: https://schema.pragmaticbim.ch
slots:
- language_tag
- text_value
class_uri: pbs:LocalizedText

```
</details>

### Induced

<details>
```yaml
name: LocalizedText
description: Localized text value for a specific language tag.
from_schema: https://schema.pragmaticbim.ch
attributes:
  language_tag:
    name: language_tag
    description: IETF BCP 47 language tag (for example en, de, pt-BR).
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LocalizedText
    domain_of:
    - LocalizedText
    range: string
    required: true
  text_value:
    name: text_value
    description: Localized text value.
    from_schema: https://schema.pragmaticbim.ch
    rank: 1000
    owner: LocalizedText
    domain_of:
    - LocalizedText
    range: string
    required: true
class_uri: pbs:LocalizedText

```
</details></div>
---
search:
  boost: 2.0
---


# Enum: ContextType 



<div data-search-exclude markdown="1">

URI: [pbs:ContextType](https://schema.pragmaticbim.ch/ContextType)

**Enum URI:** [pbs:ContextType](https://schema.pragmaticbim.ch/ContextType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| project | ifcowl:IfcProject |  |
| perimeter | ifcowl:IfcSite |  |
| legal_site | pbs:LegalSiteContext |  |
| building | bot:Building |  |
| civil_structure | ifcowl:IfcCivilElement |  |
| level | bot:Storey |  |
| zone | bot:Zone |  |




## Slots

| Name | Description |
| ---  | --- |
| [context_type](context_type.md) | Classification of context entity (project, perimeter, legal_site, building, civil_structure, level, zone). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: ContextType
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:ContextType
permissible_values:
  project:
    text: project
    meaning: ifcowl:IfcProject
  perimeter:
    text: perimeter
    meaning: ifcowl:IfcSite
    exact_mappings:
    - bot:Site
  legal_site:
    text: legal_site
    meaning: pbs:LegalSiteContext
  building:
    text: building
    meaning: bot:Building
  civil_structure:
    text: civil_structure
    meaning: ifcowl:IfcCivilElement
  level:
    text: level
    meaning: bot:Storey
  zone:
    text: zone
    meaning: bot:Zone

```
</details>

</div>
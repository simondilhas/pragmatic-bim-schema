---
search:
  boost: 2.0
---


# Enum: PerformancePropertyValueType 




_Type discriminator for normalized performance property values._



<div data-search-exclude markdown="1">

URI: [pbs:PerformancePropertyValueType](https://schema.pragmaticbim.ch/PerformancePropertyValueType)

**Enum URI:** [pbs:PerformancePropertyValueType](https://schema.pragmaticbim.ch/PerformancePropertyValueType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| string | pbs:performance_property_value_type_string |  |
| number | pbs:performance_property_value_type_number |  |
| boolean | pbs:performance_property_value_type_boolean |  |




## Slots

| Name | Description |
| ---  | --- |
| [property_value_type](property_value_type.md) | Value type discriminator for normalized storage (for example string, number, boolean). |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: PerformancePropertyValueType
description: Type discriminator for normalized performance property values.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:PerformancePropertyValueType
permissible_values:
  string:
    text: string
    meaning: pbs:performance_property_value_type_string
  number:
    text: number
    meaning: pbs:performance_property_value_type_number
  boolean:
    text: boolean
    meaning: pbs:performance_property_value_type_boolean

```
</details>

</div>
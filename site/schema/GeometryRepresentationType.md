---
search:
  boost: 2.0
---


# Enum: GeometryRepresentationType 




_Classification of geometric representation dimension/style._



<div data-search-exclude markdown="1">

URI: [pbs:GeometryRepresentationType](https://schema.pragmaticbim.ch/GeometryRepresentationType)

**Enum URI:** [pbs:GeometryRepresentationType](https://schema.pragmaticbim.ch/GeometryRepresentationType)


## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| axis | None | Linear axis/centerline representation. |
| body_3d | None | 3D volumetric/body representation. |
| footprint_2d | None | 2D surface/footprint representation. |
| point | None | Point/dot representation. |




## Slots

| Name | Description |
| ---  | --- |
| [geometry_representation](geometry_representation.md) | Representation kind/dimension (for example body_3d, footprint_2d, point), independent of file format. |
| [affected_geometry_role](affected_geometry_role.md) | Geometry role affected when change_type is geometry_change. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch






## LinkML Source

<details>
```yaml
name: GeometryRepresentationType
description: Classification of geometric representation dimension/style.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
enum_uri: pbs:GeometryRepresentationType
permissible_values:
  axis:
    text: axis
    description: Linear axis/centerline representation.
  body_3d:
    text: body_3d
    description: 3D volumetric/body representation.
  footprint_2d:
    text: footprint_2d
    description: 2D surface/footprint representation.
  point:
    text: point
    description: Point/dot representation.

```
</details>

</div>
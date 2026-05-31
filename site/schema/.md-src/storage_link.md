---
search:
  boost: 5.0
---

# Slot: storage_link 


_URI/URL/path to the stored document location._



<div data-search-exclude markdown="1">



URI: [pbs:storage_link](https://schema.pragmaticbim.ch/storage_link)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Reference to an external document stored in a file system, DMS, object storage, or URL. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Document](Document.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:storage_link |
| native | pbs:storage_link |




## LinkML Source

<details>
```yaml
name: storage_link
description: URI/URL/path to the stored document location.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Document
range: uriorcurie
required: true

```
</details></div>
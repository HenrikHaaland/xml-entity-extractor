# XML Entity Extractor

**XML Entity Extractor** is a lightweight utility designed to extract specific entities from XML files based on their ID. It enables you to parse XML data and retrieve elements by matching the desired `id` attributes.

## Features
- Extracts entities by ID from XML files
- Supports large XML files with efficient parsing
- Easy to integrate into scripts or larger projects
- two diffrent ways to search for id which is "id" and "about"

## Usage
1. Clone the repository
2. Pass your XML file and the target `id` to extract the desired entity

## Example
```python
python xee.py cim-about.xml urn:uuid:4a

```
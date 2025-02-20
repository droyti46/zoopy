![logo](img/logo.png)
# ZooPy: A Python Library for Animal Data Analysis

## Overview
**ZooPy** is a Python library designed for analyzing and processing biological data related to animals. It provides tools for working with datasets, performing image recognition etc.
![turtle](img/turtle.png)           

## Installation
To install ZooPy, run:

```bash
pip install zoopy
```

## Usage
Getting started:

```python
from zoopy import animal

dog = animal.Animal('dog')
print(dog)
```

ZooPy supports multiple languages and synonyms (based on NLP):

```python
for animal_name in ['собака', 'пёс', 'chien', 'hund']:
    dog = animal.Animal(animal_name)
    print(dog.name_en)
```

See more [examples](examples/).

## Dependencies
- `pandas`

## License
This project is licensed under the MIT License.
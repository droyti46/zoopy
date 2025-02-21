<div align="center"><img src="img/logo.png"></div>

<h1 align="center"> ZooPy: A Python Library for Animal Data Analysis</h1>

<p align="center">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
    <img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/></a>
</p>

## Overview
**ZooPy** is a Python library designed for analyzing and processing biological data related to animals. It provides tools for working with datasets, performing image recognition etc.
<div align="center"><img src="img/turtle.png"></div>

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
- `pandas==2.2.3`

## License
This project is licensed under the MIT License.
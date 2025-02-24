<div align="center"><img src="img/logo.png"></div>

<h1 align="center"> ZooPy: A Python Library for Animal Data Analysis</h1>

<p align="center">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/></a>
    <img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/></a>
</p>

## Overview
**ZooPy** is a simple Python library with a concise API designed for analyzing and processing biological data related to animals. It provides tools for working with datasets, performing image recognition etc.
<div align="center"><img src="img/turtle.png"></div>

## Data
The data was collected from [Wikipedia](https://www.wikipedia.org/) and contains the languages:
- 🇷🇺 Russian

## Library Structure
<div align="center"><img src="img/structure.png" width=550px></div>

## Installation
To install ZooPy, run:

```bash
pip install zoopy
```

Also install the NLP model for Spacy

- Russian (40 MB):
```python -m spacy download ru_core_news_md```

## Usage
Getting started:

```python
from zoopy import animal

cat = animal.Animal('кошка', 'ru')
cat.display()
```

<div align="center"><img src="img/cat-display.png" width=500px></div>


ZooPy has several pre-trained models

```python
import cv2
from zoopy import models

model = models.ImageClassification()

img = cv2.imread('turtle.jpeg')
model.predict(img)
```

For more information see [docs](docs/).

## Dependencies
- `pandas==2.2.3`

## Contact
Contact me by [Mail](nikitabakutov2008@gmail.com) or [Telegram](https://t.me/droyti).

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
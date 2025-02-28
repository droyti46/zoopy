<div align="center"><img src="img/logo.png"></div>

<h1 align="center"> ZooPy: A Python Library for Animal Data Analysis</h1>

<p align="center">
    <img alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/>
    <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
    <img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
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

## Usage
Getting started:

```python
from zoopy import animal

cat = animal.Animal('кошка', 'ru')
cat.display()
```

<div align="center"><img src="img/cat-display.png" width=500px></div>

\
ZooPy has several pre-trained models

```python
import cv2
from zoopy import models

model = models.ImageClassification()

img = cv2.imread('turtle.jpeg')
model.predict(img)
```

Create different graphics

```python
from zoopy import animal, viz

turtle = animal.Animal('черепаха', 'ru')
viz.plot_classification(turtle)
```

<div align="center"><img src="img/classification.png" width=500px></div>

For more information see [docs](docs/).

## Dependencies
- `pandas==2.2.3`
- `matplotlib==3.9.0`

## Contact
Contact me by [Mail](nikitabakutov2008@gmail.com) or [Telegram](https://t.me/droyti).

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing
See the [CONTRIBUTING](./CONTRIBUTING.md) file if you want to help the project.
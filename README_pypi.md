<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/logo.png?raw=true"></div>

<h1 align="center"> ZooPy: A Python Library for Animal Data Analysis</h1>

<p align="center">
    <img alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/>
    <img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
    <img alt="torch" src="https://img.shields.io/badge/Torch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
</p>

## Overview
**ZooPy** is a simple Python library with a concise API designed for analyzing and processing biological data related to animals. It provides tools for working with datasets, performing image recognition etc.
<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/turtle.png?raw=true"></div>

## Data
The data was collected from [Wikipedia](https://www.wikipedia.org/) and contains the languages:
- 🇷🇺 Russian

## Library Structure
<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/structure.png?raw=true" width=550px></div>

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

<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/cat-display.png?raw=true" width=500px></div>

\
ZooPy has interfaces for several pre-trained models, for example, ImageNet

```python
import cv2

img = cv2.imread('img/duck.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow(img)
```

<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/duck.jpg?raw=true" width=500px></div>

```python
from zoopy import models

model = models.ImageClassification()
print(model.predict(img))
```

```Output: albatross```

Create different graphics

```python
from zoopy import animal, viz

turtle = animal.Animal('черепаха', 'ru')
viz.plot_classification(turtle)
```

<div align="center"><img src="https://github.com/droyti46/zoopy/blob/main/img/classification.png?raw=true" width=500px></div>

## Contact
Contact me by [Mail](mailto:nikitabakutov2008@gmail.com) or [Telegram](https://t.me/droyti).
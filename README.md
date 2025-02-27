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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animal Information</title>
    <style>
        .container {
            display: flex;
            justify-content: space-between;
        }
        .left, .right {
            width: 48%;
        }
    </style>
</head>
<body>
    <h1>Кошка</h1>
    <hr>
    <h2>Scientific classification</h2>
    <div class="container">
        <div class="left">
            <b>domain</b>: Эукариоты<br>
            <b>kingdom</b>: Животные<br>
            <b>subkingdom</b>: Эуметазои<br>
            <b>phylum</b>: Хордовые<br>
            <b>subphylum</b>: Позвоночные<br>
            <b>infraphylum</b>: Челюстноротые<br>
            <b>superclass</b>: Четвероногие<br>
            <b>class</b>: Млекопитающие<br>
            <b>order</b>: Хищные<br>
            <b>suborder</b>: Кошкообразные<br>
            <b>superfamily</b>: Feloidea<br>
            <b>family</b>: Кошачьи<br>
            <b>subfamily</b>: Малые кошки<br>
            <b>genus</b>: Кошки<br>
            <b>species</b>: Кошка<br>
        </div>
        <div class="right">
            <h2>ID</h2>
            <b>FW</b>: 231413
        </div>
    </div>
</body>
</html>

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
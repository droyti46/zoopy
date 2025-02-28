<div align="center"><img src="img/logo.png"></div>

<h1 align="center"> ZooPy: A Python Library for Animal Data Analysis</h1>

<p align="center">
    <img alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/>
    <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
    <img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
    <img alt="torch" src="https://img.shields.io/badge/Torch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
</p>

## Overview
**ZooPy** is a simple Python library with a concise API designed for analyzing and processing biological data related to animals. It provides tools for working with datasets, performing image recognition etc.
<div align="center"><img src="img/turtle.png" style="border-radius: 20px"></div>

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

<div align="center"><img src="img/cat-display.png" width=500px style="border-radius: 20px"></div>

\
ZooPy has interfaces for several pre-trained models, for example, ImageNet

```python
import cv2

img = cv2.imread('img/duck.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow(img)
```

<div align="center"><img src="img/duck.jpg" width=500px style="border-radius: 20px"></div>

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

<div align="center"><img src="img/classification.png" width=500px style="border-radius: 20px"></div>

For more information see [docs](docs/).

## Dependencies
- `pandas>=2.2.0`
- `matplotlib>=3.9.0`
- `tqdm>=4.66.0`
- `Levenshtein>=0.26.0`
- `numpy>=1.26.4`
- `torch>=2.4.0`
- `torchvision>=0.19.0`

## Contact
Contact me by [Mail](mailto:nikitabakutov2008@gmail.com) or [Telegram](https://t.me/droyti).

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing
See the [CONTRIBUTING](./CONTRIBUTING.md) file if you want to help the project.
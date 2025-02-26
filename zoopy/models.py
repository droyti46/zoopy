'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains interfaces of pre-trained models for predictions
'''

import numpy as np

class ImageClassification:

    '''
    A class for representing a photo classification model

    Examples:
        >>> from zoopy import models

        >>> model = models.ImageClassification()
        >>> model.predict('turtle.jpeg')
    '''

    def __init__(self, model_file: str | None = None):
        pass

    def predict(self, img: np.ndarray | str) -> None:
        pass

    def finetune(self,
                 x: list[np.ndarray] | np.ndarray,
                 y: list[str] | np.ndarray) -> None:
        pass

    def save(self, file: str) -> None:
        pass
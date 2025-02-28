'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains machine learning methods for analytics

classes:
    ImageClassification
'''

import numpy as np
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights

RESNET_CLASSES_LABELS_FILE = 'zoopy/datasets/imagenet_classes.txt'

class ImageClassification:

    '''
    Represents an image classification model

    Methods:
        predict(...) -> str: predicts animal in image

    Examples:
        >>> import cv2
        >>> from zoopy import models

        >>> img = cv2.imread('img.jpg')
        >>> img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        >>> model = models.ImageClassification()
        >>> model.predict(img)
    '''

    def __init__(self):
        # Load pre-trained model ResNet50
        self.__model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
        self.__model.eval()

        # Load class labels ImageNet
        self.__labels = self._load_imagenet_labels()

        # Transformations for the input image
        self.__transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def _load_imagenet_labels(self) -> list[str]:
        # Load class labels ImageNet
        with open(RESNET_CLASSES_LABELS_FILE) as f:
            labels = [line.split(', ')[1].strip()
                      for line in f.readlines()]
        
        return labels

    def predict(self, img: np.ndarray) -> str:

        '''
        Predicts animal in image

        Parameters:
            img (np.ndarray): img in RGB format

        Return:
            animal_class (str): name of animal in image
        '''

        # Convert image for model
        img_tensor = self.__transform(img).unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            outputs = self.__model(img_tensor)
            _, predicted = torch.max(outputs, 1)

        return self.__labels[predicted.item()]
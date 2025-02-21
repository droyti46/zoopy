import pandas as pd

class Animal:

    '''
    A class for representing animals

    Attributes:
        animal_name (str): name of the animal

    Methods:
        to_series() -> pd.Series:
            Converting features to the pd.Series type
        
        to_dict() -> dict:
            Converting features to the dict type

    Examples:
        >>> from zoopy.animal import Animal
        >>> animal = Animal('cat')
        >>> print(animal.class)
    '''

    def __init__(self, animal_name: str) -> None:
        pass

    def __str__(self) -> str:
        pass

    def plot_classification():
        pass

    def to_series(self) -> pd.Series:
        pass

    def to_dict(self) -> dict:
        pass
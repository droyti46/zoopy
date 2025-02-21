import pandas as pd

from zoopy.data import file_loader

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

    def __init__(self, animal_name: str, lang: str) -> None:
        self.__series: pd.Series = file_loader.get_animal(animal_name, lang)

    def __str__(self) -> str:
        return str(self.__series)

    def to_series(self) -> pd.Series:
        return self.__series

    def to_dict(self) -> dict:
        return self.__series.to_dict()
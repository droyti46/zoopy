'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains instruments for work with data

functions:
    sort_dataframe_by_levenshtein(...) -> pandas.DataFrame

classes:
    DataLoader
'''

import importlib.resources

import pandas as pd
import Levenshtein

from zoopy import exceptions

ANIMALS_DATASET_NAME = 'animals_{}.csv'
SUPPORTED_LANGUAGES = ['ru']
SIMILARITY_COLUMN = 'similarity'

def sort_dataframe_by_levenshtein(
        data: pd.DataFrame,
        column: str,
        string: str,
    ) -> pd.DataFrame:

    '''
    Creates in original dataset column "similarity" and sorts dataset
    by Levenshtein distance with string

    Parameters:
        data (pandas.DataFrame): original dataset
        column (str): column that will be used for Levenshtein distance
        string (str)
    '''

    data[SIMILARITY_COLUMN] = data[column].apply(lambda s: Levenshtein.ratio(s, string))
    return data.sort_values(SIMILARITY_COLUMN, ascending=False)

class _SingletonWrapper:

    ''''
    Wrapper for pattern "Singleton"
    '''

    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        '''Returns a single instance of the class'''
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)

        return self._instance
    
def singleton(cls):
    '''
    Decorator for Singleton class
    '''
    return _SingletonWrapper(cls)

@singleton
class DataLoader:

    '''
    Represents class for working with data
    When called in any part of the program,
    it returns only one instance due to the pattern "Singleton"

    Methods:
        load_animals_dataset(lang: str) -> pandas.DataFrame:
            Returns text dataset in pandas.Dataframe type

        get_animal(animal_name: str, lang: str) -> pandas.Series:
            Returns animal from dataset.
            Uses the Levenshtein distance

    Examples:
        >>> from zoopy import data
        >>> data_loader = data.DataLoader()

        >>> dataset = data_loader.load_animals_dataset('ru')
        >>> dataset.head()

        >>> dog = data_loader.get_animal('dog', 'ru')
    '''

    def __init__(self):
        self.datasets: dict[str: pd.DataFrame] = {lang: None for lang in SUPPORTED_LANGUAGES}
    
    def __check_and_load_dataset(self, lang: str) -> None:
        if self.datasets[lang] is None:
            self.datasets[lang] = self.load_animals_dataset(lang)

    def load_animals_dataset(self, lang: str = 'ru') -> pd.DataFrame:
        with importlib.resources.files('zoopy.datasets') \
                                .joinpath(ANIMALS_DATASET_NAME.format(lang)) \
                                .open('r', encoding='utf-8') as f:
            return pd.read_csv(f)
    
    def get_all_by(
            self,
            column: str,
            value: str,
            lang: str
        ) -> pd.DataFrame:

        '''
        Returns filtered values from dataset

        Parameters:
            column: column for search
            value: value for filter
            lang: language of returned data
        '''

        self.__check_and_load_dataset(lang)

        data: pd.DataFrame = self.datasets[lang]
        found = data[data[column].str.lower() == value.lower().strip()]

        return found

    def get_animal(
            self,
            animal_name: str,
            lang: str,
            accurate: bool = False
        ) -> pd.Series:

        '''
        Returns animal in pandas.Series from dataset
        Uses the Levenshtein distance

        Parameters:
            animal_name: animal's name (in original language or English)
            lang: language of returned data
        '''

        self.__check_and_load_dataset(lang)
        data: pd.DataFrame = self.datasets[lang]

        if accurate:
            return data[data['name'] == animal_name].iloc[0]

        found = sort_dataframe_by_levenshtein(data, 'name', animal_name)
        
        return found.iloc[0]
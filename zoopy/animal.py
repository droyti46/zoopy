'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains instruments for work with animals

classes:
    Animal
'''

import pandas as pd
from IPython.display import display, HTML

from zoopy import data

PATH_TO_DESCRIPTION_TXT = 'zoopy/templates/description.txt'
PATH_TO_DESCRIPTION_HTML = 'zoopy/templates/description.html'

ID_COLUMNS = ['ITIS', 'NCBI', 'EOL', 'FW']
ADDITIONAL_COLUMNS = ['name', 'name_en', 'similarity']

class Animal:

    '''
    Represents an animal

    Attributes:
        animal_name (str): name of the animal
        lang (str): language in which the name is written

    Methods:
        display() -> None:
            Displays information about the animal in the Jupyter cell
        
        to_series() -> pd.Series:
            Converting features to the pandas.Series type
        
        to_dict() -> dict:
            Converting features to the dict type

    Examples:
        >>> from zoopy.animal import Animal
        >>> animal = Animal('cat')
        >>> print(animal.class_)
    '''

    def __init__(self, animal_name: str, lang: str) -> None:
        self.__data_loader = data.DataLoader()
        self.__series: pd.Series = self.__data_loader.get_animal(animal_name, lang)

        self.classification = self.__series.drop(
            ID_COLUMNS + ADDITIONAL_COLUMNS
        ).dropna().to_dict()

        self.ids = self.__series[ID_COLUMNS].dropna().to_dict()

    def __get_description(self,
                          file_path: str,
                          new_line_tag: str = '\n',
                          bold_tags: tuple[str] = ('', '')) -> str:
        
        '''
        Returns a string for output

        Parameters:
            file_path (str): path to file
            new_line_tag (str), optinonal: tag for new_line (<br> in HTML or \n in String)
            bold_tags (tuple[str]), optional:
                tag for bold words (('<b>', '</b>') in HTML)
        '''

        with open(file_path, 'r') as f:
            description = f.read()
        
        bold_tag1, bold_tag2 = bold_tags

        # Extraction text features
        classification_str = new_line_tag.join(
            f'{bold_tag1}{key}{bold_tag2}: {val}' for key, val in self.classification.items()
        )
        id_str = new_line_tag.join(
            f'{bold_tag1}{key}{bold_tag2}: {val}' for key, val in self.ids.items()
        )

        # Template substitution
        description = description \
                .replace('{ANIMAL_NAME}', self.__series['name']) \
                .replace('{CLASSIFICATION}', classification_str) \
                .replace('{ID}', id_str)
        
        return description

    def __str__(self) -> str:
        description = self.__get_description(PATH_TO_DESCRIPTION_TXT)
        return description
    
    def display(self) -> None:
        '''Display animal in Jupyter cell'''

        description = self.__get_description(
            PATH_TO_DESCRIPTION_HTML,
            '<br>',
            ('<b>', '</b>')
        )
        display(HTML(description))

    def to_series(self) -> pd.Series:
        '''Converting features to pandas.Series type'''
        return self.__series

    def to_dict(self) -> dict:
        '''Converting features to dict type'''
        return self.__series.to_dict()

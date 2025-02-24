import IPython.display
import pandas as pd
from colorama import init, Fore, Back, Style
from IPython.display import display, HTML

from zoopy import data

init()

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
            ['name', 'language', 'ITIS', 'NCBI', 'EOL', 'FW', 'similarity']
        ).dropna().to_dict()

    def __str__(self) -> str:
        return f'''{Back.GREEN}=== {self.__series["name"]} ==={Style.RESET_ALL}

{Back.YELLOW}{Fore.BLACK}# Scientific classification{Style.RESET_ALL}
{"\n".join(f"{Fore.YELLOW}{key}{Style.RESET_ALL}: {value}" for key, value in self.classification.items())}

{Back.YELLOW}{Fore.BLACK}# ID{Style.RESET_ALL}
{"\n".join(f"{Fore.YELLOW}{val}{Style.RESET_ALL}: {self.__series[val]}" for val in ["ITIS", "NCBI", "EOL", "FW"])}
'''
    
    def display(self) -> None:
        with open('zoopy/templates/description.html', 'r') as f:
            description = f.read()

        classification_str = '<br>'.join(
            f'<span style="color: yellow">{key}</span>: {value}' for key, value in self.classification.items()
        )
        id_str = '<br>'.join(
            f'<span style="color: yellow">{val}</span>: {self.__series[val]}' for val in ["ITIS", "NCBI", "EOL", "FW"]
        )

        description = description \
                .replace('{ANIMAL_NAME}', self.__series["name"]) \
                .replace('{CLASSIFICATION}', classification_str) \
                .replace('{ID}', id_str)
        
        display(HTML(description))

    def to_series(self) -> pd.Series:
        return self.__series

    def to_dict(self) -> dict:
        return self.__series.to_dict()

import pandas as pd
import Levenshtein

from zoopy import exceptions

ANIMALS_DATASET_PATH = 'zoopy/datasets/animals_{}.csv'
SUPPORTED_LANGUAGES = ['ru']
SIMILARITY_COLUMN = 'similarity'

def sort_dataframe_by_levenshtein(
        data: pd.DataFrame,
        column: str,
        string: str,
    ) -> pd.DataFrame:

    data[SIMILARITY_COLUMN] = data[column].apply(lambda s: Levenshtein.ratio(s, string))
    return data.sort_values(SIMILARITY_COLUMN, ascending=False)

class DataLoader:

    '''
    Represents class for working with data
    '''

    def __init__(self):
        self.datasets: dict[str: pd.DataFrame] = {lang: None for lang in SUPPORTED_LANGUAGES}

    def load_animals_dataset(self, lang: str = 'ru') -> pd.DataFrame:
        return pd.read_csv(ANIMALS_DATASET_PATH.format(lang))

    def get_animal(
            self,
            animal_name: str,
            lang: str,
        ) -> pd.Series:

        if not self.datasets[lang]:
            self.datasets[lang] = self.load_animals_dataset(lang)

        data: pd.DataFrame = self.datasets[lang]
        found = sort_dataframe_by_levenshtein(data, 'name', animal_name)
        
        return found.iloc[0]
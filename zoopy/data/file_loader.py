import pandas as pd
import spacy

ANIMALS_DATASET_PATH = 'zoopy/data/datasets/animals_{}.csv'
SUPPORTED_LANGUAGES = ['ru']
NLP_MODELS = {
    'ru': 'ru_core_news_md'
}
SIMILARITY_COLUMN = 'similarity'

def load_animals_dataset(lang: str = 'ru') -> pd.DataFrame:
    return pd.read_csv(ANIMALS_DATASET_PATH.format(lang))

ANIMALS_DATASETS = {
    lang: load_animals_dataset(lang)
    for lang in SUPPORTED_LANGUAGES
}

def sort_dataframe_by_similarity(
        data: pd.DataFrame,
        column: str,
        string: str,
        lang: str
    ) -> pd.DataFrame:

    nlp = spacy.load(NLP_MODELS[lang])
    doc = nlp(string)
    data[SIMILARITY_COLUMN] = data[column].apply(lambda s: nlp(s).similarity(doc))

    return data.sort_values(SIMILARITY_COLUMN, ascending=False)

def get_animal(animal_name: str, lang: str) -> pd.Series:
    data = ANIMALS_DATASETS[lang]
    found = data[data['name'].str.contains(animal_name, case=False, na=False)]
    found = sort_dataframe_by_similarity(found, 'name', animal_name, lang)
    
    return found.iloc[0]
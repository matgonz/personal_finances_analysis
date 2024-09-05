import pandas as pd
import re
from src import utils

def credit_card_pipeline(path: str) -> pd.DataFrame:

    from_to_category = {'payment': 'fatura'}

    category_from_title = {
        'Buser':'transporte', 'Mp *Buser':'transporte',
        'Assai Atacadista':'supermercado', 'Gympass Gympassbr':'saúde',
        'Wellhub Gympass Br Gym':'saúde', 'Openai *Chatgpt Subscr':'serviços'}
    
    installment_pattern = r"\b(?:0|[1-9]|[1-9][0-9]|100)/(?:0|[1-9]|[1-9][0-9]|100)\b"

    # load data
    dataframe = utils.read_files(path.format('/credit_card'))

    # format date
    dataframe['date'] = pd.to_datetime(dataframe['date'], format='%Y-%m-%d')

    # remove installment number of title
    dataframe['fmt_title'] = dataframe['title'].apply(lambda x: re.sub(installment_pattern, "", x).strip())

    # flag rows where the title contains installment number
    dataframe['is_installment'] = dataframe['title'].str.contains(installment_pattern)

    # create new category column
    dataframe['new_category'] = dataframe['category'].copy()
    dataframe['new_category'] = dataframe['new_category'].replace(from_to_category)
    for title, category in category_from_title.items():
        dataframe.loc[dataframe['title'] == title, 'new_category'] = category


    return dataframe
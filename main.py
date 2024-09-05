from src import pipeline

if __name__ == '__main__':

    data_path = 'D:/Workspace/data/personal_finances/nubank/{0}'

    # Process Credit Card Data
    df_credit_card = pipeline.credit_card_pipeline(data_path)
    df_credit_card.to_csv(data_path.format('/credit_card_database.csv'), index=False, encoding='utf-8')
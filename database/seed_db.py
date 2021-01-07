import logging
from logging.config import dictConfig

import pandas as pd
from config import LOGGING_CONFIG
from instance.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine

dictConfig(LOGGING_CONFIG)

TABLE_NAME = "chinese_word"
CSV_PATH = './data/words.csv'

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    # TODO: assert db exists

    df = pd.read_csv(CSV_PATH, header=None)
    df = df.rename(columns={0: 'word'})

    logging.info('Reading %s in df', CSV_PATH)
    logging.info(f'df shape: {df.shape}')
    logging.info(df.head())

    logging.info('writing in %s', TABLE_NAME)
    df.to_sql(TABLE_NAME, engine, if_exists='append', index=False)
    logging.info('write completed')

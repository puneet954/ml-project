import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import pymysql

from dotenv import load_dotenv

load_dotenv() #load the environment variable
host=os.getenv("host")
user=os.getenv("user")
passward=os.getenv("passward")
db=os.getenv('db')


def read_sql_data():
    logging.info("reading sql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            passward=passward,
            db=db
        )
        logging.info("connection stablished",mydb)
        df=pd.read_sql_query('select * from students',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)

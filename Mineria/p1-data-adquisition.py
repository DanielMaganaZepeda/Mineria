import pandas as pd
from tabulate import tabulate
from kaggle.api.kaggle_api_extended import KaggleApi
#import os

api = KaggleApi()
api.authenticate()
#api.dataset_download_file('cyaris/2016-mlb-season', file_name='baseball_reference_2016_clean.csv')
#os.rename('baseball_reference_2016_clean.csv', 'MLB 2016 Season.csv')

df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')
print(df)

input()
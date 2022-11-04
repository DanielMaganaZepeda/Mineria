import pandas as pd
from tabulate import tabulate
import numpy as np

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, tablefmt='github', showindex=False, numalign='center', stralign='left',headers="keys"))

df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

#Quitamos columnas que no nos sirvan 
df = df.drop(columns=['Unnamed: 0','field_type','game_type','start_time','day_of_week','temperature','wind_speed','wind_direction','sky','total_runs','game_hours_dec','season',
'home_team_win','home_team_loss','home_team_outcome','away_team_errors','away_team_hits','home_team_errors','home_team_hits'])

#Cambiamos el formato de los nombres de los equipos de {City, Team} => {City}
df.loc[df['away_team']=="Boston Red Sox",'away_team']='Red-Sox'
df.loc[df['away_team']=="Boston Red Sox",'home_team']='Red-Sox'
df.loc[df['away_team']=="Chicago White Sox",'away_team']='White-Sox'
df.loc[df['away_team']=="Chicago White Sox",'home_team']='White-Sox'
df.loc[df['away_team']=="Toronto Blue Jays",'away_team']='Blue-Jays'
df.loc[df['away_team']=="Toronto Blue Jayx",'home_team']='Blue-Jays'

df['away_team'] = df['away_team'].apply(lambda x: x.split(' ')[-1])
df['home_team'] = df['home_team'].apply(lambda x: x.split(' ')[-1])

#Agregamos columna de resultado
df['juego']=(df['away_team']+" @ "+df['home_team'])

df['resultado']=np.where((df['home_team_runs']>df['away_team_runs']),
(df['home_team_runs'].astype(str)+"-"+df['away_team_runs'].astype(str)+" "+df['home_team']),
(df['away_team_runs'].astype(str)+"-"+df['home_team_runs'].astype(str)+" "+df['away_team']))

df = df.drop(columns=['home_team_runs','away_team_runs','home_team','away_team'])

#cambiamos el orden de las columnas
df = df[['juego','date','venue','resultado','attendance']]

#cambiamos nombre de las columnas
df.rename(columns={'date':'fecha','venue':'estadio','attendance':'asistencia'},inplace=True)

print_tabulate(df)

input()
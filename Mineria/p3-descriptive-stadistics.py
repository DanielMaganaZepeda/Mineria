import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

#Mayor asistencia
juego = df.iloc[df['attendance'].idxmax()]
print("Juego con mayor asistencia:",juego['away_team'],'@',juego['home_team'],',',juego['attendance'])

#Mayor asistencia en temporada regular
juego = df.iloc[(df[df['season']=='regular season'])['attendance'].idxmax()]
print("Juego de temporada regular con mayor asistencia:",juego['away_team'],'@',juego['home_team'],',',juego['attendance'])

#Menor asistencia
juego = df.iloc[df['attendance'].idxmin()]
print("Juego con menor asistencia:",juego['away_team'],'@',juego['home_team'],',',juego['attendance'])

#Menor asistencia en post season
juego = df.iloc[(df[df['season']=='post season'])['attendance'].idxmin()]
print("Juego de post season con menor asistencia:",juego['away_team'],'@',juego['home_team'],',',juego['attendance'])

#Total de asistentes en la temporada
print("Cantidad total de asistentes en la temporada: ",df['attendance'].sum())

#Promedio de asistencia
print("Promedio de asistencia por juego: ",df['attendance'].sum() / df['attendance'].count())

#Juego con la mayor diferencia de carreras
df['dif'] = abs(df['home_team_runs']-df['away_team_runs'])
juego = df.iloc[df['dif'].idxmax()]
print("Juego con mayor diferencia de carreras:",juego['away_team'],'@',juego['home_team'],":",juego['date'],
(juego['home_team_runs'].astype(str)+"-"+juego['away_team_runs'].astype(str)+" "+juego['home_team']) if juego['home_team_runs']>juego['away_team_runs'] 
else (juego['away_team_runs'].astype(str)+"-"+juego['home_team_runs'].astype(str)+" "+juego['away_team']))

input()
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

#Cambiamos el formato de los nombres de los equipos de {City, Team} => {City}
df.loc[df['away_team']=="Boston Red Sox",'away_team']='RedSox'
df.loc[df['home_team']=="Boston Red Sox",'home_team']='RedSox'
df.loc[df['away_team']=="Chicago White Sox",'away_team']='WhiteSox'
df.loc[df['home_team']=="Chicago White Sox",'home_team']='WhiteSox'
df.loc[df['away_team']=="Toronto Blue Jays",'away_team']='BlueJays'
df.loc[df['home_team']=="Toronto Blue Jays",'home_team']='BlueJays'

df['away_team'] = df['away_team'].apply(lambda x: x.split(' ')[-1])
df['home_team'] = df['home_team'].apply(lambda x: x.split(' ')[-1])

equipos = df['home_team'].tolist()
equipos = list(np.unique(equipos))

# Porcentaje del total de asistencia
""""
sizes = []
total = df['attendance'].sum()
for equipo in equipos:
    sizes.append(((df[(df['home_team']==equipo) & (df['season']=='regular season')])['attendance'].sum())/total)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=equipos, autopct='%1.1f%%')
ax1.axis('equal')
plt.title('Porcentaje de asistencia total en regulada temporal 2016 por equipo')
plt.savefig("C:/Users/Daniel/Mineria/Graficas/Porcentaje de asistencia total por equipo.png")
"""

#Total de carreras / errores
"""
sizes = []
for equipo in equipos:
    sizes.append((df[df['home_team']==equipo])['home_team_errors'].sum() + (df[df['away_team']==equipo])['away_team_errors'].sum())

fig1, ax1 = plt.subplots()
ax1.bar(equipos, sizes)
plt.title('Errores hechos por equipo')
plt.ylabel('Errores')
plt.xticks(rotation=90)
plt.savefig("C:/Users/Daniel/Mineria/Graficas/Errores hechos por equipo.png")

plt.show()
"""

input()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

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

sizes = []
for equipo in equipos:
    sizes.append((df[df['home_team']==equipo])['home_team_errors'].sum() + (df[df['away_team']==equipo])['away_team_errors'].sum())

fig, ax = plt.subplots()

#BOX PLOT MATLIB
''' 
positions = []
x=2
for equipo in equipos:
    positions.append(x)
    x=x+2

plt.style.use('_mpl-gallery')

VP = ax.boxplot(sizes, positions, widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False)

plt.show()
'''

df = pd.DataFrame({'Equipo': equipos, 'Errores':sizes})
moore_lm = ols('Equipo ~Errores', data=df).fit()
table = sm.stats.anova_lm(moore_lm, typ=2)
print(table)

input()
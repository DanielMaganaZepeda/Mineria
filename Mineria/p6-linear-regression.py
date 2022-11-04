import pandas as pd
import numpy as np
import statsmodels.api as sm
import numbers
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

#Cambiamos el formato de los nombres de los equipos de {City, Team} => {City}
velocidad_viento = df['wind_speed'].sort_values().unique()

errores = []
for velocidad in velocidad_viento:
    errores.append((df[df['wind_speed']==velocidad]['home_team_errors'].sum()+df[df['wind_speed']==velocidad]['away_team_errors'].sum())/df[df['wind_speed']==velocidad]['attendance'].count())

df = pd.DataFrame({'Velocidad':velocidad_viento, 'Errores':errores})


def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.show()

linear_regression(df,"Velocidad", "Errores")

print(df)

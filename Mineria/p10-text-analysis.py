from numpy import split
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)


df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

all_words = ""
#frase = df['home_team_runs'] # "hola a todos muchas  palabras palabras hola muchas hola hola hola palabras palabras hola muchas hola hola hola palabras palabras hola muchas hola hola hola palabras palabras hola muchas hola hola hola"
palabras = df['home_team_runs'].astype(str)

Counter(" ".join(palabras).split()).most_common(10)
# looping through all incidents and joining them to one text, to extract most common words
S = all_words.split()
C = pd.Categorical(S)

counts = df['home_team_runs'].value_counts()
counts.index = counts.index.map(str)
wordcloud = WordCloud().generate_from_frequencies(counts)

# print(all_words)
# plot the WordCloud image
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
plt.savefig("C:/Users/Daniel/Mineria/Graficas/TextAnalysis-CarrerasPromedio.png")
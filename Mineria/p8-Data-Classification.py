import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from scipy.stats import mode

def normalize_distribution(dist: np.array, n: int) -> np.array:
    b = dist - min(dist) + 0.000001
    c = (b / np.sum(b)) * n
    return np.round(c)


def create_distribution(mean: float, size: int) -> pd.Series:
    return normalize_distribution(np.random.standard_normal(size), mean * size)


def generate_df(means: List[Tuple[float, float, str]], n: int) -> pd.DataFrame:
    lists = [
        (create_distribution(_x, n), create_distribution(_y, n), np.repeat(_l, n))
        for _x, _y, _l in means
    ]
    x = np.array([])
    y = np.array([])
    labels = np.array([])
    for _x, _y, _l in lists:
        x = np.concatenate((x, _x), axis=None)
        y = np.concatenate((y, _y))
        labels = np.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})


def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)


def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = df['Hora']
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        ax.scatter(df[x_column], df[y_column], label=label, color=cmap(i))
    ax = plt.gca()
    ax.set_ylim([0, 100000])
    ax.set_xlim([0, 15])
    plt.savefig(file_path)
    plt.close()


def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


def k_nearest_neightbors(
    points: List[np.array], labels: np.array, input_data: List[np.array], k: int
):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]


groups = [(3, 100000, "Juegos matutinos"),(6, 100000, "Juegos vespertinos"),(9, 100000, "Juegos nocturnos")]
df = pd.read_csv('C:/Users/Daniel/Mineria/MLB 2016 Season.csv')

horas = []
temp = df['start_time']

for hora in temp:
    horas.append(float(hora.split()[0].split(':')[0]) + float((hora.split()[0]).split(':')[1])/60)

df = pd.DataFrame({'Hora':horas, 'Asistencia':df['attendance']})

scatter_group_by("C:/Users/Daniel/Mineria/Graficas/Test.png", df, "Hora", "Asistencia", "Hora")

input()
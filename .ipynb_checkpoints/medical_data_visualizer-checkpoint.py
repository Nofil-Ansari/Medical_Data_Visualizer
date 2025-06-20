import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_data.csv')

# 2
df['overweight'] = df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = df.copy()
    df_cat['cholesterol'] = (df_cat['cholesterol'] > 1).astype(int)
    df_cat['gluc'] = (df_cat['gluc'] > 1).astype(int)

    



    # 8
    fig = sns.catplot(
        x="variable",
        hue="value",
        col="cardio",
        data=pd.melt(df_cat, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]),
        kind="count"
    ).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

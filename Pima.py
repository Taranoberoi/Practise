import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ('C:\Files\PIMA.csv')

#print(df.head(5))
#print(" shape of the data is ",df.shape)
#print(df.tail(5))
#print(df.isnull())
#print(df.isnull().values.any())  # check if there is any null value in any of the column

def plot_corr(df, size=11):

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    plot_corr(df)
    plt.show(11)







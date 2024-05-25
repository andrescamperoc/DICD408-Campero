##Importar librerias
import pandas as pd
import numpy as numpy

#Extraccion
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data = pd.read_csv(wine_url, header=None)

wine_quality_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_url = pd.read_csv(wine_quality_url, sep=";")

#initial look at the data
print(wine_data.head())
print(wine_quality_url.head())
#Saving the transformed data as csv file

wine_data.to_csv("wine_dataset.csv", index=False)
wine_quality_url.to_csv('wine_quality_dataset.csv', index = False)
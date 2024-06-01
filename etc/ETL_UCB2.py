##Importar librerias
import pandas as pd
import numpy as numpy

#Extraccion
Valoreti = "NA&EMEA.csv"
valoreti_vct = pd.read_csv(Valoreti)

print(valoreti_vct.head())


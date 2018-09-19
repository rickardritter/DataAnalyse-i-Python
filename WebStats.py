import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np



#Viser stats paa besokte nettside, lager egne stats
web_stats = {'Dag':[1,2,3,4,5,6],
             'Besokende':[43,34,65,56,29,76],
             'Bytte Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats) #Lager en data frame

print(df.head())

df['Besokende'].plot() # Gjor det grafisk visualisering ved bruk av matplotlib
plt.show()

df.plot()
plt.show()

 # bruker numpy for aa printe liste
df2 = pd.DataFrame(np.array(df[['Besokende','Bytte Rate']]))
print(df2)

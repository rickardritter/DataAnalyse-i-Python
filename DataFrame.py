import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style


start = datetime.datetime(2015, 1, 1) #Dato for onsket aksjekurs
end = datetime.datetime.now()


df = web.DataReader("ORK.OL", "yahoo", start, end) # Verdien av Orkla aksjen fra 2015 til i dag.

style.use('fivethirtyeight')

print(df.head())

df['High'].plot() # bruker matplotlib for grafisk visualisering.
plt.legend()
plt.show()

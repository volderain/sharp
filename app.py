# This code is meant to calculate sharp ration among different equities

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
df['100ma'] = df['Close'].rolling(window=100).mean()
df.dropna(inplace=True)
print(df.head())
df['Close'].plot()
plt.show()

##start = dt.datetime(2000, 1, 1)
##end = dt.datetime(2016, 12, 31)

##df = web.DataReader('TSLA', 'yahoo', start, end)
##df.to_csv('TSLA.csv')
#print(df.head(6))
#print(df.tail(6))



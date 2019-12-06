from pandas_datareader import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# you are going to check if the file tsla.pkl exists
# if this file doesn't exist, you are going to fetch the data
# if this file exist you are going to read this file and create
# the dataframe tsla

try:
    tsla=pd.read_pickle('tsla.pkl')
    print('file found')
except:
    print('fine not found')
    tsla = data.DataReader("TSLA",
                       start='2009-1-1',
                       end='2019-1-31',
                       data_source='yahoo')
    tsla.to_pickle('tsla.pkl')

ts=pd.DataFrame(index=tsla.index)

ts['price']=tsla['Adj Close']
#lowest 30 day price
ts['support']=ts['price'].rolling(30).min()
#max 30 day price
ts['resistance']=ts['price'].rolling(30).max()
#support + the 0.05* difference between support and resistance
ts['tol_support']=ts['support']+ (ts['resistance']-ts['support'])*0.05
ts['tol_resistance']=ts['resistance'] - (ts['resistance']-\
                            ts['support'])*0.05

#if price is greater than the cap: sell
ts['signal_sell']=np.where(ts['price']>ts['tol_resistance'],1,0)
#if price is lower than the base: buy
ts['signal_buy']=np.where(ts['price']<ts['tol_support'],1,0)

ts['position']=pd.Series(np.zeros(len(ts)))
in_long_position=False
for i in range(len(ts)):
    if ts['price'][i]>ts['tol_resistance'][i]\
        and in_long_position:
        ts.position.values[i]=0
        in_long_position=False
    elif ts['price'][i]<ts['tol_support'][i]\
        and not in_long_position:
        ts.position.values[i]=1
        in_long_position=True
    elif in_long_position:
        ts.position.values[i]=1
    else:
        ts.position.values[i]=0

ts['signal']=ts['position'].diff()

fig=plt.figure()
ax1=fig.add_subplot(111,ylabel='Tesla Price')
ts['price'].plot(ax=ax1,color='red',lw=2.)
ts['tol_resistance'].plot(ax=ax1,color='blue',lw=2.)
ts['tol_support'].plot(ax=ax1,color='green',lw=2.)

ax1.plot(ts.loc[ts.signal ==1].index,
         ts.price[ts.signal ==1],
         '^',color='k',label='buy')
ax1.plot(ts.loc[ts.signal ==-1].index,
         ts.price[ts.signal ==-1],
         'v',color='k',label='sell')
plt.legend()
plt.show()



initial_capital=float(10000)
positions=pd.DataFrame(index=ts.index).fillna(0)
positions['TSLA']=10*ts['signal']
positions['TSLA'][0]=0
portfolio=positions.multiply(ts['price'],axis=0)
portfolio['holdings']=ts['position'].multiply(ts['price'],axis=0)*10
pos_diff=positions.diff()
portfolio['cash']=initial_capital - portfolio['TSLA'].cumsum()
portfolio['total']=portfolio['cash']+portfolio['holdings']
portfolio.plot()
plt.show()
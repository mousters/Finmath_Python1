from pandas_datareader import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression





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


def create_trading_strategy_data(financial_data):
    trading_strategy=pd.DataFrame(index=financial_data.index)
    trading_strategy['price']=financial_data['Adj Close']
    trading_strategy['openclose']= financial_data['Open'] - financial_data['Close']
    trading_strategy['highlow']= financial_data['High'] - financial_data['Low']
    trading_strategy['volume']=financial_data['Volume']
    trading_strategy['direction']=\
        np.where(trading_strategy['price']\
                 -trading_strategy['price'].\
                 shift(1)>=0,1,-1)
    trading_strategy['direction']=\
        trading_strategy['direction'].shift(-1)
    return trading_strategy


tsla_trading_strategy_trading=create_trading_strategy_data(tsla)

print(tsla_trading_strategy_trading)

X = tsla_trading_strategy_trading.loc[:,['price','openclose','highlow','volume']]
X = X[1:-1]
y = tsla_trading_strategy_trading.loc[:,'direction']
y = y[1:-1]

model=LogisticRegression()
model.fit(X,y)

pred_values=model.predict(X)
print(np.where(pred_values==y,1,0).mean())
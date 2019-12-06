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

except:
    print('fine not found')
    tsla = data.DataReader("TSLA",
                       start='2009-1-1',
                       end='2019-1-31',
                       data_source='yahoo')
    tsla.to_pickle('tsla.pkl')


def create_trading_strategy_data(financial_data):
    trading_strategy=pd.DataFrame(index=financial_data.index)
    # Empty
    # DataFrame
    # Columns: []
    # Index: [2010 - 06 - 29 00:00: 00, 2010 - 06 - 30...
    # [2164 rows x 0 columns]
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
#
# print(tsla_trading_strategy_trading)
#                  price  openclose    highlow    volume  direction
# Date
# 2010-06-29   23.889999  -4.889999   7.459999  18766300       -1.0
# 2010-06-30   23.830000   1.960001   7.120001  17187100       -1.0
# 2010-07-01   21.959999   3.040001   5.650000   8218800       -1.0
# 2010-07-02   19.200001   3.799999   4.390001   5139800       -1.0
# 2010-07-06   16.110001   3.889999   4.170000   6866900       -1.0
X = tsla_trading_strategy_trading.loc[:,['price','openclose','highlow','volume']]
X = X[1:-1]
y = tsla_trading_strategy_trading.loc[:,'direction']
y = y[1:-1]
# y
# Date
# 2010-06-30   -1.0
# 2010-07-01   -1.0
# 2010-07-02   -1.0
# 2010-07-06   -1.0
# 2010-07-07    1.0
#              ...

model=LogisticRegression()
model.fit(X,y)

pred_values=model.predict(X)
np.sum(pred_values)
print(np.where(pred_values==y,1,0).mean())
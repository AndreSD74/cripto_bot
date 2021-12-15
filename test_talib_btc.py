# testing TA-Lib with ETH historical 

# ETH = Ethereum

import investpy
import talib

import pandas as pd
import json
import numpy as np

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib


pd_eth = investpy.crypto.get_crypto_historical_data("Bitcoin", as_json=False, order='ascending', interval='Daily', from_date='01/01/2019', to_date='13/12/2021')

pd_eth.columns = [col.lower().replace(" ","_") for col in pd_eth.columns]

## Candle Stick
#  fig = go.Figure(data=go.Ohlc(
#    x=pd_eth.index,
#    open=pd_eth['open'],
#    high=pd_eth['high'],
#    low=pd_eth['low'],
#    close=pd_eth['close'],
# ))
# fig.show()


## SMA
pd_eth['sma'] = talib.SMA(pd_eth.close, 14)

pd_eth[['close','sma']].dropna().plot(
    title="média móvel",
    figsize=(20,8)
)


## Bollinger Bands
upper, middle, lower = (a.dropna() for a in talib.BBANDS(pd_eth.close, matype=talib.MA_Type.T3))
plt.figure(figsize=(20,12))
plt.plot(middle[-50:],"-.")
plt.plot(pd_eth.close[-50:], color="black")
plt.fill_between(
    middle[-50:].index,
    upper[-50:],lower[-50:],
    alpha=.1,
    color="red"
)

bbands = pd.concat([upper,lower,pd_eth.close],axis=1,join="inner")
bbands.columns=['up','lo','clo']

bbands['result'] = np.where(bbands.clo>bbands.up, 1, 0) # sell
bbands['result'] = np.where(bbands.clo<bbands.lo,-1, bbands.result) # buy


fig,ax = plt.subplots(2,1,figsize=(20,10))
ax[0].plot(bbands.clo[-100:],color="r")
ax[1].set_title('Sell and Buy')
ax[1].plot(bbands.result[-100:], color="blue")

plt.show()

## Three Inside Up/Down
# integer = talib.CDL3INSIDE(pd_eth.open ,pd_eth.high, pd_eth.low, pd_eth.close)
# integer.plot()


# ARRON
ad, aup = talib.AROON(pd_eth.high, pd_eth.low, timeperiod=14)

fig, ax = plt.subplots(2,1,figsize=(20,10))

ax[0].plot(pd_eth.close[-150:-50],color="r")
ax[1].plot(ad[-150:-50],color="blue")
ax[1].plot(aup[-150:-50],color="tab:orange")

plt.show()
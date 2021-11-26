# https://testnet.binance.vision/
# https://algotrading101.com/learn/binance-python-api-guide/
# https://python-binance.readthedocs.io/en/latest/overview.html


import os
binance_api = os.environ.get('binance_api')
binance_secret = os.environ.get('binance_secret')

from binance.client import Client

client = Client(binance_api, binance_secret)

# TEST's URL
client.API_URL = 'https://testnet.binance.vision/api'

# get account information
print(client.get_account())

# get balance for a specific asset only (BTC)
print(client.get_asset_balance(asset='BTC'))

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
print(btc_price)

#  print(client.get_exchange_info())



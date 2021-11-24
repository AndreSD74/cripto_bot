# pip install websocket-client

# https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md

# wss://stream.binance.com:9443

import websocket, json

# socket_tst = 'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'

# Bitcoin US$
coin_param = 'btcusd'
# Get for each 1 minute
interval = '1m'

# Connect String
socket_tst = f'wss://stream.binance.com:9443/ws/{coin_param}t@kline_{interval}'

# function is called when receive a message:
def on_message(ws, message):
    print(message)

# function is called when websocket is closed:
def on_close(ws, message):
    print("THE END")

# Creating WebSocket...
ws = websocket.WebSocketApp(
    socket_tst,
    on_message = on_message,
    on_close = on_close
)

# Run!
ws.run_forever()


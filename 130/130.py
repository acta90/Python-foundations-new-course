import websocket
import json
import datetime
import time
# API KEY: bpo8glvrh5ra872e30s0
# Symbol: BINANCE:BTCUSDT


def on_message(ws, message):
    x = json.loads(message)
    volume = x['data'][0]['v']
    price = x['data'][0]['p']
    print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), "price:", price, "volume:", volume)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bpo8glvrh5ra872e30s0",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


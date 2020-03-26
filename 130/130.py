import websocket
import threading
import json
import datetime

try:
    import thread
except ImportError:
    import _thread as thread
# API KEY: bpnp9mvrh5ra872du36g
# Symbol: BINANCE:BTCUSDT


mylist = []  # How to implement mylist outside of the global scope.


def on_message(ws, message):
    x = json.loads(message)
    volume = x['data'][0]['v']
    price = x['data'][0]['p']
    mylist.append(price)
    print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), "price:", price, "volume:", volume)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


def f(f_stop):
    try:
        avgprice = sum(mylist) / len(mylist)
        print('THE AVERAGE PRICE FOR THE LAST MINUTE IS: ', avgprice)
        mylist.clear()
    except:
        pass
    if not f_stop.is_set():
        threading.Timer(60, f, [f_stop]).start()


f_stop = threading.Event()
f(f_stop)
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bpnp9mvrh5ra872du36g",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

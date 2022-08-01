import csv
from dotenv import load_dotenv
import os
from binance.client import Client

load_dotenv()

b_key = os.getenv("BinanceAPI_Key")
print(b_key)
b_secret = os.getenv("BinanceAPI_Secret")
client = Client(b_key,b_secret)


"""
we want data from 2017 to 2022
we want data from 1min,5min,15min,1h,4h,1D,3D,1W,1M
"""

Intervals = [
    [Client.KLINE_INTERVAL_1MINUTE,"1min"],
    [Client.KLINE_INTERVAL_5MINUTE,"5min"],
    [Client.KLINE_INTERVAL_15MINUTE,"15min"],
    [Client.KLINE_INTERVAL_1HOUR,"1h"],
    [Client.KLINE_INTERVAL_4HOUR,"4h"],
    [Client.KLINE_INTERVAL_1DAY,"1d"],
    [Client.KLINE_INTERVAL_3DAY,"3d"],
    [Client.KLINE_INTERVAL_1WEEK,"1w"],
    [Client.KLINE_INTERVAL_1MONTH,"1m"],
]

Time_Periods = [
    ["1 Jan, 2017","31 Dec, 2017","2017"],
    ["1 Jan, 2018","31 Dec, 2018","2018"],
    ["1 Jan, 2019","31 Dec, 2019","2019"],
    ["1 Jan, 2020","31 Dec, 2020","2020"],
    ["1 Jan, 2021","31 Dec, 2021","2021"],
    ["1 Jan, 2022","1 Jul, 2022","2022H1"]
]

for time_period in Time_Periods:
    for interval in Intervals:
        candles = client.get_historical_klines("BTCUSDT",interval[0],time_period[0],time_period[1])
        
        i = interval[1]
        tp = time_period[2]
        filename = "DATA/BTCUSDT_{}_{}.csv".format(i,tp)
        csvfile = open(filename,"w",newline="")
        csvwriter = csv.writer(csvfile,delimeter=",")
        for candle in candles:
            candle[0] /= 10
            csvwriter.writerow(candle)
        csvfile.close()




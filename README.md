# BarPatternFinder
Repo that aims to find non-random patterns in price action

Data Folder Format:
{ASSET&PAIR}_{INTERVAL}_{TIME_PERIOD}
ex: BTCUSDT_4H_2020
ex: BTCUSDT_4H_2020Q1
ex: BTCUSDT_4H_2020H1
ex: BTCUSDT_15M_2020&2021

Candle Object Attributes:
-open, high, low, close, timestamp
-return: (close-open) / open
Pattern Object:
-Candle c1,c2,c3,c4,cI
-Candle followingCandle

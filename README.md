# BarPatternFinder
Repo that aims to find non-random patterns in price action
<br>
Data Folder Format:
<br>
{ASSET&PAIR}_{INTERVAL}_{TIME_PERIOD}
<br>
ex: BTCUSDT_4H_2020, BTCUSDT_4H_2020Q1, BTCUSDT_4H_2020H1, BTCUSDT_15M_2020&2021
<br>
Candle Object Attributes:
<br>
-open, high, low, close, timestamp
<br>
-return: (close-open) / open
<br>
Pattern Object:
<br>
-Candle c1,c2,c3,c4,cI
<br>
-Candle followingCandle

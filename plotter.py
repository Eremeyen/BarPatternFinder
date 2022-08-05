import matplotlib as plt
import json
import os
import green_red_pattern_finder


#test of matplotlib
filename = ("BTCUSDT_1d_2017.csv")
candles = green_red_pattern_finder.candles_from_CSV(filename)
l_three = green_red_pattern_finder.lengthThreeKlines(candles)

returns_dict = {}
for key in l_three:
    returns_dict[key] = []
    for kline in l_three[key]:
        returns_dict[key].append(kline.following_candle.ratio)

plt.plot(returns_dict[True,True,False])
plt.ylabel('return values')
plt.show

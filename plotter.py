import matplotlib.pyplot as plt
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
count = 0
x_axis = []
for i in returns_dict["[True, True, False]"]:
    x_axis.append(count)
    count += 1


plt.scatter(x_axis,returns_dict["[True, True, False]"], c="blue")
plt.savefig("plots/test.png")
#plt.show()

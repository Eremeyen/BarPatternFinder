import matplotlib.pyplot as plt
import json
import os
import green_red_pattern_finder


#test of matplotlib
filename = ("BTCUSDT_1d_2017.csv")
def getPlots(filename):
    candles = green_red_pattern_finder.candles_from_CSV(filename)
    l_three = green_red_pattern_finder.lengthThreeKlines(candles)

    returns_dict = {}
    for key in l_three:
        returns_dict[key] = []
        for kline in l_three[key]:
            returns_dict[key].append(kline.following_candle.ratio)
    for key in returns_dict:
        x_axis = []
        count = 0
        for i in returns_dict[key]:
            x_axis.append(count)
            count +=1
        plt.ylabel("following candle return")
        plt.xlabel("chronological order")
        plt.title(key + filename[:-4])
        plt.scatter(x_axis,returns_dict[key],c="blue")
        plt.savefig("plots/" + key + filename[:-4] + ".png")
    """
    count = 0
    x_axis = []
    for i in returns_dict["[True, True, False]"]:
        x_axis.append(count)
        count += 1
    

    plt.scatter(x_axis,returns_dict["[True, True, False]"], c="blue")
    plt.savefig("plots/test.png")
    """
#plt.show()
getPlots("BTCUSDT_4h_2020.csv")

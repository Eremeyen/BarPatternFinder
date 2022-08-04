#mean and median of following_candle ratio
#percentage of green following candles
#62 plots
import green_red_pattern_finder
import statistics
import os
#import mathplotlib



#example/rough code
filename = "BTCUSDT_4h_2022H1.CSV"

candles = green_red_pattern_finder.candles_from_CSV(filename)
length_three_p = green_red_pattern_finder.lengthThreeKlines(candles)
length_four_p = green_red_pattern_finder.lengthFourKlines(candles)
length_five_p = green_red_pattern_finder.lengthFiveKlines(candles)
#print(length_five_p)

#receives the dictionaries as inputs and outputs another dictionary
def statsDictionary(dic):
    dict = {}
    for key in dic:
        dict[key] = {}
        r_arr = []
        for i in dic[key]:
            print(i)
            r_arr.append(i.following_candle.ratio)
        print(len(r_arr))
        dict[key]["average return"] = sum(r_arr)/len(r_arr)
        dict[key]["median return"] = statistics.median(r_arr)
        dict[key]["number"] = len(dic[key])
        count = 0
        for i in dic[key]:
            if(i.following_candle.is_green):
                count +=1
        dict[key]["percentage of green candles"] = count / len(dic[key]) * 100
    return dict



five = statsDictionary(length_five_p)
print(five)

#idea: sort list of returns?
#store timestamps as well?
#use numpy arrays instead?

    





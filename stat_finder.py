#mean and median of following_candle ratio
#percentage of green following candles
#62 plots
import green_red_pattern_finder
import statistics
import os
import json
#import mathplotlib



#example/rough code
"""
filename = "BTCUSDT_4h_2022H1.CSV"

candles = green_red_pattern_finder.candles_from_CSV(filename)
length_three_p = green_red_pattern_finder.lengthThreeKlines(candles)
length_four_p = green_red_pattern_finder.lengthFourKlines(candles)
length_five_p = green_red_pattern_finder.lengthFiveKlines(candles)
"""

#receives the dictionaries as inputs and outputs another dictionary
def statsDictionary(dic):
    dict = {}
    for key in dic:
        dict[key] = {}
        r_arr = []
        for i in dic[key]:
            r_arr.append(i.following_candle.ratio*100)
        if(len(r_arr) != 0):
            dict[key]["average return"] = sum(r_arr)/len(r_arr)
        else:
            dict[key]["average return"] = "this pattern wasn't observed"
        if(len(r_arr) != 0):
            dict[key]["median return"] = statistics.median(r_arr)
        else:
            dict[key]["median return"] = "this pattern wasn't observed"
        dict[key]["number"] = len(dic[key])
        count = 0
        for i in dic[key]:
            if(i.following_candle.is_green):
                count +=1
        dict[key]["percengage of green candles"] = count / len(dic[key]) * 100 if len(r_arr) > 0 else "this pattern wasn't observed"
    return dict




#sample saving as json file:

"""
json = json.dumps(five)
jsonwriter = open("Pattern_Results/test.json","w")
jsonwriter.write(json)
jsonwriter.close
"""

def generate_json():
    for file in os.listdir("DATA"):
        candles = green_red_pattern_finder.candles_from_CSV(file)
        three_klines = green_red_pattern_finder.lengthThreeKlines(candles)
        three = statsDictionary(three_klines)

        four_klines = green_red_pattern_finder.lengthFourKlines(candles)
        four = statsDictionary(four_klines)

        five_klines = green_red_pattern_finder.lengthFiveKlines(candles)
        five = statsDictionary(five_klines)
        
        j = json.dumps(three)
        jsonwriter = open("Pattern_Results/" + "three" + file[:-4] +".json","w")
        jsonwriter.write(j)
        jsonwriter.close

        j = json.dumps(four)
        jsonwriter = open("Pattern_Results/" + "four" + file[:-4] +".json","w")
        jsonwriter.write(j)
        jsonwriter.close

        j = json.dumps(five)
        jsonwriter = open("Pattern_Results/" + "five" + file[:-4] +".json","w")
        jsonwriter.write(j)
        jsonwriter.close

generate_json()



#idea: sort list of returns?
#store timestamps as well?
#use numpy arrays instead?







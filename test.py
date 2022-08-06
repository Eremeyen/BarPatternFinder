import json
def bug_fix_number(filename):
    jsonfile = open(filename)
    dict = json.load(jsonfile)
    count = 0
    for key in dict:
        count += dict[key]["number"]
    jsonfile.close()
    return count

#print(bug_fix_number("Pattern_Results/fiveBTCUSDT_1d_2021.json"))

def weighted_percentage_average(filename):
    jsonfile = open(filename)
    dict = json.load(jsonfile)
    count = 0
    for key in dict:
        count += dict[key]["number"]*dict[key]["percengage of green candles"]
    return count / bug_fix_number(filename)

print(weighted_percentage_average("Pattern_Results/fiveBTCUSDT_1min_2022H1.json"))

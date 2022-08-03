import csv
from itertools import permutations

class klineN:
    def __init__(self,candles,followingCandle):
        self.candles = candles
        self.followingCandle = followingCandle
class Candle:
    def __init__(self,open,high,low,close,timestamp):
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.timestamp = float(timestamp)
        self.is_green = float(close) > float(open)
        self.ratio = (float(close)-float(open)) / float(open)

#implementing simple green/red patterns
#green is true, red is false
pat_l1 = [[True],[False]]

pat_l2 = [[True, False],[True, True],[False,False],[False,True]]

t1 = permutations([True,True,False])
t2 = permutations([False,False,True])
pat_l3 = [[True,True,True],[False,False,False]]
#probably need to use a for loop instead
for i in list(t1):
    pat_l3.append(list(i))
for i in list(t2):
    pat_l3.append(list(i))



f1 = permutations([True,True,False,False])
f2 = permutations([True,True,True,False])
f3 = permutations([False,False,False,True])
pat_l4 = [[True,True,True,True],[False,False,False,False]]
for i in list(f1):
    pat_l4.append(list(i))
for i in list(f2):
    pat_l4.append(list(i))
for i in list(f3):
    pat_l4.append(list(i))

fi1 = permutations([True,False,False,False,False])
fi2 = permutations([True,True,False,False,False])
fi3 = permutations([True,True,True,False,False])
fi4 = permutations([True,True,True,True,False])
pat_l5 = [[True,True,True,True,True],[False,False,False,False,False]]
for i in list(fi1):
    pat_l5.append(list(i))
for i in list(fi2):
    pat_l5.append(list(i))
for i in list(fi3):
    pat_l5.append(list(i))
for i in list(fi4):
    pat_l5.append(list(i))




def candles_from_CSV(filename):
    csvfile = open("DATA/" + filename)
    csv_reader = csv.reader(csvfile)
    candles = []
    for row in csv_reader:
        candles.append(row)
    csvfile.close()
    return candles

def lengthThreeKlines(candles):
    pattern_dict = {}
    for i in pat_l3:
        s = str(i)
        pattern_dict[s] = []
    for i in range(len(candles)-4):
        check_pattern = []
        c1 = Candle(candles[i][1],candles[i][2],candles[i][3],candles[i][4],candles[i][0])
        c2 = Candle(candles[i+1][1],candles[i+1][2],candles[i+1][3],candles[i+1][4],candles[i+1][0])
        c3 = Candle(candles[i+2][1],candles[i+2][2],candles[i+2][3],candles[i+2][4],candles[i+2][0])
        cf = [c1,c2,c3]
        c4 = Candle(candles[i+3][1],candles[i+3][2],candles[i+3][3],candles[i+3][4],candles[i+3][0])
        check_pattern.append(c1.is_green)
        check_pattern.append(c2.is_green)
        check_pattern.append(c3.is_green)
        for key in pattern_dict:
            if(key == str(check_pattern)):
                pattern_dict[key].append(klineN(cf,c4))
    return pattern_dict

   
def lengthFourKlines(candles):
    pattern_dict = {}
    for i in pat_l4:
        s = str(i)
        pattern_dict[s] = []
    for i in range(len(candles)-5):
        check_pattern = []
        c1 = Candle(candles[i][1],candles[i][2],candles[i][3],candles[i][4],candles[i][0])
        c2 = Candle(candles[i+1][1],candles[i+1][2],candles[i+1][3],candles[i+1][4],candles[i+1][0])
        c3 = Candle(candles[i+2][1],candles[i+2][2],candles[i+2][3],candles[i+2][4],candles[i+2][0])
        c4 = Candle(candles[i+3][1],candles[i+3][2],candles[i+3][3],candles[i+3][4],candles[i+3][0])
        cs = [c1,c2,c3,c4]
        cf = Candle(candles[i+4][1],candles[i+4][2],candles[i+4][3],candles[i+4][4],candles[i+4][0])
        check_pattern.append(c1.is_green)
        check_pattern.append(c2.is_green)
        check_pattern.append(c3.is_green)
        check_pattern.append(c4.is_green)
        for key in pattern_dict:
            if(key == str(check_pattern)):
                pattern_dict[key].append(klineN(cs,cf))
        return pattern_dict

   

def lengthFiveKlines(candles):
    pattern_dict = {}
    for i in pat_l5:
        s = str(i)
        pattern_dict[s] = []
    for i in range(len(candles)-6):
        check_pattern = []
        c1 = Candle(candles[i][1],candles[i][2],candles[i][3],candles[i][4],candles[i][0])
        c2 = Candle(candles[i+1][1],candles[i+1][2],candles[i+1][3],candles[i+1][4],candles[i+1][0])
        c3 = Candle(candles[i+2][1],candles[i+2][2],candles[i+2][3],candles[i+2][4],candles[i+2][0])
        c4 = Candle(candles[i+3][1],candles[i+3][2],candles[i+3][3],candles[i+3][4],candles[i+3][0])
        c5 = Candle(candles[i+4][1],candles[i+4][2],candles[i+4][3],candles[i+4][4],candles[i+4][0])
        cs = [c1,c2,c3,c4,c5]
        cf = Candle(candles[i+5][1],candles[i+5][2],candles[i+5][3],candles[i+5][4],candles[i+5][0])
        check_pattern.append(c1.is_green)
        check_pattern.append(c2.is_green)
        check_pattern.append(c3.is_green)
        check_pattern.append(c4.is_green)
        check_pattern.append(c5.is_green)
        for key in pattern_dict:
            if(key == str(check_pattern)):
                pattern_dict[key].append(klineN(cs,cf))
        return pattern_dict
    





    



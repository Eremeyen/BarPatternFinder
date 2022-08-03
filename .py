#mean and median of following_candle ratio
#percentage of green following candles
#62 plots
import green_red_pattern_finder
#import mathplotlib



#example/rough code
filename = "BTCUSDT_1m_2022H1.CSV"

candles = green_red_pattern_finder.candles_from_CSV(filename)
length_three_p = green_red_pattern_finder.lengthThreeKlines(candles)
length_four_p = green_red_pattern_finder.lengthFourKlines(candles)
length_five_p = green_red_pattern_finder.lengthFiveKlines(candles)

print(length_three_p)




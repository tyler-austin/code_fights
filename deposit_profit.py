import math


def deposit_profit(deposit, rate, threshold):
    return math.ceil((math.log(threshold) - math.log(deposit))/(math.log(1 + (rate / 100))))

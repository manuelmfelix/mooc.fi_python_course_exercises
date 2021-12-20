# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower,upper))
    weekly_draw = sample(number_pool, amount)
    weekly_draw.sort()
    return weekly_draw
    



if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
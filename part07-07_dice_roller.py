# Write your solution here
from random import *

def roll(die: str):
    A = (3,3,3,3,3,6)
    B = (2,2,2,5,5,5)
    C = (1,4,4,4,4,4)

    return choice(locals()[die])

def  play(die1: str, die2: str, times: int):
    A = (3,3,3,3,3,6)
    B = (2,2,2,5,5,5)
    C = (1,4,4,4,4,4)
    a,b,c=0,0,0

    for _ in range(times):
        d = choice(locals()[die1])
        e = choice(locals()[die2])
        if d > e:
            a += 1
        elif d < e:
            b += 1
        else:
            c += 1
    return (a,b,c)



if __name__ == "__main__":
    result = play("A", "B", 10)
    print(result)
    # result = play("B", "B", 1000)
    # print(result)
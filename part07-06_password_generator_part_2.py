# Write your solution here
from random import *
from string import *

def generate_strong_password(value: int, first: bool, second: bool):
    password = ""
    touse,punct = "",""
    touse += ascii_lowercase
    password += choice(touse)
    if first == True:
        touse += digits
    if second == True:
        for a in punctuation:
            if a in "!?=+-()#":
                punct += a
                touse += punct
    if first == True and value-len(password) > 0:
        password += choice(digits)
    if first == True and second == True and value-len(password) > 0 or second == True and value-len(password) > 0:
        password += choice(punct)

    if value-len(password)>0:
        for _ in range(value-len(password)):
            password += choice(touse)
        
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
    # print(generate_strong_password(5,False,False))
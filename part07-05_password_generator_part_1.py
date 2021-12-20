# Write your solution here
from random import *
from string import *

def generate_password(value: int):
    password = ""
    # print(choice(ascii_lowercase))
    for i in range(value):
        password += choice(ascii_lowercase)
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
    # generate_password(8)
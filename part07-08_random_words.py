# Write your solution here
from random import *
from string import *

def words(n: int, beginning: str):

    mylist = []

    with open("words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            mylist.append(line)
            
    newlist = []
    test = []

    for a in mylist:
        if a.startswith(beginning) and a not in test:
            test.append(a)
    if len(test) < n:
        raise ValueError

    newlist = sample(test,n)

    return newlist


if __name__ == "__main__":
    word_list = words(10, "carbi")
    for word in word_list:
        print(word)
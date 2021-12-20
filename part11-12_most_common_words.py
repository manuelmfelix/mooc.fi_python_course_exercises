# WRITE YOUR SOLUTION HERE:
from string import *

def most_common_words(filename: str, lower_limit: int):

    with open(filename) as new_file:
        contents = new_file.read()
    
    contents = contents.translate(str.maketrans('', '', punctuation))

    final = []

    for line in contents.split():
        final.append(line)

    return {word: final.count(word) for word in final if final.count(word) >= lower_limit}
    
    # return {word: contents.count(word) for word in contents.split() if contents.count(word) > lower_limit}

if __name__ =='__main__':
    #sentence = "List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list. However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly. Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension."
    print(most_common_words("comprehensions.txt", 3))
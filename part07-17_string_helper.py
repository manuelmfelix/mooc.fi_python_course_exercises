# Write your solution here
from string import *

def change_case(orig_string: str):
    a = list(orig_string)
    new = ""
    for b in a:
        if b.isupper():
            new += b.lower()
        elif b.islower():
            new += b.upper()
        elif b == " ":
            new += " "
    return new

def split_in_half(orig_string: str):
    a = int(len(orig_string)/2)
    b = orig_string[0:a]
    c = orig_string[a:len(orig_string)]
    d = (b,c)
    return d

def remove_special_characters(orig_string: str):
    a = list(orig_string)
    c = ascii_lowercase+ascii_uppercase+digits+" "
    new = ""
    for b in a:
        if b in c:
            new += b
    return new


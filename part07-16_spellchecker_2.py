# write your solution here
from difflib import *

if True:
    text = input("Write text: ")
else:
    text = "this is acually a good and usefull program"

wordcheck = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        wordcheck.append(line)

text2 = text.split()
text3 = []
text4 = []
for a in text2:
    if a.lower() not in wordcheck:
        text4.append(a)
        a = f"*{a}*"
    text3.append(a)

print(" ".join(text3))
print("seggestions:")

for b in text4:
    print(f"{b}: ",end="")
    a = get_close_matches(b,wordcheck)
    counter = 0
    for i in a:
        if counter != len(a)-1:
            print(i, end=", ")
            counter += 1
        else:
            print(i)


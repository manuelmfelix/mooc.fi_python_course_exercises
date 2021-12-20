# write your solution here
if True:
    text = input("Write text: ")
else:
    text = "We use ptython to make a spell checker"

wordcheck = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        wordcheck.append(line)



# text2 = text.split()
# text3 = []
# for a in text2:
#     if a.lower() not in wordcheck:
#         a = f"*{a}*"
#     text3.append(a)

print(" ".join(text3))

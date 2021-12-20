# Write your solution here
concat = ""
b = ""
while True:
    a = input("Please type in a word: ")
    if a == "end":
        break
    if a == b:
        break
    b = a
    concat += a + " "

print(concat)
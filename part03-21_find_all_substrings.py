# Write your solution here
a = input("Please type in a word: ")
b = input("Please type in a character: ")

while a.find(b)!= -1:
    if a.find(b)+3<=len(a):
        print(a[a.find(b):a.find(b)+3])
    a = a[a.find(b)+1:]

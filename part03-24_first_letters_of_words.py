# Write your solution here
a = input("Please type in a sentence: ")
print(a[0])
while a.find(" ")!= -1:
    a = a[a.find(" ")+1:]
    print(a[0])
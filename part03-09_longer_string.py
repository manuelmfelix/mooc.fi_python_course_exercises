# Write your solution here
a = input("Please type in string 1: ")
b = input("Please type in string 2: ")
if len(a)>len(b):
    print(f"{a} is longer")
elif len(b)>len(a):
    print(f"{b} is longer")
else:
    print("The strings are equally long")

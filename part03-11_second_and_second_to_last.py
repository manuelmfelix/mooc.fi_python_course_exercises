# Write your solution here
a = input("Please type in a string: ")
b = a[1]
c = a[-2]
if b != c:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {b}")
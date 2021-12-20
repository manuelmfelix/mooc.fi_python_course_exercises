# Write your solution here
a = int(input("Please type in a number: "))
b=1
c=a
while b != c and c>b:
    print(b)
    print(c)
    b += 1
    c -= 1
if a%2!=0:
    print(b)
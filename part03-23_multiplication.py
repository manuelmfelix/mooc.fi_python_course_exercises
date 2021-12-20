# Write your solution here
a = int(input("Please type in a number: "))
b = 1
c = 1
while c <= a:
    while b <= a:
        print(f"{c} x {b} = {c*b}")
        b += 1
    c += 1
    b = 1
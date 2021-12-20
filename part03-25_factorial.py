# Write your solution here
b = 1
c = 1
d = 1
while b > 0:
    b = int(input("Please type in an amount: "))
    c = 1
    d = 1
    if b <= 0:
        print("Thanks and bye!")
        break
    while c <= b:
        d *= c
        c += 1
    print(f"The factorial of the number {b} is {d}")
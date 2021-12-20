# Write your solution here
num = int(input("Limit: "))
a = 2
sum = 1
concat = "1"
while sum < num:
    concat += f" + {a}"
    sum += a
    a += 1


print(f"The consecutive sum: {concat} = {sum}")
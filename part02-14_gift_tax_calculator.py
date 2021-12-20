# Write your solution here
num = int(input("Value of gift: "))
if num < 5000:
    print("No tax!")
elif num <= 25000:
    print(f"Amount of tax: {(100 + (num - 5000) * 0.08)} euros")
elif num <= 55000:
    print(f"Amount of tax: {(1700 + (num - 25000) * 0.10)} euros")
elif num <= 200000:
    print(f"Amount of tax: {(4700 + (num - 55000) * 0.12)} euros")
elif num <= 1000000:
    print(f"Amount of tax: {(22100 + (num - 200000) * 0.15)} euros")
elif num>1000000:
    print(f"Amount of tax: {(142100 + (num - 1000000) * 0.17)} euros")
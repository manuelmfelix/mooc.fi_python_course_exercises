# Write your solution here
num = int(input("What is your age? "))
if num>=5 and num<120:
    print(f"Ok, you're {num} years old")
elif num<5 and num>=0:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
# Write your solution here
num1 = input("Please type in the 1st word: ")
num2 = input("Please type in the 2nd word: ")
if num1>num2:
    print(f"{num1} comes alphabetically last.")
elif num1<num2:
    print(f"{num2} comes alphabetically last.")
elif num1==num2:
    print("You gave the same word twice.")
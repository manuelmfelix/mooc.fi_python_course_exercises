# Write your solution here
num = int(input("Please type in a year: "))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")

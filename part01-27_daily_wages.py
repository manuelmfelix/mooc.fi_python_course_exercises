# Write your solution here
wage = float(input("Hourly wage: "))
worked = int(input("Hours worked: "))
week = input("Day of the week: ")
if week=="Monday" or week=="Tuesday" or week=="Wednesday" or week=="Thursday" or week=="Friday" or week=="Saturday":
    print(f"Daily wages: {wage * worked} euros")

if week == "Sunday":
    print(f"Daily wages: {wage*2 * worked} euros")
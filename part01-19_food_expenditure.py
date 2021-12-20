# Write your solution here
cafe = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))


print("Average food expenditure:")
print(f"Daily: {(lunch*cafe+groceries)/7} euros")
print(f"Weekly: {cafe*lunch+groceries} euros")
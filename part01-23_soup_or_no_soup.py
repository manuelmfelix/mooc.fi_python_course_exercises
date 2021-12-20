# Write your solution here
name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")

if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    price = 5.90
    print(f"The total cost is {portions*price}\nNext please!")
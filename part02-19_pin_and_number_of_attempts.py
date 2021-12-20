# Write your solution here
count = 0
while True:
    num = int(input("PIN: "))
    count += 1
    if num == 4321:
        if count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {count} attempts")
        break
    print("Wrong")
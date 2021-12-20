# Write your solution here
pass1 = input("Password: ")
while True:
    pass2 = input("Repeat password: ")
    if pass1==pass2:
        break
    print("They do not match!")

print("User account created!")
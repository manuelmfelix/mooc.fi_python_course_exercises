# Write your solution here
phoneBook = {}
while True:
    a = int(input("command (1 search, 2 add, 3 quit):" ))
    if a == 1:
        name = input("name: ")
        if name not in phoneBook:
            print("no number")
        else:
            print(phoneBook[name][0])
    if a == 2:
        name = input("name: ")
        number = input("number")
        phoneBook[name]=[number]
        #print(phoneBook)
        print("ok!")
    if a == 3:
        print("quitting...")
        break

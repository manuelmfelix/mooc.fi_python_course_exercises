# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    a = int(input("Function: "))
    if a == 1:
        b = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(f"{b}\n")
        print("Diary saved")
    elif a == 2:
        print("Entries: ")
        with open("diary.txt") as new_file:
            for line in new_file:
                if line != "\n":
                    line = line.strip()
                    print(line)
    elif a == 0:
        print("Bye now!")
        break
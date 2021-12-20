# Write your solution here

while True:
    print("1 - add word, 2 - search, 3 - quit")
    a = int(input("Function: "))
    if a == 1:
        b = input("The word in Finnish: ")
        c = input("The word in English: ")
        with open("dictionary.txt", "a") as my_file:
            my_file.write(f"{b} {c}\n")
        print("Dictionary entry added")
    elif a == 2:
        searchterm = input("Search term: ")
        with open("dictionary.txt") as new_file:
            for line in new_file:
                if line != "\n":
                    line = line.strip()
                    line = line.split()
                    if searchterm in line[0] or searchterm in line[1]:
                        print(f"{line[0]} - {line[1]}")
    elif a == 3:
        print("Bye!")
        break
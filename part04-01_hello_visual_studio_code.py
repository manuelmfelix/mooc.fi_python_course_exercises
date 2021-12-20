# Write your solution here
a=""
while True:
    a = input("Editor: ")
    a = a.lower()
    if a != "visual studio code":
        if a =="word" or a == "notepad":
            print("awful")
        else:
            print("not good")
    else:
        print("an excellent choice!")
        break
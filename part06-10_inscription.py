# Write your solution here
a = input("Whom should I sign this to: ")
b = input("Where shall I save it: ")

with open(b,"w") as my_file:
    my_file.write(f"Hi {a}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
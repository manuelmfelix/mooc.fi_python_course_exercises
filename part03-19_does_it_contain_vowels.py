# Write your solution here
b = input("Please type in a string: ")
c="aeo"
d=0
while d<len(c):
    substring  = c[d]
    if substring  in b:
        print(f"{substring} found")
    else:
        print(f"{substring} not found")
    d += 1
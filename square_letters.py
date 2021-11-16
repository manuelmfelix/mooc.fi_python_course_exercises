# Write your solution here
letters = ["A","B","C","D","E","F","G","H", "I", "J", "K", "L", "M", "N", "O", \
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
layers = int(input("Layers: "))
width = layers*2-1
counter = layers-1
while counter > -layers:
    a = layers-1
    while a > -layers:
        b = a
        if abs(b) < abs(counter):
            b = counter
        print(letters[abs(b)],end="")
        a -= 1
    print()
    counter -= 1
# Write your solution here
a = int(input("Width: "))
b = int(input("Height: "))
c=0
concat=""
while c<a:
    concat+="#"
    c+=1

print(f"{concat}\n"*b)
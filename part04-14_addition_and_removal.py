# Write your solution here
my_list=[]
a=1
print(f"The list is now {my_list}")
while True:
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "x":
        print("Bye!")
        break
    elif choice == "d":
        my_list.append(a)
        a += 1
        print(f"The list is now {my_list}")
    elif choice == "r":
        a -= 1
        my_list.remove(a)
        print(f"The list is now {my_list}")
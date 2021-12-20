# Write your solution here
my_list=[]
a = 0
while True:
    num = int(input("How many items: "))
    while a < num:
        b = int(input(f"Item {a+1}: "))
        my_list.append(b)
        a += 1
    print(my_list)
    break
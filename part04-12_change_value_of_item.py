# Write your solution here
my_list = [1,2,3,4,5]
while True:
    num = int(input("Index: "))
    if num == -1:
        break
    new = int(input("New value: "))
    my_list[num]=new
    print(my_list)
# Write your solution here
my_list=[]
while True:
    a = input("Word: ")
    if a in my_list:
        print(f"You typed in {len(my_list)} different words")
        break
    my_list.append(a)

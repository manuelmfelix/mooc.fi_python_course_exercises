# Write your solution here
a = input("Word: ")
print("*"*30)
b = int((30-len(a))/2-1)
if len(a)%2==0:
    print("*" + b*" " + a + b*" " + "*")
else:
    print("*" + b*" " + a + b*" " + " *")
#print(len("*" + b*" " + a + b*" " + "*"))

print("*"*30)
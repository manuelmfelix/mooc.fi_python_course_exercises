# Write your solution here
a = input("Please type in a word: ")
b = input("Please type in a character: ")
c = a.find(b)
if c >= 0:
    c = a.find(b, c+len(b))

if c!=-1:
    print(f"The second occurrence of the substring is at index {c}.")
else:
    print("The substring does not occur twice in the string.")
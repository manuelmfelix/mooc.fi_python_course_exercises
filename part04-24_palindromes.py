# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(a):
    return a == a[::-1]


while True:
    a = input("Please type in a palindrome: ")
    if palindromes(a) == True:
        print(f"{a} is a palindrome!")
        break
    print("that wasn't a palindrome")


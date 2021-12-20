# Write your solution here
def histogram(string):
    letters = {}
    for i in string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for a in letters:
        print(f"{a} "+"*"*letters[a])
    return

if __name__ == "__main__":
    print(histogram("abba"))

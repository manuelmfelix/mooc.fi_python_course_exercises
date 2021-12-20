# Write your solution here
def no_vowels(a):
    b = 0
    c=""
    while b < len(a):
        if a[b] not in "aeiou":
            c += a[b]
        b += 1
    return c



if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
# Write your solution here
def most_common_character(a):
    b = 0
    c=""
    d = 0
    while b < len(a):
        if a.count(a[b]) > d:
            d = a.count(a[b])
            c = a[b]
        b += 1
    return c



if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
# Write your solution here
def distinct_numbers(a: list):
    b = []
    for c in a:
        if c not in b:
            b.append(c)
    return (sorted(b))


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
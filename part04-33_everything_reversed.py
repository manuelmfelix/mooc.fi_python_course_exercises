# Write your solution here
def everything_reversed(a: list):
    b = []
    a = a[::-1]
    for c in a:
        b.append(c[::-1])
    return b


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
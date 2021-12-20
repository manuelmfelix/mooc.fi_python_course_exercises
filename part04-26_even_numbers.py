# Write your solution here
def even_numbers(a: list):
    c = []
    for b in a:
        if b%2==0:
            c.append(b)
    return c

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
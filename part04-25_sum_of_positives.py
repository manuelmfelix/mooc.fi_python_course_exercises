# Write your solution here
def sum_of_positives(a: list):
    c = 0
    for b in a:
        if b>0:
            c += b
    return c

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
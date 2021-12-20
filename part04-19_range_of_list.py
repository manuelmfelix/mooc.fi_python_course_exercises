# Write your solution here
def  range_of_list(a: list):
    a = sorted(a)
    b = a[len(a)-1]-a[0]
    return b
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
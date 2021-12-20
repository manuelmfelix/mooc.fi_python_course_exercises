# Write your solution here
def mean(a: list):
    b = sum(a)/len(a)
    return b
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
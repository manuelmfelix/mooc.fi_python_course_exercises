# Write your solution here
def length_of_longest(a: list):
    c = 0
    for b in a:
        if len(b)>c:
            c = len(b)
    return (c)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
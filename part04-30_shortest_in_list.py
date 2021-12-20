# Write your solution here
def shortest(a: list):
    c = a[0]
    for b in a:
        if len(b)<len(c):
            c = b
    return (c)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
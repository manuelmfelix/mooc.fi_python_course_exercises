# Write your solution here
def all_the_longest(a: list):
    c = []
    c.append(a[0])
    for b in a:
        for d in c:  
            if len(b)>len(d):
                c = []
                c.append(b)
    for b in a:
        if len(b) == len(c[0]) and b not in c:
            c.append(b)
    return (c)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
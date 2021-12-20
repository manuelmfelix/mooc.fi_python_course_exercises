# Write your solution here

def oldest_person(people: list):
    a = people[0]
    for b in people:
        if b[1]<a[1]:
            print("B: ",b)
            print("A: ",a)
            a = b
        
    return a[0]


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))



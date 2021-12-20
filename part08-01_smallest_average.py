# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    list = [person1,person2,person3]
    small = 30
    person = {}
    name = ""
    for a in list:
        b = a.pop("name")
        c = sum(a.values())/3
        if c < small:
            person = a
            name = b
            small = c
    person["name"] = name
    return person
    # for a in list:
    #     for a.keys() in new:
    #         print(a.keys())
    # list = [person1.pop('name', None),person2.pop('name', None),person3.pop('name', None)]
    # result = person1.pop('name', None)
    # print(result)

if __name__ == "__main__":

    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
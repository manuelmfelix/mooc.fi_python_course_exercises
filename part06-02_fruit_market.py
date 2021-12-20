# write your solution here

def read_fruits():
    dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = parts[1]
            dictionary[name] = float(price)
    return dictionary


if __name__ == "__main__":
    print(read_fruits())
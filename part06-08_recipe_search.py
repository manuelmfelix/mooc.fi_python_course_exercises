# Write your solution here

def search_by_name(filename: str, word: str):

    recipebooklist = []
    test = []

    with open(filename) as new_file:
        for line in new_file:
            if line != "\n":
                line = line.strip()
                test.append(line)
            else:
                recipebooklist.append(test)
                test = []
            recipebooklist.append(test)

    recipebook = {}
    for a in recipebooklist:
        recipebook[a[0]]=a[1:]
    # print(recipebook)
    # print(recipebook.keys())
    search = []
    for a in recipebook.keys():
        if word.lower() in a.lower():
            search.append(a)
    
    return search

def search_by_time(filename: str, prep_time: int):

    recipebooklist = []
    test = []

    with open(filename) as new_file:
        for line in new_file:
            if line != "\n":
                line = line.strip()
                test.append(line)
            else:
                recipebooklist.append(test)
                test = []
            recipebooklist.append(test)

    recipebook = {}
    for a in recipebooklist:
        recipebook[a[0]]=a[1:]
    # print(recipebook)
    # print(recipebook.keys())
    search = []
    for a in recipebook.keys():
        # print(recipebook[a][0])
        # print("Perp: ", prep_time+int(recipebook[a][0]))
        if prep_time > int(recipebook[a][0]):
            search.append(f"{a}, preparation time {recipebook[a][0]} min")
    return search



def search_by_ingredient(filename: str, ingredient: str):

    recipebooklist = []
    test = []

    with open(filename) as new_file:
        for line in new_file:
            if line != "\n":
                line = line.strip()
                test.append(line)
            else:
                recipebooklist.append(test)
                test = []
            recipebooklist.append(test)

    recipebook = {}
    for a in recipebooklist:
        recipebook[a[0]]=a[1:]
    # print(recipebook)
    # print(recipebook.keys())
    search = []
    for a in recipebook.keys():
        # print(recipebook[a][0])
        # print("Perp: ", prep_time+int(recipebook[a][0]))
        if ingredient in recipebook[a][1:]:
            search.append(f"{a}, preparation time {recipebook[a][0]} min")
    return search


if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
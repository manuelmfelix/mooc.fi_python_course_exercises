# Write your solution here
def no_shouting(a: list):
    b = []
    for c in a:
        if not c.isupper():
            b.append(c)
    return(b)
    



if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
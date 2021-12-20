# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            line = int(line.replace("\n", ""))
            if line > largest:
                largest = line
        return largest

if __name__ == "__main__":
    print(largest())
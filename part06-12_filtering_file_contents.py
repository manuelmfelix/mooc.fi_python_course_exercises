# Write your solution here
def filter_solutions():
    solutions = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            parts = line.split(';')
            parts[len(parts)-1] = parts[len(parts)-1].strip()
            solutions.append(parts)
    
    countercor = 0
    counterin = 0
    for a in solutions:
        if "+" in a[1]:
            b = a[1].split("+")
            if int(b[0])+int(b[1])==int(a[2]):
                if countercor == 0:
                    with open("correct.csv", "w") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
                    countercor += 1
                else:
                    with open("correct.csv", "a") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
            else:
                if counterin == 0:
                    with open("incorrect.csv", "w") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
                    counterin += 1
                else:
                    with open("incorrect.csv", "a") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")

        elif "-" in a[1]:
            b = a[1].split("-")
            if int(b[0])-int(b[1])==int(a[2]):
                if countercor == 0:
                    with open("correct.csv", "w") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
                    countercor += 1
                else:
                    with open("correct.csv", "a") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
            else:
                if counterin == 0:
                    with open("incorrect.csv", "w") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")
                    counterin += 1
                else:
                    with open("incorrect.csv", "a") as my_file:
                        line = f"{a[0]};{a[1]};{a[2]}"
                        my_file.write(line+"\n")



if __name__ == "__main__":
    filter_solutions()


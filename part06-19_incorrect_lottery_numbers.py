# Write your solution here

def filter_incorrect():
    counter = 0
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            parts = line.split(';')
            week = parts[0].split()
            numbers = parts[1].split(',')
            
            try:
                teste = int(week[1])
                if len(numbers) == 7:
                    pass
                else:
                    raise ValueError
                teste2=[]
                for a in numbers:
                    b = int(a)
                    if b<0 or b<40:
                        raise ValueError
                    if b in teste2:
                        raise ValueError
                    teste2.append(a)

                if counter == 0:
                    with open("correct_numbers.csv", "w") as my_file:
                        my_file.write(line)
                        counter += 1
                else:
                    with open("correct_numbers.csv", "a") as my_file:
                        my_file.write(line)

            except:
                pass


if __name__ == "__main__":
    filter_incorrect()

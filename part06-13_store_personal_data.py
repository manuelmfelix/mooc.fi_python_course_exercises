# Write your solution here
def store_personal_data(person: tuple):
    a = list(person)
    with open("people.csv", "a") as my_file:
        line = f"{a[0]};{a[1]};{a[2]}"
        my_file.write(line+"\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
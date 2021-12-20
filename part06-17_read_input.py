# Write your solution here
def read_input(a: str, min: int, max: int):
    while True:
        try:
            input_str = input(a)
            number = int(input_str)
            if number <= max and number >= min:
                return number
        except ValueError:
            pass

        print("You must type in an integer between 5 and 10")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
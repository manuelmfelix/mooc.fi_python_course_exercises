# Write your solution here
def remove_smallest(numbers: list):
    b = numbers[0]
    for a in numbers:
        if a < b:
            b = a
    numbers.remove(b)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
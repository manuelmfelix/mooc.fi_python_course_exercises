# Write your solution here
def formatted(a: list):
    b = []
    for c in a:
        b.append(f"{c:.2f}")
    return b

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
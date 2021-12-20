# Write your solution here
def longest(strings: list):
    a = 0
    c = ""
    for b in strings:
        if len(b)>a:
            a = len(b)
            c = b
    return c


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
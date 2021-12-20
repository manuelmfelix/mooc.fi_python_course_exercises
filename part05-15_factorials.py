# Write your solution here
def factorials(n: int):
    a = 1
    c = {}
    for b in range(1,n+1):
        a *= b
        c[b] = a
    return c


if __name__ == "__main__":
    k = factorials(5)
    print(factorials(5))
    print(k)
    print(k[1])
    print(k[3])
    print(k[5])
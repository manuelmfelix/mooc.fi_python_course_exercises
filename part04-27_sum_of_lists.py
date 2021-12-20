# Write your solution here
def list_sum (a: list, b: list):
    c=[]
    d = 0
    e = 0
    while d < len(a):
        e = a[d]+b[d]
        d += 1
        c.append(e)
    return c

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
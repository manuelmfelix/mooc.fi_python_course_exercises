# Write your solution here
def invert(dictionary: dict):
    a = list(dictionary.keys())
    #print(a)
    b = list(dictionary.values())
    #print(b)
    c = {}
    for i in range(len(a)):
        c[b[i]]=a[i]
    print(c)

if __name__ == "__main__":
    invert({1: 10, 2: 20, 3: 30})
    #print(s)
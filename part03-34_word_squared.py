# Write your solution here
def squared(x,y):
    a = 0
    b = 1
    c = 0
    #print(len(x))
    while b <= y:
        d = ""
        e = 0
        while e < y:
            if c >= len(x):
                c=0
            d += x[c]
            c += 1
            e += 1
        print(d)
        b += 1
 # Testing the function
if __name__ == "__main__":
    squared("manuel",3)
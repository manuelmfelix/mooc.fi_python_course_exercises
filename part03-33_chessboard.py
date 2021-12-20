# Write your solution here
def chessboard(x):
    a = 1
    b = 1
    while b <= x:
        c = 1
        d = ""
        if b%2 == 0:
            a = 0
        else:
            a = 1
        while c <= x:
            d += str(a)
            if a == 1:
                a=0
            else:
                a=1
            c += 1
        print(d)
        b += 1


# Testing the function
if __name__ == "__main__":
    chessboard(4)

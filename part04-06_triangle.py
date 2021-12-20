# Copy here code of line function from previous exercise
def line(x,y):
    print(y[0]*x)

def triangle(size):
    # You should call function line here with proper parameters
    b=1
    while b<=size:
        line(b,"#")
        b += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

# Copy here code of line function from previous exercise
def line(x,y):
    print(y[0]*x)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    b=0
    while b<size:
        line(size, "#")
        b +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

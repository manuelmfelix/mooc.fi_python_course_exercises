# Copy here code of line function from previous exercise
def line(x,y):
    print(y[0]*x)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    b=0
    while b<height:
        line(10, "#")
        b +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)

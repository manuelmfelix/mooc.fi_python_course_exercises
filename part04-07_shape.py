# Copy here code of line function from previous exercise and use it in your solution
def line(x,y):
    print(y[0]*x)

def shape(width,s1,height,s2):
    b=1
    while b<=width:
        line(b,s1)
        b += 1
    a=1
    while a<=height:
        line(width, s2)
        a +=1
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
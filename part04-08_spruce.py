# Write your solution here
def spruce(size):
    print("a spruce!")
    a = 1
    while a<=size:
        b = int(a*2-1)
        c = int(((size*2-1)-b)/2)
        print(c*" "+b*"*"+c*" ")
        a +=1
    a = 1
    b = int(a*2-1)
    c = int(((size*2-1)-b)/2)    
    print(c*" "+b*"*"+c*" ")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(10)
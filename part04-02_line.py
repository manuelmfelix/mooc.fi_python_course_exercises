# Write your solution here
def line(x,y):
    if y !="":
        print(y[0]*x)
    else:
        print("*"*x)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")
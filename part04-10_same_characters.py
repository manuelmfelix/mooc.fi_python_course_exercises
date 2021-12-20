# Write your solution here
def same_chars(a,b,c):
    if b>len(a)-1 or c>len(a)-1:
        return False
    elif (b or c)<=0:
        return False

    if a[b]==a[c]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))
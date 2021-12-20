# Write your solution here
def times_ten(start_index: int, end_index: int):
    newDic = {}
    for a in range(start_index,end_index+1):
        newDic[a]=a*10
    return newDic

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
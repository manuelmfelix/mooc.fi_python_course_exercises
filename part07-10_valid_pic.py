# Write your solution here
from datetime import *
from string import *

def is_it_valid(pic: str):
    if len(pic)>11:
        return False
    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    # if int(day) > 31 or int(month) > 12 or int(year) > datetime.now().year:
    #     return False
    century = pic[6]
    pi = pic[7:10]
    pi2 = day+month+year+pi
    control = pic[10]
    day = int(day)
    month=int(month)
    year=int(year)
    if century == "+":
        year += 1800
    elif century == "-":
        year += 1900
    elif century == "A":
        year += 2000
    else:
        return False
    
    try:
        if datetime(year,month,day) > datetime.now():
            return False
    except:
        return False

    cont = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    # a = (int(pic[0])+int(pic[1])+int(pic[2])+int(pic[3])+int(pic[4])+int(pic[5])+int(pic[7])+int(pic[8])+int(pic[9]))%31
    a = int(pi2)%31

    # print(len(cont))
    # print(a)
    # print(cont[a])

    if cont[a] != control:
        # print("haha")
        return False
    
    return True


if __name__ == "__main__":
    print(is_it_valid("080842-720N"))
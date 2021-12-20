# Write your solution here
from datetime import *
from csv import *

def final_points():

    file1 = open("start_times.csv")
    csvreader1 = reader(file1,delimiter=';')
    start_times=[]
    for a in csvreader1:
        start_times.append(a)

    file2 = open("submissions.csv")
    csvreader2 = reader(file2,delimiter=';')
    submissions=[]
    for a in csvreader2:
        submissions.append(a)
    
    finaldic = {}
    for a in start_times:
        student = a[0]
        start = datetime.strptime(a[1], "%H:%M")
        finish = start
        notafinal = 0
        estud = {}
        print(student,end=":")
        #q = 0
        #w = 0
        for b in submissions:
            if b[0] == student:
                #q += 1
                finish = datetime.strptime(b[3], "%H:%M")
                if finish-start < timedelta(hours=3):
                    #w += 1
                    if b[1] not in estud.keys():
                        estud[b[1]]=int(b[2])
                        print(f"not: {estud[b[1]]}")
                    else:
                        if int(estud[b[1]]) < int(b[2]):
                            estud[b[1]]=int(b[2])
                            print(f"in: {estud[b[1]]}")
                        
        for a in estud:
            notafinal += estud[a]
        finaldic[student]=notafinal
        #print(f"Q: {q}, W: {w}")
        print()
    return finaldic

if __name__ == "__main__":

    print(final_points())
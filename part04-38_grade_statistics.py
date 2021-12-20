# Write your solution here
def gradeEx(a: list):
    a[1] = int(int(a[1])/10)
    a = [int(a[0]),int(a[1])]
    return a

def inputValues():
    counter = 0
    grades = []
    finalGrades = []
    while True:
        values = input("Exam points and exercises completed: ")
        if values == "":
            break
        counter += 1
        a = values.split()
        a = gradeEx(a)
        sum = int(a[0])+int(a[1])
        grades.append(sum)
        finalGrades.append(grading2(a))
        listReturn = [grades,finalGrades]
    return listReturn

def grading2(a: list):
    b = 0
    if a[0]<10 or (a[0]+a[1])<15:
        b = 0
    elif (a[0]+a[1])<18:
        b = 1
    elif (a[0]+a[1])<21:
        b = 2
    elif (a[0]+a[1])<24:
        b = 3
    elif (a[0]+a[1])<28:
        b = 4
    else:
        b = 5
    return b

def statAve(grades: list):
    print("Statistics:")
    count = len(grades)
    suma = sum(grades)
    average = suma/count
    print(f"Points average: {average}")

    return

def statPos(grades: list):
    count = len(grades)
    a = sum(x > 0 for x in grades)
    positive = float((a/count)*100)
    print(f"Pass percentage: {positive:.1f}")


def gradeDist(a: list):
    list = [5,4,3,2,1,0]
    c = 0
    print("Grade distribution:")
    while c < len(list):
        print(f"  {list[c]}:","*"*a.count(list[c]))
        c += 1
    return

results = inputValues()
grades = results[0]
newGrades = results[1]
statAve(grades)
statPos(newGrades)
gradeDist(newGrades)

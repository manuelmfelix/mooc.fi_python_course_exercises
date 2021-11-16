# Write your solution here

def add_student(database: dict, name: str):
    database[name] = []

def print_student(database: dict, name: str):
    if name in database.keys():
        if database[name] == []:
            print(f"{name}:\n no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(database[name])} completed courses:")
            b = 0
            c = 0
            for a in database[name]:
                print(" ",a[0],a[1])
                b += int(a[1])
                c += 1
            print(f" average grade {b/c}")
    else:
        print(f"{name}: no such person in the database")

def add_course(database: dict, name: str, course: tuple):
    b = 0
    if course[1] == 0:
        b = 1
    for a in database[name]:
        if course[0] == a[0] and course[1]<a[1]:
            b = 1
        if course[1]>a[1]:
            database[name].remove(a)
            
    if b == 0:
        database[name].append(course)
    

def summary(database: dict):
    courses,average,c,most,best,count = 0,0,0,0,0,0
    studentMost,studentAve,studentCheck = "","",""
    for b in database.keys():
        studentCheck = b
        count += 1
        for a in database[b]:
            c += int(a[1])
            courses += 1
            average = c/courses
        if most < courses:
            most = courses
            studentMost = studentCheck
        if best < average:
            best = average
            studentAve = studentCheck

    print(f"students {count}")
    print(f"most courses completed {most} {studentMost}")
    print(f"best average grade {best} {studentAve}")
        


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)
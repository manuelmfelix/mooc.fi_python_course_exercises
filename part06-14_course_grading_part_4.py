# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam Points: ")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}".strip()

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        #print("len: ",parts[7])
        parts[len(parts)-1].strip()
        #print(len(parts)-1)
        a = 7
        c=[]
        for b in range(1,a+1):
            c.append(int(parts[b].strip()))
        exercises[parts[0]] = c

exam = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        #print("len: ",parts[7])
        parts[len(parts)-1].strip()
        #print(len(parts)-1)
        a = 3
        c=[]
        for b in range(1,a+1):
            c.append(int(parts[b].strip()))
        exam[parts[0]] = c

info = []
with open(course_info) as new_file:
    for line in new_file:
        if line != "\n":
            line = line.strip()
            line = line.split(":")
        info.append(line[1].strip())

title = f"{info[0]}, {info[1]} credits"
sep = len(title)*"="
print(title)
print(sep)

# print(students)
# print(exercises)
# print(exam)
name = "name"
exec_nbr = "exec_nbr"
exec_pts="exec_pts."
exm_pts="exm_pts."
tot_pts="tot_pts."
grade="grade"

cab = f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade}"

with open("results.txt", "w") as my_file:
    my_file.write(f"{title}\n")
    my_file.write(f"{sep}\n")
    my_file.write(f"{cab}\n")

print(cab)
counterstudents = 0
for id, name in students.items():
    if id in exercises:
        points1 = 0
        if id in exam:
            points1 = sum(exam[id])
        # print(sum(exercises[id]))
        # sum = sum(exercises[id])
        points2 = int(sum(exercises[id])/40*10)
        a = [points1,points2]
        b = 0
        if (a[0]+a[1])<15:
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

        final = f"{name:30}{sum(exercises[id]):<10}{points2:<10}{points1:<10}{points1+points2:<10}{b}"
        print(final)
        with open("results.txt", "a") as my_file:
            my_file.write(f"{final}\n")

        if counterstudents == 0:
            with open("results.csv", "w") as my_file:
                line = f"{id};{name};{b}"
                my_file.write(line+"\n")
                counterstudents += 1
        else:
            with open("results.csv", "a") as my_file:
                line = f"{id};{name};{b}"
                my_file.write(line+"\n")


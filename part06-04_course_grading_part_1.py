# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

# print(students.items())
# print(exercises)

for id, name in students.items():
    if id in exercises:
        # print(sum(exercises[id]))
        # sum = sum(exercises[id])
        print(f"{name} {sum(exercises[id])}")
# Write your solution here
from datetime import *


if False:
    file = input("Filename: ")
    date = input("Starting date: ")
    days = int(input("How many days: "))
else:
    file = "late_june.txt"
    date = "24.6.2020"
    dias = 5

print("Please type in screen time in minutes on each day (TV computer mobile):")

my_time = datetime.strptime(date, "%d.%m.%Y")

counter = 0

for i in range(dias):
    my_dias = timedelta(days=i)
    data = my_time+my_dias
    data = data.strftime("%d.%m.%Y")
    a = input(f"Screen time {data}: ")

    if counter == 0:
        with open(file,"w") as new_file:
            new_file.write(f"{a}\n")
            counter += 1
    else:
        with open(file,"a") as new_file:
            new_file.write(f"{a}\n")

print(f"Data stored in file {file}")

begin = my_time.strftime("%d.%m.%Y")
data2 = my_time+timedelta(days=dias-1)
end = data2.strftime("%d.%m.%Y")



print(f"Time period: {begin}-{end}")
print(f"Time period: {}")





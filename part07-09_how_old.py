# Write your solution here
from datetime import *

if True:
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
else:
    day = 10
    month = 4
    year = 1990

age = datetime(year, month, day)
mil = datetime(1999,12,31)
final = mil-age


if final.days > 0 :
    print(f"You were {final.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
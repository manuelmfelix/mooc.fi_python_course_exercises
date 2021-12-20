# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))
d = (b**2) - (4*a*c)

sol1 = (-b-sqrt(d))/(2*a)
sol2 = (-b+sqrt(d))/(2*a)

print(f"The roots are {sol1} and {sol2}")

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
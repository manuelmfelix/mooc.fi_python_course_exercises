# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        else:
            return self.sum

    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return self.sum/self.numbers
        
stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    a = int(input("Please type in integer numbers:"))
    if a == -1:
        break
    else:
        stats.add_number(a)
        if a%2==0:
            even.add_number(a)
        else:
            odd.add_number(a)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
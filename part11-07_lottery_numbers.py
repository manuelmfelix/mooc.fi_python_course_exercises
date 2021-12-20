# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, numberList: list):
        self._week = week
        self._numberList = numberList
        self._correct = 0
        
    def number_of_hits(self, numbers: list):
            return sum([1 if number in numbers else 0 for number in self._numberList])
            
    def hits_in_place(self, numbers):
        return [number if number in self._numberList else -1 for number in numbers]



if __name__ =='__main__':
    week8 = LotteryNumbers(2, [1,3, 5, 7, 9, 11, 13])
    my_numbers = [1,2, 5, 6, 9, 10, 11]
    
    print(week8.hits_in_place(my_numbers))
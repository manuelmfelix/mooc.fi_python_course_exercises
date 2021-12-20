import collections

class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counter = collections.Counter(my_list)
        # counter.values().index(max(counter.values()))
        return counter.most_common(1)[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        counter = collections.Counter(my_list)
        count = 0
        for a in counter.keys():
            if counter[a]>=2:
                count += 1
        return count



if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
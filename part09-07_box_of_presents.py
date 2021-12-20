
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Present: {self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.weight = 0

    def add_present(self, present: Present):
        self.weight += present.weight

    def total_weight(self):
        return self.weight



if __name__ == '__main__':
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
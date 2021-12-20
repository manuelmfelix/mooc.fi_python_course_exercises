class Item:

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

class Suitcase:

    def __init__(self, maxWeight: int):
        self.__maxWeight = maxWeight
        self.__itemList = []

    @property
    def itemList(self):
        return self.__itemList

    def __checkWeight(self):
        soma = 0
        for a in self.__itemList:
            soma += a.weight()
        return soma

    def add_item(self, item: Item):
        if item.weight() + self.__checkWeight() > self.__maxWeight:
            return
        else:
            self.__itemList.append(item)

    def print_items(self):
        for a in self.__itemList:
            print(a)
        return

    def weight(self):
        a = self.__checkWeight()
        return a

    def heaviest_item(self):
        item = self.__itemList[0]
        if len(self.__itemList) == 0:
            return None
        else:
            for a in self.__itemList:
                if a.weight() > item.weight():
                    item = a
        return item

    def __str__(self):
        if len(self.__itemList) == 1:
            return f"{len(self.__itemList)} item ({self.__checkWeight()} kg)"
        else:
            return f"{len(self.__itemList)} items ({self.__checkWeight()} kg)"

class CargoHold:

    def __init__(self, maxWeight: int):
        self.__maxWeight = maxWeight
        self.__suitList = []

    def __checkWeight(self):
        soma = 0
        for a in self.__suitList:
            soma += a.weight()
        return soma

    def add_suitcase(self, suit: Suitcase):
        if suit.weight() + self.__checkWeight() > self.__maxWeight:
            return
        else:
            self.__suitList.append(suit)

    def print_items(self):
        for b in self.__suitList:
            for a in b.itemList:
                print(a)
        return

    def __str__(self):
        if len(self.__suitList) == 1:
            return f"{len(self.__suitList)} suitcase, space for {self.__maxWeight - self.__checkWeight()} kg"
        else:
            return f"{len(self.__suitList)} suitcases, space for {self.__maxWeight - self.__checkWeight()} kg"

            


if __name__ == '__main__':

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
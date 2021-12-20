# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write your solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

def total_units(my_list: ShoppingList):
    a = 0
    for i in range(1,my_list.number_of_items()+1):
        a += my_list.amount(i)
    return a

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    # print(my_list.number_of_items())

    print(total_units(my_list))

# Write your solution here
import fractions

def fractionate(amount: int):
    b = []
    for a in range(amount):
        b.append(fractions.Fraction(1,amount))
    return b


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))


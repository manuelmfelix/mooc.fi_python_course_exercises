# Write your solution here
def new_person(name: str, age: int):
    b = name.split()

    if name == "" or len(b)<2 or len(name)>40 or age<0 or age>150:
        raise ValueError("The input was invalid.")

    a = (name,age)
    return a

if __name__ == "__main__":
    print(new_person("manuel felix",32))

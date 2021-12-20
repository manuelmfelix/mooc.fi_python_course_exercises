# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
        self.height = 0

    def add(self, person: Person):
        self.people.append(person)
        self.height += person.height

    def is_empty(self):
        return len(self.people) == 0

    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, and their combined height is {self.height} cm")
        for a in self.people:
            print(f"{a.name} ({a.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None
        else:
            short = self.people[0]
            h = self.people[0].height
            for a in self.people:
                if h > a.height:
                    short = a
                    h = a.height
            return short

    def remove_shortest(self):
        shortest = self.shortest()
        if len(self.people) == 0:
            return None
        else:
            for a in self.people:
                if a.name == shortest.name:
                    self.height -= a.height
                    self.people.remove(a)
                    return a
            


if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
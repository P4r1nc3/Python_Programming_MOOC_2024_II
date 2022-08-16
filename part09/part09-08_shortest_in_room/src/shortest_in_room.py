
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def get_total_height(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        return total_height

    def print_contents(self):
        final_str = f'There are {len(self.persons)} persons in the room, and their combined height is {self.get_total_height()} cm\n'
        for person in self.persons:
            final_str += f'{person.name} ({person.height} cm)\n'
        final_str = final_str.strip()
        print(final_str)

    def shortest(self):
        if self.is_empty():
            return None

        shortest = self.persons[0]
        for person in self.persons:
            if shortest.height > person.height:
                shortest = person
        
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        
        shortest = self.shortest()
        shortest_index = self.persons.index(shortest)
        return self.persons.pop(shortest_index)
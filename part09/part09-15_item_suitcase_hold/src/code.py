# Write your solution here:
class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'

class Suitcase:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__items = []
    
    @property
    def items(self):
        return self.__items

    def add_item(self, item: Item):
        # self.__items.append(item)
        new_possible_weight = self.weight() + item.weight()
        if new_possible_weight <= self.__max_weight:
            self.__items.append(item)
    
    def weight(self):
        total_weight = 0
        for item in self.__items:
            total_weight += item.weight()
        return total_weight
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def is_empty(self):
        return len(self.__items) == 0

    def heaviest_item(self):
        if self.is_empty():
            return None
        
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

    def __str__(self):
        if len(self.__items) == 1:
            items_str = 'item'
        else:
            items_str = 'items'
        return f'{len(self.__items)} {items_str} ({self.weight()} kg)'

class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        possible_total_weight = self.__weight() + suitcase.weight()
        if possible_total_weight <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def __weight(self):
        total_weight = 0
        for suitcase in self.__suitcases:
            total_weight += suitcase.weight()
        return total_weight

    def is_empty(self):
        return len(self.__suitcases) == 0

    def print_items(self):
        if self.is_empty():
            print('')
        else:
            for suitcase in self.__suitcases:
                suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
            suitcases_str = 'suitcase'
        else:
            suitcases_str = 'suitcases'
        return f'{len(self.__suitcases)} {suitcases_str}, space for {self.__max_weight-self.__weight()} kg'


if __name__ == "__main__":
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
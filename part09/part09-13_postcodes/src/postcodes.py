# Add the requested members to the class below:

class City:

    postcodes = {
        'Helsinki' : '00100',
        'Turku' : '20100',
        'Tampere' : '33100',
        'Rovaniemi' : '96100',
        'Oulu' : '90100'
    }


    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"

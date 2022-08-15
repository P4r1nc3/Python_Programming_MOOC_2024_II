# WRITE YOUR SOLUTION HERE:

class Pet:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.description})"

class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name
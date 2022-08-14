# Write your solution here

class Checklist:
    def __init__(self, header : str, entries : list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id : str, balance : bool, discount : int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model : str, length : float, max_speed : int, bidirectional : bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed 
        self.bidirectional = bidirectional
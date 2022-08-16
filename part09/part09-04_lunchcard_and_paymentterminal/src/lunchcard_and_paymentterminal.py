# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_price = 2.50
        if payment >= lunch_price:
            self.funds += lunch_price
            self.lunches += 1
            return payment - lunch_price
        else:
            return payment

    def eat_special(self, payment: float):
        special_lunch_price = 4.30
        if payment >= special_lunch_price:
            self.funds += special_lunch_price
            self.specials += 1
            return payment - special_lunch_price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_price = 2.50
        sold = card.subtract_from_balance(lunch_price)
        if sold:
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        special_lunch_price = 4.30
        sold = card.subtract_from_balance(special_lunch_price)
        if sold:
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
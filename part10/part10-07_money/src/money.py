# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __get_money(self):
        return self.__euros + (self.__cents/100)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: 'Money'):
        return self.__get_money() == another.__get_money()

    def __lt__(self, another: 'Money'):
        return self.__get_money() < another.__get_money()

    def __gt__(self, another: 'Money'):
        return self.__get_money() > another.__get_money()

    def __ne__(self, another: 'Money'):
        return self.__get_money() != another.__get_money()

    def __add__(self, another: 'Money'):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        if total_cents >= 100:
            total_euros += 1
        total_cents = total_cents % 100
        new = Money(total_euros, total_cents)
        return new

    def __sub__(self, another: 'Money'):
        if (self.__get_money() < another.__get_money()):
            raise ValueError('a negative result is not allowed')
        total_euros = self.__euros - another.__euros
        if self.__cents >= another.__cents:
            total_cents = self.__cents - another.__cents
        else:
            total_euros -= 1
            total_cents = self.__cents + (100-another.__cents)
        new = Money(total_euros, total_cents)
        return new

# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'
    
    def __lt__(self, another: 'SimpleDate'):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year:
            if self.__month < another.__month:
                return True
            elif self.__month == another.__month:
                if self.__day < another.__day:
                    return True

        return False

    def __gt__(self, another: 'SimpleDate'):
        if self.__eq__(another) == False and self.__lt__(another) == False:
            return True
        return False

    def __eq__(self, another: 'SimpleDate'):
        if self.__day == another.__day and \
            self.__month == another.__month and \
                self.__year == another.__year:
                return True
        return False

    def __ne__(self, another: 'SimpleDate'):
        if self.__eq__(another) == False:
            return True
        return False

    def __convert_curr_date_to_days(self):
        return ((self.__year-1)*12*30) + ((self.__month-1)*30) + self.__day

    def __add__(self, days_to_add: int):
        days = self.__convert_curr_date_to_days()
        days += days_to_add
        year = (days//360)+1
        month = ((days//30)%12)+1
        day = days%30
        return SimpleDate(day, month, year)

    def __sub__(self, another: 'SimpleDate'):
        curr_days = self.__convert_curr_date_to_days()
        another_days = another.__convert_curr_date_to_days()
        return abs(curr_days - another_days)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)
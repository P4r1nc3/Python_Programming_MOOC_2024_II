# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest_count = 1
        greatest_count_element = my_list[0]
        for element in my_list:
            if my_list.count(element) > greatest_count:
                greatest_count = my_list.count(element)
                greatest_count_element = element
        return greatest_count_element
    
    @classmethod
    def doubles(cls, my_list: list):
        my_set = set(my_list)
        count_at_least_double = 0
        for element in my_set:
            if my_list.count(element) >= 2:
                count_at_least_double += 1
        return count_at_least_double


    if __name__ == "__main__":
        numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
        print(ListHelper.greatest_frequency(numbers))
        print(ListHelper.doubles(numbers))
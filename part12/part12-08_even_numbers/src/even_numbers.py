# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning
    # return [a for a in range(beginning,maximum+1) if a%2==0]
    while number <= maximum:
        if number%2 == 0:
            yield number
        number += 1

if __name__=='__main_':
    numbers = even_numbers(2, 10)
    print(numbers)
    for number in numbers:
        print(number)
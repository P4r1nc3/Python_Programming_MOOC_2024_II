from random import choice

def word_generator(letters: str, length: int, amount:int):
    return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
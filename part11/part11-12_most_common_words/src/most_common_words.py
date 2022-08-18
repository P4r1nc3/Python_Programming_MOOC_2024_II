# WRITE YOUR SOLUTION HERE:
import string

def strip_special_chars(word: string):
    final_word = ''
    for character in word:
        if character not in string.punctuation:
            final_word += character
    return final_word

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        all_words = []
        for line in file:
            words = line.strip().split(' ')
            for word in words:
                all_words.append(strip_special_chars(word))
        word_count = {word : all_words.count(word) for word in all_words}
        return {word: count for word, count in word_count.items() if count >= lower_limit}    
# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string : str, forbidden : str):
        filtered = [letter for letter in string if letter not in forbidden]
        return ''.join(filtered)

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
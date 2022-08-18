def balanced_brackets(my_string: str):
    my_string = ''.join([character for character in my_string if character in '()[]'])

    if len(my_string) == 0:
        return True

    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)

# def balanced_brackets(my_string: str):
#     if len(my_string) == 0:
#         return True
#     if not (my_string[0] == '(' and my_string[-1] == ')'):
#         return False

#     # remove first and last character
#     return balanced_brackets(my_string[1:-1])



def balanced_brackets(my_string: str):
    new_string = "".join([character for character in my_string if character in "[()]"])
    
    if len(new_string) == 0:
        return True
    if not (new_string[0] == '(' and new_string[-1] == ')' or new_string[0] == '[' and new_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(new_string[1:-1])


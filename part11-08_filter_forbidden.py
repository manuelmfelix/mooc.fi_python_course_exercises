# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return " ".join(["".join(character for character in word if character not in forbidden) for word in string.split() if word not in forbidden])

if __name__ =='__main__':
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
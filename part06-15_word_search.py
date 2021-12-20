# Write your solution here
import fnmatch

def find_words(search_term: str):
    wordcheck = []

    with open("words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            wordcheck.append(line)

    search_term=search_term.replace(".","?")

    filtered = fnmatch.filter(wordcheck, search_term)

    return filtered


if __name__ == "__main__":
    print(find_words("ca."))


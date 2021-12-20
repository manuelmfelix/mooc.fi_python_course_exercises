# Write your solution here
import string

def separate_characters(mystring: string):
    a,b,c="","",""

    for n in mystring:
        if n in string.ascii_letters:
            a += n

    for n in mystring:
        if n in string.punctuation:
            b += n

    for n in mystring:
        if n not in string.punctuation and n not in string.ascii_letters:
            c += n

    return (a,b,c)
    

if __name__ == "__main__":
    parts = separate_characters("a. s, d: f; g* ")
    print(parts)
    print(parts[0])
    print(parts[1])
    print(parts[2])
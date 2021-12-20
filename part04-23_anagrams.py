# Write your solution here
def anagrams(a,b):
    return sorted(a)==sorted(b)

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
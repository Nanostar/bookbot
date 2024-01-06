def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"-- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    num_letters = get_letter_count(text)
    sorted_letters = dict_to_list(num_letters)
    for items in sorted_letters:
        if items["char"].isalpha():
            print(f"The '{items["char"]}' character was found {items["num"]} times")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    lowertext = text.lower()
    letterDict = {}
    for s in lowertext:
        if s in letterDict.keys():
            letterDict[s] = letterDict[s] + 1
        else:
            letterDict[s] = 1
    return letterDict

def dict_to_list(letterDict):
    sorted_list = []
    for c in letterDict:
        sorted_list.append({"char": c, "num": letterDict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()
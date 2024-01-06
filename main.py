def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_letters = get_letter_count(text)
    
    for [i,j] in num_letters:
        if i.isalpha():
            print(f"The '{i}' character was found {j} times")



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
    letterList = list(letterDict.items())
    letterList.sort()
    return letterList


main()
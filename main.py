import sys
from stats import get_num_words, get_num_chars, sort_dictionary

def get_book_text(file_path):
    print(file_path)
    with open(file_path, "r") as b:
        book = b.read()

    return book

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book = get_book_text(path_to_book)

    report = f'''
============ BOOKBOT ============
Analyzing book found at {path_to_book}...
----------- Word Count ----------
Found {get_num_words(book)} total words
--------- Character Count -------
'''

    for c in sort_dictionary(get_num_chars(book)):
        if not c["char"].isalpha():
            continue
        report += (f"{c["char"]}: {c["num"]}\n")

    report += "============= END ==============="
    print(report)

main()
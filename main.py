from stats import get_num_words

def get_book_text(book_location):
    with open(book_location) as book:
        return book.read()

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")

main()
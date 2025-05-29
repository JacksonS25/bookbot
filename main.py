def get_book_text(book_location):
    with open(book_location) as book:
        return book.read()

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
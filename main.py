def get_book_text(book_location):
    with open(book_location) as book:
        return book.read()

def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")

main()
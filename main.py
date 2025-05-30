import sys
from stats import get_num_words, count_characters, sort_character_count

def get_book_text(book_location):
    with open(book_location) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    character_count = count_characters(book)
    sorted_character_count = sort_character_count(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_character_count:
        if i["ch"].isalpha() == True:
            print(f"{i["ch"]}: {i["num"]}")
    print("============= END ===============")


main()
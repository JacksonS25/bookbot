def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def count_characters(book_text):
    character_count = {}
    for word in book_text:
        letters = word.split()
        for letter in letters:
            if letter.lower() in character_count:
                character_count[letter.lower()] += 1
            else:
                character_count[letter.lower()] = 1
    return character_count

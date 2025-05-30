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

def sort_on(dict):
    return dict["num"]

def sort_character_count(character_count):
    count_dict_list = []
    for character in character_count:
        count_dict_list.append({"ch": character, "num": character_count[character]})
    count_dict_list.sort(reverse=True, key=sort_on)
    return count_dict_list
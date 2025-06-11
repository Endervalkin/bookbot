character_dict = {}
character_list = []


def get_word_count(book_text):
	# counts the number of words in the text
	words = book_text.split()
	return len(words)

def get_char_count(book_text):
	# counts the number of characters in the text
    lower_text = book_text.lower()
    for char in lower_text:
        if char.isalpha() or char.isspace() or char in ".,!?;:'\"-":
            # Convert character to lowercase for case-insensitive counting
            # Only count alphabetic characters and spaces
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict

def sort_on(d):
     return d["num"]

def sort_characters(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
     

     
    

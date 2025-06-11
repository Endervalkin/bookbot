import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import (
    get_word_count, 
	get_char_count, 
	sort_characters
)
# word_count counts the number of words in the document defined in path to file.
# char_count counts the number of characters in the document defined in path to file and returns as a dictionary.

def main():
	path_to_file = sys.argv[1]
	book_text = get_book_text(path_to_file)
	word_count = get_word_count(book_text)
	character_dict = get_char_count(book_text)
	sort_characters_list = sort_characters(character_dict)
	print_report(path_to_file, word_count, sort_characters_list)

	
def get_book_text(path_to_file):
	with open(path_to_file) as f:
	# opens the file frankenstein.txt
		return f.read()
	


def print_report(path_to_file, word_count, sort_characters_list):
	# prints the report of the book
	book_text = get_book_text(path_to_file)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/" + path_to_file)
	print("----------- Word Count ----------")
	print(f"Found", word_count, "total words.")
	print("----------- Character Count ----------")
	for item in sort_characters_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")


main()
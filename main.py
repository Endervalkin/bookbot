path_to_file = "/mnt/c/bookbot/books/frankenstein.txt"
def get_book_text(f):
	with open(path_to_file) as f:
	# opens the file frankenstein.txt
		book_text = f.read()
	
	return book_text

from stats import word_count
# This function counts the number of words in the document defined in path to file.

def main():
	book_text = get_book_text(path_to_file)
	print(word_count(book_text), "words found in the document.")

main()


path_to_file = "/mnt/c/bookbot/books/frankenstein.txt"
def get_book_text(f):
	with open(path_to_file) as f:
	# opens the file frankenstein.txt
		return f.read()
		

def main():
	book_text = get_book_text(path_to_file)
	print(book_text)

main()


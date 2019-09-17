import re
def is_palindrome(string):
	if len(string) == 0:
		return False
	if len(string) == 1:
		return True

	else:
		start = 0
		end = len(string)-1
		while start<end:
			if string[start] != string[end]:
				return False
			start += 1
			end -= 1
	return True

#print(is_palindrome("radr"))

def map_length(input_words):
	words_list = input_words.split()
	return [len(word) for word in words_list]

#input_words = input("Please enter the words separated by space:\n")
#print(map_length(input_words))

def search_word(text_file):
	file_name = "./" + text_file
	f = open(file_name, 'r')
	pattern = 'Darshan'
	if re.search(pattern, f.read()):
		print("Match Found")
	else:
		print("No match found")

search_word("abc.txt")

def remove_duplicates(input_words_without_space):
	list_words = input_words_without_space.split()
	if len(list_words) == 0:
		return None
	
	if len(list_words) == 1:
		return list_words

	else:
		return list(set(list_words))

input_words = input("Please enter the words separated by space:\n")
print(remove_duplicates(input_words))

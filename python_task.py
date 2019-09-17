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

input_words = input("Please enter the words separated by space:\n")
print(map_length(input_words))

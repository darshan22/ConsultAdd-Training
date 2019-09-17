import re

class python_task():
	def __init__(self):
		pass

	def is_palindrome(self, string):
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


	def map_length(self, input_words):
		words_list = input_words.split()
		if len(words_list) == 0:
			return None
		else:
			return [len(word) for word in words_list]


	def search_pattern(self, text_file, pattern):
		file_name = "./" + text_file
		f = open(file_name, 'r')
		if re.search(pattern, f.read()):
			print("Match Found")
		else:
			print("No match found")


	def remove_duplicates(self, input_words_without_space):
		list_words = input_words_without_space.split()
		if len(list_words) == 0:
			return None
		
		if len(list_words) == 1:
			return list_words

		else:
			return list(set(list_words))

def main():
	task = python_task()    #create an instance of class.
	flag = True
	while flag:     #loop for repetetive menu. and accept a choice from user.
		print("*************************MAIN MENU******************************")
		choice = input("""
		       Please select from the options below. 
		       1. CHECK FOR PALINDROME
		       2. CHECK THE LENGTH OF WORDS
		       3. SEARCH FOR PATTERN IN THE DOCUMENT
		       4. REMOVE THE DUPLICATES FROM THE LIST
		       5. CANCEL\n""")

		if choice.isalpha() or len(choice)==0:			
			print("Invalid Entry. Please Try Again!")
			main()

		if int(choice) == 1:
			string = input("Please enter the string")
			print(task.is_palindrome(string)):\n

		elif int(choice) == 2:
			words_without_space = input("Please enter the words with space in it:\n")
			print(task.map_length(words_without_space))

		elif int(choice) == 3:
			file_name = input("Please enter the name of the text file present in your current directory with .txt extension:\n")
			pattern = input("Please enter the name to find:\n")
			task.search_pattern(file_name, pattern)

		elif int(choice) == 4:
			input_list = input("Please enter the words in the list with spaces:\n")
			print(task.remove_duplicates(input_list))

		elif int(choice) == 5:
			print("Thank you!")
			flag = False    
	    
if __name__ == "__main__":
	main()

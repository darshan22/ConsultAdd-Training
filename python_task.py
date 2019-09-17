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

print(is_palindrome("radr"))

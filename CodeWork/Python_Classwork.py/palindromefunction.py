def reverse_string(word):
	reverse_word = ''
	for number in range(len(word)-1, -1, -1):
		reverse_word += word[number]

	return reverse_word


def palindrome(number):
	return str(number) == reverse_string(str(number))

print(palindrome("hannah"))
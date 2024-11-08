def palindrome (number):
	return "it's a palindrome" if str(number) == str(number)[::-1] else "print it's not a palindrome"
print(palindrome(number))
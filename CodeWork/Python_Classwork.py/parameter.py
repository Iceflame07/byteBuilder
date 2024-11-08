'''
Def the function that will enter word and save it
Print the word in reversed order and save it
'''

def reverse_string(word):
	reverse_word = ''
	for number in range(len(word)-1, -1, -1):
		reverse_word += word[number]

	return reverse_word

print(reverse_word("Cohort"))
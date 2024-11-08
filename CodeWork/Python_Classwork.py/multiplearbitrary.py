def multiply_number(*number):
	total = 0
	for number in number:
	    total *= number
	return total
print(multiply_number(2, 4, 6, 8))
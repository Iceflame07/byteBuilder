'''
Prompt the computer to create a program of a given number and save
Prompt the computer to create a multiplication table and save
Prompt the computer to enter 1 to 10 a given multiplication and save
'''

number = int(input("Enter integer: "))

for i in range(1, 11):
	number *= i
	print(number + "x" + i + '=' + number * i) 
'''
prompt the user to input the first number and save
prompt the user to input the second number and save
prompt the user to input the third number and save
prompt the computer to display them in increasing numbers and save
'''

number1 = int(input("Enter the first_number:"))
number2 = int(input("Enter the second_number:"))
number3 = int(input("Enter the third_number:"))

total = number1 + number2 + number3
for number in range(total):
 total += number

print(number)
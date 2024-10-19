'''
prompt the user to input an array of numbers and save
prompt the computer to initialize a row in ascending and descending order and save
prompt the computer to loop through the numbers and save
prompt the computer to multiply the element in the third row and save
prompt the computer to double the elements and save
display the result
'''

row = int(input("Enter numbers in row:"))
column = int(input("Enter numbers in column:"))
array = [5,2,7,1,8,2] *row
array.sort ()
print(array)

for i in range(row):
	for j in range(column):
		print(f' {i * j}', end = " ")
	print()


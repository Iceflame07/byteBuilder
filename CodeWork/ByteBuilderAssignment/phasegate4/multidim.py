'''
prompt the user to input two digits and column and save as in input
prompt the user to generate a two dimensional array and save
prompt the computer to store the element value in the i-th row and j-th column and save
prompt the computer to store it in an array as i*j and save
display result and save
'''

row = int(input("Enter numbers in row:"))
column = int(input("Enter numbers in column:"))
array = [[0] * column]*row


for i in range(row):
	for j in range(column):
		print(f' {i * j}', end = " ")


'''
for index in range(len(array)):
'''
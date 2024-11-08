'''
Prompt the user for deposit amount and save
Prompt the user to input options 1 or 2 for deposit or withdrawal and save
Prompt the computer
Prompt the computer to increase amount if 1 is deposit and save
Prompt the computer to decrease amount if 2 is withdrawal and save
print the balance and save
'''

def eskay_bank(amount, user_input):

 balance = 0
user_input = input(menu)
menu = """
Enter option 1 to deposit
or 2 to withdraw
3 to check balance
0 to end: """

user_input = input(menu)

while user_input !='0':
	if user_input == '1':
		amount = float(input("Enter amount: "))
		balance += amount
	elif user_input == '2':
		amount = float(input("Enter amount: "))
		if balance < amount:
 			print("insufficient funds")
		else:
			balance -= amount
	elif user_input == '3':
		print("your balance is ", balance)

	user_input = input(menu)
	print("Thank you for using eskay bank!!!")

def eskay_bank(amount, user_option):
	balance = 0

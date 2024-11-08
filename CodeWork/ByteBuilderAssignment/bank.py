'''
Prompt the user for deposit amount input and save
Prompt the user for withdrawal amount input and save
Prompt the computer to enter the transaction log and save
Prompt the computer to input balance and save
'''

deposit_amount = int(input("Enter deposit amount:$"))

withdrawal_amount = float(input("Enter withdrawal amount:$"))

balance = deposit_amount - withdrawal_amount

print(balance)
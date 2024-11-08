'''
Prompt the user for deposit amount and collect the amount to input and save
Prompt the user to add new deposit balance and save
Prompt the user for withdrawal amount input and save
Prompt the user for transfer float and save
Prompt the computer to input balance and save
Prompt the computer to input thank you for banking with us and save
'''

deposit_amount = float(input("Enter deposit amount:$"))

new_deposit = float(input("Enter new deposit:$"))

withdrawal_amount = float(input("Enter withdrawal amount:$"))

transfer_amount = float(input("Enter transfer amount:$"))

balance = deposit_amount - withdrawal_amount - transfer_amount

print(balance)

print("Thank you for banking with us!!!")
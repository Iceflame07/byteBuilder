'''
Prompt user to enter the principal amount
Prompt user to enter the annual interest rate %
If(5%) divide the answer 
Convert annual interest rate to decimal 
Convert annually to monthly
Prompt user for duration
Calculate the duration by 12 
Using the formula to give us our duration in month
Use answers for your calculations
Display the final result
'''

principalamount = int(input("Enter the principalamount: "))
annualinterest = int(input("Enter the annual interest: "))
duration = int(input("Enter the duration in years as payment: "))
 
PERCENTAGE = 100

MONTH = 12

monthlyinterest = annualinterest / PERCENTAGE / MONTH

monthlyduration = duration * MONTH

monthlypaymentfirststep =  (1 + monthlyinterest) ** monthlyduration

monthlypaymentsecondstep = monthlyinterest * monthlypaymentfirststep

monthlypaymentthirdstep = ((1 + monthlyinterest) ** monthlyduration) - 1

monthlypayment = principalamount * (monthlypaymentsecondstep / monthlypaymentthirdstep)

print("Monthly Payment is $",monthlypayment)
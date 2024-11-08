def convert_currency(dollar_amount):
    RATE = 1550
    if type(dollar_amount) not in (Int, float)
	return "Invalid Input"
    if dollar_amount < 0:
	raise ValueError("Invalid amount")
   return round(dollar_amount * RATE, 2)



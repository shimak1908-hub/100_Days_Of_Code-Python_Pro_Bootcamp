print("Welcome to the tip calcualator!")
t_bill = float(input("What was the total bill? $"))
tip_perc = int(input("How much tip would you like to give? 10%, 12%, 15% "))
ppl = int(input("How many people to split the bill "))
amt = (t_bill + (t_bill * tip_perc / 100)) / ppl
print( F"Each person should pay: {amt :.2f}")



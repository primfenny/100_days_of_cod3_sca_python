print("welcome to the tip calculator!")
bill = float(input("what was the total bil? $"))
#change bill int a number format to run the math operation!
percent = int(input("what percentage do you want to give? 10, 12,or 15?"))
people = int(input("how many people to split the bill? "))
bill_tip = percent / 100 * bill + bill
print (bill_tip)
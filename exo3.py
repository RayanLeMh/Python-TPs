Amount = float(input("Total amount: "))
numItems = int(input("Number of items: "))
DayOfWeek = str(input("Day of the week: ")).capitalize()

if DayOfWeek in ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]:
    Amount = Amount - Amount * 0.1
elif DayOfWeek in ["Saturday" , "Sunday"]:
    Amount = Amount - Amount * 0.2
else:
    print("Please write the day properly")

if numItems>5:
    Amount = Amount - Amount * 0.05 

print("Total price after discount: ", Amount, " dinars")


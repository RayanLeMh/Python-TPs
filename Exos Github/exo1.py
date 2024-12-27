Name = str(input("Please enter your name: "))

if Name.upper() != "VIP":
    NumTickets = int(input("How many tickets would you like to buy? "))
    TotalCost = NumTickets * 15.50
    print("The total cost is ", TotalCost, ", Enjoy your tickets!")
else:
    print("Enjoy the show for free!")
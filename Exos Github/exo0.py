people= int(input("how many people need a ride? "))

fit = int(input("how many people fit in one taxi? "))

taxi = people / fit

if taxi - int(taxi) == 0:
    print("you need", int(taxi), "taxi")
else:
    print("you need", int(taxi)+1, "taxi")
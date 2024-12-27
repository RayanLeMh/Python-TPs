FirstPersonAge = int(input("Please type in the age of the first person: "))
SecondPersonAge = int(input("Please type in the age of the second person: "))

if(FirstPersonAge>SecondPersonAge):
    print("The older age is: ",FirstPersonAge)
elif(SecondPersonAge>FirstPersonAge):
    print("The older age is: ",SecondPersonAge)
elif(FirstPersonAge==SecondPersonAge):
    print("Both people are the same age!")
else:
    print("Enter a correct age!")
    
print("input:")
yearInput = int(input("Please type in a year:"))
if (yearInput % 4 == 0):
    print("output:")
    print("That year is a leap year.")
elif(yearInput % 100 ==0):
    if(yearInput % 400 ==0):
        print("output:")
        print("That year is a leap year.")
else:
        print("output:")
        print("That year is not a leap year.")
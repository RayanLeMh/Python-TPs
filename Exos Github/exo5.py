print("Runner 1:")
firstRunnerName = str(input("Name: "))
firstRunnerTime = float(input("Time (in seconds): "))
print("Runner 2:")
secondRunnerName = str(input("Name: "))
secondRunnerTime = float(input("Time (in seconds): "))

if(firstRunnerTime>secondRunnerTime):
    print("The faster runner is: ",firstRunnerName)
elif(firstRunnerTime<secondRunnerTime):
    print("The faster runner is: ",secondRunnerName)
elif(firstRunnerTime==secondRunnerTime):
    print(firstRunnerName, "and",secondRunnerName,"have the same time")

while True:
    try:
        
        N = int(input("Enter a positive integer: "))
        
        
        if N > 0:
            break  
        else:
            print("Please enter a positive integer.")
    except ValueError:
        
        print("Invalid input. Please enter a valid integer.")

for num in range(-N, N + 1):
    if num != 0:
        print(num)
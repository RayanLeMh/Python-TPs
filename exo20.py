import statistics

user_list = []

def save_to_file(list):
    file_path = input("Enter the path to save the file: ")
    with open(file_path, "w") as file:
        for num in sorted(list):
            file.write(str(num) + "\n")
    print(f"List saved to {file_path}.")

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    else:
        user_list.append(number)
        
        print("Current list:", user_list)
        
        sorted_list = sorted(user_list)
        print("Sorted list:", sorted_list)
        
        sorted_list.reverse()
        print("List in descending order:", sorted_list)

if user_list:
    print("List mean:", statistics.mean(user_list))
    print("List median:", statistics.median(user_list))
else:
    print("No numbers were entered.")

save = input("Do you want to save the list to a file (y/n): ")
if save.lower() == 'y':
    save_to_file(user_list)
else:
    exit()

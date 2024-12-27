cities = []

print("Enter the name of the city to check it population number, if u want to stop just type (stop)")

while True:
    city = input("Enter the name of the city:").strip()
    if city.lower() == "stop":
        break
    cities.append(city)

for city in cities:
    population = len(city) * 1000000
    print(f"The city {city} has {len(city)} letters, so its population is: {population}")

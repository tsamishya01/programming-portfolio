countries = {}  

while True:
    country_input = input("Enter a country (or press Enter to quit): ").strip()
    if country_input == "":
        print("Exiting program.")
        break

    country_key = country_input.lower()  
    if country_key in countries:
        print(f"The capital of {country_input.title()} is {countries[country_key]}.")
    else:
        capital = input(f"I don't know the capital of {country_input.title()}. Please enter it: ").strip()
        countries[country_key] = capital
        print(f"{country_input.title()} has been added with capital {capital}.")

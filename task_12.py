def startCountryPetition():
    countryInput = input("Please, insert a list of country separated by a comma and without spaces: ")
    cleanedCountries = map(lambda x:str(x).strip(), countryInput.split(","))
    listOfCountries = set(cleanedCountries)
    orderList = sorted(listOfCountries)
    capitalizedCountries = map(lambda x: str(x).capitalize(), orderList)
    print(", ".join(capitalizedCountries))

def main():
    startCountryPetition()

if __name__ == "__main__":
    main()
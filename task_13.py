from functools import reduce

def getSumFilteredElements(list):
    filterElements = filter(lambda x: x % 2 != 0, list)
    result = reduce(lambda a, b: int(a) + int(b), filterElements)
    print(f"The sum of odd numbers is: {result}")
def main():
    listOfElements = input("Insert the elements separated by comma: ")
    cleanElements = map(lambda x: int(str(x).strip()), listOfElements.split(","))
    nonRepite = set(cleanElements)
    getSumFilteredElements(nonRepite)

if __name__ == "__main__":
    main()
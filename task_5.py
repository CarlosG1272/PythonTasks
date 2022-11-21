# Function for determine leap year

def isBisiest(year):
    firstCondition = year % 4 == 0
    secondCondition = year % 100 != 0
    thirdCondition = year % 400 == 0
    return (firstCondition and secondCondition) or thirdCondition

print("Must be True values")
print(isBisiest(2020))
print(isBisiest(1984))
print(isBisiest(1040))
print("Must be False values")
print(isBisiest(2022))
print(isBisiest(2015))
print(isBisiest(1983))